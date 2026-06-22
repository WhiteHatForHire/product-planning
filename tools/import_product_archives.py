#!/usr/bin/env python3
"""Import the product-planning zip archives into a searchable Markdown vault."""

from __future__ import annotations

import csv
import json
import re
import shutil
import unicodedata
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[1]

ARCHIVES = [
    (
        Path("/Users/marcusvale/Downloads/##Phronetics-20260621T181431Z-3-001.zip"),
        "Phronetics",
    ),
    (
        Path("/Users/marcusvale/Downloads/######Symposium Studios-20260622T005426Z-3-001.zip"),
        "Symposium Studios",
    ),
    (
        Path("/Users/marcusvale/Downloads/####Software Projects-20260622T005424Z-3-001.zip"),
        "Software Projects",
    ),
]

RESET_DIRS = [
    "products",
    "theory",
    "studio",
    "archive",
]

BINARY_EXTS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".mp4",
    ".mov",
    ".pdf",
    ".zip",
}

SECRET_PATTERNS = [
    "recovery-codes",
    "credential-tracker",
    "credentials",
    "password",
    "secret",
    "token",
    "api-key",
    "api key",
]

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
SS_NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


@dataclass
class ImportedDoc:
    archive: str
    source_path: str
    output_path: Path
    title: str
    route: str
    word_count: int
    privacy: str
    status: str
    tags: list[str]


@dataclass
class ManifestEntry:
    archive: str
    source_path: str
    size: int
    kind: str
    note: str


def clean_previous_outputs() -> None:
    for rel in RESET_DIRS:
        target = REPO_ROOT / rel
        if target.exists():
            shutil.rmtree(target)
    for rel in RESET_DIRS:
        (REPO_ROOT / rel).mkdir(parents=True, exist_ok=True)
    (REPO_ROOT / "archive" / "manifests").mkdir(parents=True, exist_ok=True)


def slugify(value: str, max_len: int = 96) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value or "untitled")[:max_len].strip("-")


