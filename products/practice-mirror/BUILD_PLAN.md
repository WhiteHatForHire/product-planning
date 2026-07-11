# Practice Mirror - Build Plan

## Phase 0 - Repo setup

- Create app scaffold.
- Add UI shell.
- Add seed scenarios.
- Add environment docs.

## Phase 1 - Static prototype

- Scenario mode selector.
- Setup form.
- Static conversation screen.
- Static review screen.
- Seed scenario flow.

Exit criteria:

- Product can be demoed without AI using mocked responses.

## Phase 2 - Scenario Designer

- Add server route.
- Validate JSON output.
- Convert setup form into scenario plan.
- Start live session from generated plan.

Exit criteria:

- User can create a custom scenario.

## Phase 3 - Counterpart Actor

- Add live turn route.
- Maintain transcript.
- Update emotional temperature deterministically or from structured AI output.
- Ensure actor does not coach.

Exit criteria:

- User can run a 5-10 turn practice session.

## Phase 4 - Pause Coach

- Add pause state.
- Add concise hint route.
- Resume roleplay without losing state.

Exit criteria:

- User can get tactical help without ending the session.

## Phase 5 - Review

- Add review route.
- Add final script generation.
- Add review screen.
- Save/delete session locally.

Exit criteria:

- Completed session produces specific feedback and a useful final script.

## Phase 6 - Demo polish

- Improve visual hierarchy.
- Add 5 seed scenarios.
- Add loading and error states.
- Add transcript export.
- Add safety refusal copy for disallowed scenarios.

## First implementation order

1. Static UI.
2. Seed scenarios.
3. Scenario Designer.
4. Counterpart Actor.
5. Live Coach.
6. Review Coach.
7. Final script.
8. Export/delete.