def title_from_path(path: str) -> str:
    name = Path(path).name
    for suffix in [".docx", ".md", ".txt", ".xlsx"]:
        if name.lower().endswith(suffix):
            name = name[: -len(suffix)]
    name = re.sub(r"[_-]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name or "Untitled"


def extract_archives() -> Path:
    cache = REPO_ROOT / ".import-cache"
    if cache.exists():
        shutil.rmtree(cache)
    cache.mkdir()
    for archive_path, label in ARCHIVES:
        out = cache / label
        out.mkdir()
        with zipfile.ZipFile(archive_path) as zf:
            zf.extractall(out)
    return cache


def docx_to_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as zf:
            if "word/document.xml" not in zf.namelist():
                return ""
            tree = ET.fromstring(zf.read("word/document.xml"))
    except Exception as exc:
        return f"[DOCX_PARSE_ERROR: {exc}]"

    paragraphs: list[str] = []
    for para in tree.iter(W_NS + "p"):
        chunks: list[str] = []
        for node in para.iter():
            if node.tag == W_NS + "t" and node.text:
                chunks.append(node.text)
            elif node.tag == W_NS + "tab":
                chunks.append("\t")
            elif node.tag == W_NS + "br":
                chunks.append("\n")
        line = "".join(chunks).strip()
        if line:
            paragraphs.append(line)
    return "\n\n".join(paragraphs)


def xlsx_to_text(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as zf:
            names = zf.namelist()
            sheets: list[str] = []
            if "xl/workbook.xml" in names:
                tree = ET.fromstring(zf.read("xl/workbook.xml"))
                sheets = [node.attrib.get("name", "") for node in tree.iter(SS_NS + "sheet")]
            shared: list[str] = []
            if "xl/sharedStrings.xml" in names:
                tree = ET.fromstring(zf.read("xl/sharedStrings.xml"))
                for si in tree.iter(SS_NS + "si"):
                    text = "".join(t.text or "" for t in si.iter(SS_NS + "t")).strip()
                    if text:
                        shared.append(text)
    except Exception as exc:
        return f"[XLSX_PARSE_ERROR: {exc}]"

    lines = ["# Spreadsheet Summary", "", f"Sheets: {', '.join(sheets) or 'Unknown'}", ""]
    lines.append("## Shared Strings Sample")
    lines.extend(f"- {item}" for item in shared[:250])
    return "\n".join(lines).strip()


def plain_text(path: Path) -> str:
    data = path.read_bytes()
    if b"\x00" in data[:1000]:
        return ""
    return data.decode("utf-8", errors="replace")


def readable_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".docx":
        return docx_to_text(path)
    if ext == ".xlsx":
        return xlsx_to_text(path)
    if ext in {".md", ".txt", ""} or re.search(r"\.v\d+(\.\d+)?$", path.name):
        return plain_text(path)
    return ""


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_'-]+", text))


def privacy_for(source_path: str, text: str) -> str:
    haystack = f"{source_path}\n{text[:3000]}".lower()
    if "public" in haystack and "case study" in haystack:
        return "public-candidate"
    if any(term in haystack for term in ["confidential", "private", "internal only", "not for distribution"]):
        return "private/internal"
    return "working"


def status_for(source_path: str, text: str) -> str:
    haystack = f"{source_path}\n{text[:2000]}".lower()
    if any(term in haystack for term in ["archive", "/old/", "old/"]):
        return "archive"
    if any(term in haystack for term in ["active", "in flight", "build-ready", "production", "v1"]):
        return "active"
    if any(term in haystack for term in ["parked", "pre-build", "spec only", "shelve"]):
        return "parked"
    return "reference"


def tags_for(source_path: str) -> list[str]:
    text = source_path.lower()
    tags: list[str] = []
    for tag, needles in {
        "product": ["# products", "2 - project planning", "games ", "vsts"],
        "studio-os": ["#studio os", "symposium os", "agentic coding"],
        "theory": ["# theory", "phronetics", "directed emergence", "director model"],
        "career": ["career planning", "jobs-consulting", "resume", "salesman path"],
        "media": ["youtube", "writing", "channel", "variety show"],
        "website": ["websites", "site_overview", "copy_locked"],
        "case-study": ["case stud", "jamie stern", "eagle rocket"],
        "archive": ["archive", "/old/", "old/"],
    }.items():
        if any(needle in text for needle in needles):
            tags.append(tag)
    return tags or ["planning"]


def route_for(archive: str, source_path: str) -> Path:
    parts = source_path.split("/")
    lowered = source_path.lower()

    if archive == "Phronetics":
        if "/ai engine/" in lowered:
            return Path("products/phronetics-dialectical-combat")
        return Path("theory/phronetics")

    if archive == "Symposium Studios":
        if "# theory" in lowered:
            return Path("theory/directed-emergence")
        if "#studio os" in lowered:
            return Path("studio/symposium-os/source-notes")
        if "websites/" in lowered:
            return Path("studio/websites")
        if "jobs-consulting" in lowered or "# leveling up" in lowered:
            return Path("studio/positioning")
        if "# los angeles" in lowered:
            if "youtube" in lowered or "channel" in lowered or "variety show" in lowered:
                return Path("studio/media-youtube-writing")
            return Path("studio/offers-and-icp/la")
        if "writing/" in lowered:
            return Path("studio/media-youtube-writing/writing")
        if "new york city" in lowered:
            return Path("studio/events-and-fieldwork/new-york-city")
        if "# products " in lowered:
            try:
                idx = parts.index("# Products ")
                product = parts[idx + 1] if idx + 1 < len(parts) else ""
            except ValueError:
                product = ""
            mapping = {
                "Anchor Sobriety": "anchor",
                "Kairos app ": "kairos",
                "Dream Mirror ": "dream-mirror",
                "NYC Sublet Radar": "nyc-sublet-radar",
                "# Open Brain": "open-brain",
                "THE CAVE MVP": "games-and-experiments/the-cave",
                "Green Ford": "games-and-experiments/green-ford",
                "The Long Border": "games-and-experiments/the-long-border",
                "AI village tech demo ": "games-and-experiments/ai-village",
                "The virtue board ": "games-and-experiments/virtue-board",
            }
            return Path("products") / mapping.get(product, f"parked/{slugify(product)}")
        if "other ip" in lowered:
            return Path("products/parked/other-ip")
        return Path("studio/general")

    if archive == "Software Projects":
        if any(
            needle in lowered
            for needle in [
                "marcus_serious_build_checklist",
                "title_ marcus_s ai-native builder workflow",
                "prompt_ agentic code priming",
            ]
        ):
            return Path("theory/ai-native-builder-method")
        if "project 1_ the living landing page" in lowered:
            return Path("products/parked/living-landing-page")
        if "##insights" in lowered:
            return Path("theory/director-model")
        if "techne" in lowered or "ai native builder roadmap" in lowered:
            return Path("theory/ai-native-builder-method")
        if "# eagle rocket" in lowered or "jamie stern" in lowered:
            return Path("studio/case-studies/jamie-stern")
        if "career planning" in lowered:
            return Path("studio/positioning/career")
        if "vsts and music software" in lowered:
            return Path("products/parked/music-tools")
        if "games " in lowered:
            return Path("products/games-and-experiments")
        if "2 - project planning" in lowered:
            idx = parts.index("2 - Project planning") if "2 - Project planning" in parts else -1
            product = parts[idx + 1] if idx >= 0 and idx + 1 < len(parts) else "parked"
            mapping = {
                "#Neskala": "neskala",
                "4 Modes App": "four-modes",
                "The Arbiter": "arbiter",
                "The Propylaea": "propylaea",
                "Sober garden ": "sober-garden",
                "Manuscript forge": "manuscript-forge",
                "Councilflow": "councilflow",
                "#PatchBay": "patchbay",
            }
            return Path("products") / mapping.get(product, f"parked/{slugify(product)}")
        return Path("archive/reference-notes")

    return Path("archive/unrouted")


def is_secret(source_path: str) -> bool:
    normalized = source_path.lower().replace("_", "-")
    return any(pattern in normalized for pattern in SECRET_PATTERNS)


def markdown_doc(title: str, source_path: str, archive: str, text: str) -> str:
    privacy = privacy_for(source_path, text)
    status = status_for(source_path, text)
    tags = tags_for(source_path)
    frontmatter = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f'source_archive: "{archive}"',
        f'source_path: "{source_path.replace(chr(34), chr(39))}"',
        f"status: {status}",
        f"privacy: {privacy}",
        "tags:",
        *[f"  - {tag}" for tag in tags],
        "---",
        "",
        f"# {title}",
        "",
        "> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.",
        "",
    ]
    return "\n".join(frontmatter) + text.strip() + "\n"


def write_unique_markdown(route: Path, source_path: str, archive: str, text: str) -> ImportedDoc:
    title = title_from_path(source_path)
    out_dir = REPO_ROOT / route
    out_dir.mkdir(parents=True, exist_ok=True)
    base = slugify(title)
    out_path = out_dir / f"{base}.md"
    if out_path.exists():
        stem = slugify("/".join(Path(source_path).parts[-3:]))
        out_path = out_dir / f"{stem}.md"
    if out_path.exists():
        counter = 2
        while (out_dir / f"{base}-{counter}.md").exists():
            counter += 1
        out_path = out_dir / f"{base}-{counter}.md"
    out_path.write_text(markdown_doc(title, source_path, archive, text), encoding="utf-8")
    return ImportedDoc(
        archive=archive,
        source_path=source_path,
        output_path=out_path.relative_to(REPO_ROOT),
        title=title,
        route=str(route),
        word_count=word_count(text),
        privacy=privacy_for(source_path, text),
        status=status_for(source_path, text),
        tags=tags_for(source_path),
    )


def copy_nested_zip_markdown(source: Path, target: Path) -> list[ImportedDoc]:
    docs: list[ImportedDoc] = []
    if not source.exists():
        return docs
    tmp = REPO_ROOT / ".import-cache" / "_nested"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    with zipfile.ZipFile(source) as zf:
        zf.extractall(tmp)
    for item in tmp.rglob("*"):
        if item.is_dir():
            continue
        if item.suffix.lower() not in {".md", ".json", ".yml", ".yaml"}:
            continue
        rel = item.relative_to(tmp)
        out = REPO_ROOT / target / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        text = item.read_text(encoding="utf-8", errors="replace")
        out.write_text(text, encoding="utf-8")
        docs.append(
            ImportedDoc(
                archive="Nested package",
                source_path=str(source.name + "/" + str(rel)),
                output_path=out.relative_to(REPO_ROOT),
                title=title_from_path(str(rel)),
                route=str(target),
                word_count=word_count(text),
                privacy="working",
                status="reference",
                tags=["studio-os" if "symposium" in str(target) else "product"],
            )
        )
    return docs


def write_manifest(imported: list[ImportedDoc], binaries: list[ManifestEntry], quarantined: list[ManifestEntry]) -> None:
    manifests = REPO_ROOT / "archive" / "manifests"

    with (manifests / "imported-documents.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "archive",
                "source_path",
                "output_path",
                "route",
                "title",
                "word_count",
                "privacy",
                "status",
                "tags",
            ],
        )
        writer.writeheader()
        for doc in imported:
            writer.writerow(
                {
                    "archive": doc.archive,
                    "source_path": doc.source_path,
                    "output_path": str(doc.output_path),
                    "route": doc.route,
                    "title": doc.title,
                    "word_count": doc.word_count,
                    "privacy": doc.privacy,
                    "status": doc.status,
                    "tags": ";".join(doc.tags),
                }
            )

    lines = ["# Imported Documents", ""]
    by_route: dict[str, list[ImportedDoc]] = defaultdict(list)
    for doc in imported:
        by_route[doc.route].append(doc)
    for route in sorted(by_route):
        docs = sorted(by_route[route], key=lambda d: d.title.lower())
        lines.append(f"## {route}")
        lines.append("")
        for doc in docs:
            lines.append(
                f"- [{doc.title}](../../{doc.output_path}) - {doc.word_count} words - {doc.status} - {doc.privacy}"
            )
        lines.append("")
    (manifests / "imported-documents.md").write_text("\n".join(lines), encoding="utf-8")

    def write_entries(name: str, title: str, entries: list[ManifestEntry]) -> None:
        out = [f"# {title}", ""]
        for entry in sorted(entries, key=lambda e: (e.archive, e.source_path)):
            out.append(f"- `{entry.archive}` | `{entry.kind}` | {entry.size} bytes")
            out.append(f"  Source: `{entry.source_path}`")
            if entry.note:
                out.append(f"  Note: {entry.note}")
        out.append("")
        (manifests / name).write_text("\n".join(out), encoding="utf-8")

    write_entries("binary-assets.md", "Binary Assets Not Imported", binaries)
    write_entries("private-quarantine.md", "Private Or Sensitive Items Not Imported", quarantined)


def write_readmes(imported: list[ImportedDoc]) -> None:
    route_counts = Counter(doc.route for doc in imported)
    tag_counts = Counter(tag for doc in imported for tag in doc.tags)
    product_docs = [doc for doc in imported if str(doc.output_path).startswith("products/")]

    (REPO_ROOT / "README.md").write_text(
        """# Product Planning

Searchable planning vault for Symposium Studios, product ideas, studio operating doctrine, career/positioning material, and theory branches such as Phronetics and Directed Emergence.

This repo stores the readable planning layer. Raw zip archives, credentials, recovery codes, large media, Office originals, and private working files stay outside Git or under the ignored `private/` workspace.

Start here:

- [00-INDEX.md](00-INDEX.md)
- [01-ACTIVE-ROADMAP.md](01-ACTIVE-ROADMAP.md)
- [02-PRODUCT-PORTFOLIO.md](02-PRODUCT-PORTFOLIO.md)
- [03-THEORY-INDEX.md](03-THEORY-INDEX.md)
- [04-STUDIO-OS.md](04-STUDIO-OS.md)
- [archive/manifests/imported-documents.md](archive/manifests/imported-documents.md)

## Search

Use `rg "search term"` from the repo root, GitHub search, or any Markdown/Obsidian-style local indexer.
""",
        encoding="utf-8",
    )

    index = ["# Index", "", "## Major Areas", ""]
    for route, count in sorted(route_counts.items()):
        index.append(f"- `{route}` - {count} docs")
    index.extend(["", "## Tags", ""])
    for tag, count in sorted(tag_counts.items()):
        index.append(f"- `{tag}` - {count}")
    index.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not commit raw archives, credentials, recovery codes, or original Office files.",
            "- Treat Markdown imports as searchable working copies; provenance is kept in frontmatter.",
            "- Promote canonical docs by editing or summarizing them in place, not by piling on more copies.",
        ]
    )
    (REPO_ROOT / "00-INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")

    roadmap = """# Active Roadmap

## Current Recommendation

1. Keep this repo as the planning and search layer.
2. Promote canonical docs for active products before importing more raw material.
3. Keep sensitive material in `private/` or outside the repo.
4. Use product README files as the current source of truth; imported documents remain provenance and research.

## Immediate Priority Branches

- Anchor Sobriety: largest historical branch; needs a canonical current-state summary before more work.
- Kairos: preserve the bootstrap package and build log as a compact product planning branch.
- Dream Mirror: coherent product/spec branch with OS, prompt library, and builder bible.
- Phronetics / Dialectical Combat: theory plus pre-build product spec; keep parked but visible.
- Symposium OS: promote the nested `symposium-os-v0_3` package as studio operating infrastructure.
- Director Model / AI-native builder method: consolidate into public/private positioning material.
"""
    (REPO_ROOT / "01-ACTIVE-ROADMAP.md").write_text(roadmap, encoding="utf-8")

    portfolio = ["# Product Portfolio", ""]
    by_product: dict[str, list[ImportedDoc]] = defaultdict(list)
    for doc in product_docs:
        parts = Path(doc.output_path).parts
        key = "/".join(parts[:2]) if len(parts) >= 2 else "products"
        by_product[key].append(doc)
    for key in sorted(by_product):
        docs = sorted(by_product[key], key=lambda d: d.word_count, reverse=True)
        portfolio.append(f"## {key}")
        portfolio.append("")
        portfolio.append(f"- Documents: {len(docs)}")
        portfolio.append(f"- Total readable words: {sum(d.word_count for d in docs)}")
        portfolio.append("- Largest source docs:")
        for doc in docs[:5]:
            portfolio.append(f"  - [{doc.title}]({doc.output_path}) - {doc.word_count} words")
        portfolio.append("")
    (REPO_ROOT / "02-PRODUCT-PORTFOLIO.md").write_text("\n".join(portfolio), encoding="utf-8")

    theory = """# Theory Index

## Core Branches

- [Phronetics](theory/phronetics): practical judgment in motion; live conversational assessment/training.
- [Directed Emergence](theory/directed-emergence): governed AI-mediated game/simulation systems where state, not model improvisation, owns truth.
- [Director Model](theory/director-model): solo operator/product director model for AI-native software building.
- [AI-Native Builder Method](theory/ai-native-builder-method): toolchain, standards, and builder workflow material.

Use this section for durable concepts, not daily task lists.
"""
    (REPO_ROOT / "03-THEORY-INDEX.md").write_text(theory, encoding="utf-8")

    studio = """# Studio OS

This area holds the operating doctrine for Symposium Studios: templates, skills, positioning, websites, case studies, offers, and media strategy.

## Key Areas

- [Symposium OS](studio/symposium-os)
- [Positioning](studio/positioning)
- [Offers and ICP](studio/offers-and-icp)
- [Websites](studio/websites)
- [Case Studies](studio/case-studies)
- [Media, YouTube, and Writing](studio/media-youtube-writing)

The nested Symposium OS package has been unpacked under `studio/symposium-os/package/` so it can be searched and edited directly.
"""
    (REPO_ROOT / "04-STUDIO-OS.md").write_text(studio, encoding="utf-8")

    for route in sorted(route_counts):
        target = REPO_ROOT / route / "README.md"
        if target.exists():
            continue
        docs = sorted([doc for doc in imported if doc.route == route], key=lambda d: d.word_count, reverse=True)
        title = route.split("/")[-1].replace("-", " ").title()
        lines = [f"# {title}", "", f"Imported planning docs: {len(docs)}", ""]
        if docs:
            lines.append("## Largest Docs")
            lines.append("")
            for doc in docs[:10]:
                try:
                    rel = Path(doc.output_path).relative_to(route)
                except ValueError:
                    rel = Path(doc.output_path).name
                lines.append(f"- [{doc.title}]({rel.as_posix()}) - {doc.word_count} words")
            lines.append("")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines), encoding="utf-8")


def import_all() -> None:
    clean_previous_outputs()
    cache = extract_archives()
    imported: list[ImportedDoc] = []
    binaries: list[ManifestEntry] = []
    quarantined: list[ManifestEntry] = []

    for archive_root in cache.iterdir():
        if not archive_root.is_dir() or archive_root.name == "_nested":
            continue
        archive = archive_root.name
        for item in archive_root.rglob("*"):
            if item.is_dir():
                continue
            source_path = str(item.relative_to(archive_root))
            size = item.stat().st_size
            ext = item.suffix.lower()
            if is_secret(source_path):
                quarantined.append(ManifestEntry(archive, source_path, size, "sensitive", "Skipped by secret/credential/recovery filter."))
                continue
            if ext in BINARY_EXTS:
                binaries.append(ManifestEntry(archive, source_path, size, ext.lstrip(".") or "binary", "Tracked by manifest only."))
                continue
            text = readable_text(item)
            if not text.strip() or word_count(text) == 0:
                binaries.append(ManifestEntry(archive, source_path, size, ext.lstrip(".") or "unknown", "No readable text extracted."))
                continue
            route = route_for(archive, source_path)
            imported.append(write_unique_markdown(route, source_path, archive, text))

    kairos_zip = cache / "Symposium Studios" / "######Symposium Studios/# Products /Kairos app /Core app stuff /kairos-bootstrap.zip"
    symposium_zip = cache / "Symposium Studios" / "######Symposium Studios/#Studio OS/#SYMPOSIUM OS/symposium-os-v0_3.zip"
    imported.extend(copy_nested_zip_markdown(kairos_zip, Path("products/kairos/bootstrap-package")))
    imported.extend(copy_nested_zip_markdown(symposium_zip, Path("studio/symposium-os/package")))

    write_manifest(imported, binaries, quarantined)
    write_readmes(imported)

    summary = {
        "imported_docs": len(imported),
        "binary_manifest_entries": len(binaries),
        "quarantined_entries": len(quarantined),
        "routes": Counter(doc.route for doc in imported),
    }
    print(json.dumps(summary, indent=2, default=dict))


if __name__ == "__main__":
    import_all()
