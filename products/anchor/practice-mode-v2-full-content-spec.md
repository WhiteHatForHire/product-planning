---
title: "Practice Mode v2 — Full Content Spec"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Practice Mode v2 — Full Content Spec.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Practice Mode v2 — Full Content Spec

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Practice Mode V2

Build Directive

Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

Surfaces: artifacts/api-server/data/modules/ (module JSON files — verify path in Phase A), artifacts/recovery-checkin/src/components/practice/CompletionScreen.tsx, artifacts/recovery-checkin/src/pages/PracticeLibrary.tsx, artifacts/recovery-checkin/src/pages/Practice.tsx (escape link routing) Production impact: prompt change | UI change Council of Models: yes — required for Modules E, F, G, H before merge Auto-merge: no Credentials: gh Agent: CC Cloud

Role

You are implementing Practice Mode V2 for Anchor. This build rewrites six existing module JSON files, creates two new modules, adds commitment text personalization to the completion screen, wires repair node routing into the escape link, updates library ordering and descriptions, and removes SOS from completion tiny actions. All content is specified verbatim in this directive. Do not invent copy. You open a PR and stop — Council of Models review on Modules E, F, G, H is required before merge.

Do not expand scope into Insights stats, new practice routes, or any feature not listed in this directive.

Deployment Posture

PR-only stop. Auto-merge: no — prompt changes, Council required for four modules.

No schema migrations required. All changes are module JSON content, frontend component logic, and library display. No new DB tables.

No Fly secrets. No Vercel env changes.

Design Data

Module JSON file locations

Verify actual path in Phase A. Likely: artifacts/api-server/data/modules/ or artifacts/api-server/src/data/modules/. Each module is a separate .json file named [slug].json.

New fields added to all module JSON files

"library_description": string   — display text on the library card

"library_order": integer        — sort order in the library (1 = first)

New fields added to module outcome objects where applicable

"commitment_source_node_id": string   — which node's choice_label populates {choice} in commit_copy

"commit_copy_fallback": string        — static fallback if no matching choice found

Module version convention

Rewritten modules: v1.1.0 New modules: v1.0.0 Untouched module C: v1.0.1 (minor — SOS removal from tiny_actions only)

MODULE A: twenty-minute-urge — v1.1.0

library_order: 2 library_description: "For urges you can pause with. Add time and distance before the urge becomes a decision."

Full node tree:

{

"slug": "twenty-minute-urge",

"version": "1.1.0",

"title": "The 20-Minute Urge",

"library_description": "For urges you can pause with. Add time and distance before the urge becomes a decision.",

"library_order": 2,

"voice_exemplar": "Do not argue with the urge. Add time and distance.\n\nYou are not deciding forever. You are deciding the next 20 minutes.\n\nThe craving can be loud without being in charge.",

"contraindication": {

"global": false,

"block_on": ["medical_emergency", "self_harm", "active_use_cannot_stop", "overdose_risk"],

"module_copy": "This practice is for urges you can pause with.\n\nIf you might hurt yourself, overdose, or cannot stay safe for the next few minutes, use SOS support now.",

"module_buttons": ["Open SOS support", "Continue practice"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "You do not have to beat the urge forever.\n\nYou only have to put 20 minutes between the urge and the next action.",

"choices": [

{ "key": "start", "label": "Start", "next": "concept" }

]

},

{

"id": "concept",

"type": "concept",

"copy": "Urges rise, peak, and pass. They usually feel permanent while they are happening.\n\nThis practice is not about winning. It is about delaying the automatic move.",

"next": "practice_1"

},

{

"id": "practice_1",

"type": "practice",

"copy": "What kind of urge is this?",

"choices": [

{ "key": "use_or_drink",      "label": "Use or drink",                           "next": "practice_2" },

{ "key": "text_wrong_person", "label": "Text the wrong person",                 "next": "practice_2" },

{ "key": "buy_or_order",      "label": "Buy or order something I'll regret",    "next": "practice_2" },

{ "key": "disappear",         "label": "Disappear or shut everyone out",         "next": "practice_2" },

{ "key": "hard_to_name",      "label": "Hard to name — just activated",         "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "Where is the trigger right now?",

"choices": [

{ "key": "on_phone",       "label": "On my phone",          "response": "Put the phone somewhere inconvenient. The goal is not discipline. The goal is friction.",              "next": "practice_3" },

{ "key": "in_my_room",     "label": "In my room",           "response": "Change the room before you keep negotiating with the urge.",                                           "next": "practice_3" },

{ "key": "in_my_body",     "label": "In my body",           "response": "Stabilize the body before you trust the story your mind is telling.",                                  "next": "practice_3" },

{ "key": "nearby",         "label": "Nearby — easy access", "response": "Put distance between you and the access point. You do not have to remove it forever. Just now.",       "next": "practice_3" },

{ "key": "message_thread", "label": "In a message thread",  "response": "Close the thread. You do not have to respond yet.",                                                    "next": "practice_3" },

{ "key": "not_sure",       "label": "Not sure",             "response": "That is fine. Choose the interruption that creates the most friction between the urge and the action.", "next": "practice_3" }

]

},

{

"id": "practice_3",

"type": "practice",

"copy": "Pick one interruption for the next 20 minutes.",

"choices": [

{ "key": "move_body",          "label": "Move my body",                               "response": "Stand up now. Change your body state before you keep thinking about the urge.",            "next": "practice_4" },

{ "key": "change_rooms",       "label": "Change rooms or step outside",               "response": "Move your body through a door before the urge moves you somewhere else.",                   "next": "practice_4" },

{ "key": "text_sober_contact", "label": "Text a sober contact",                      "response": "Contact before explanation. The message can be one sentence.",                              "next": "practice_4" },

{ "key": "water_food",         "label": "Drink water or eat something",               "response": "Stabilize the body. A stabilized body tells a quieter story.",                             "next": "practice_4" },

{ "key": "distance",           "label": "Put distance between me and the trigger",   "response": "Distance is the intervention. You do not need to solve anything right now.",               "next": "practice_4" },

{ "key": "timer",              "label": "Start a 20-minute timer and do nothing else","response": "The timer is the practice. You are not doing nothing — you are creating space.",          "next": "practice_4" }

]

},

{

"id": "practice_4",

"type": "practice",

"copy": "What is the urge saying?",

"choices": [

{ "key": "just_this_once",   "label": "\"Just this once won't matter\"",   "response": "The urge is trying to make a permanent choice sound temporary. You do not have to answer it.",        "next": "synthesis" },

{ "key": "deserve_relief",   "label": "\"I deserve relief\"",              "response": "Relief is real. So is the cost. Choose relief that does not create more damage.",                     "next": "synthesis" },

{ "key": "already_ruined",   "label": "\"Today is already ruined\"",       "response": "That is the momentum trap. The next action still matters. This moment is not the whole day.",         "next": "synthesis" },

{ "key": "no_one_will_know", "label": "\"No one will know\"",              "response": "Secrecy is part of the risk. Contact breaks the spell.",                                              "next": "synthesis" },

{ "key": "cant_stand_it",    "label": "\"I can't stand this feeling\"",    "response": "You do not have to stand it forever. Stand it for the next few minutes. That is all.",               "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "If this practice feels too small, that may be the point.\n\nChoose the smallest action that interrupts the next move.",

"choices": [

{ "key": "text_person", "label": "Text one person",              "next": "synthesis" },

{ "key": "move_body",   "label": "Move my body for two minutes", "next": "synthesis" },

{ "key": "exit",        "label": "Exit Practice",                "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "An urge does not need a debate. It needs distance, time, and contact."

}

],

"outcome": {

"commitment_source_node_id": "practice_3",

"commit_copy": "For the next 20 minutes, I will {choice} before acting on the urge.",

"commit_copy_fallback": "For the next 20 minutes, I will not act on the urge.",

"tiny_actions": [

{ "key": "set_timer",    "label": "Start a 20-minute timer" },

{ "key": "text_contact", "label": "Text a sober contact now" },

{ "key": "drink_water",  "label": "Drink a glass of water" },

{ "key": "change_rooms", "label": "Change rooms or step outside" }

],

"saved_copy": "Saved. Come back before the urge turns into a decision."

}

}

MODULE B: holding-a-no — v1.1.0

library_order: 5 library_description: "For practicing a boundary under ongoing pressure — money, time, emotional access, guilt, repeated asking."

Note: Module B is for ongoing boundary pressure only. It does not handle substance offers — that is Module D.

{

"slug": "holding-a-no",

"version": "1.1.0",

"title": "Holding a No When Asked",

"library_description": "For practicing a boundary under ongoing pressure — money, time, emotional access, guilt, repeated asking.",

"library_order": 5,

"voice_exemplar": "The no does not need a courtroom argument.\n\nGuilt can show up even when the boundary is right.\n\nSay it once. Repeat if needed. Then act.",

"contraindication": {

"global": false,

"block_on": ["physical_danger", "abuse", "coercion", "immediate_safety_risk"],

"module_copy": "If saying no could put you in danger, prioritize safety and support.\n\nThis practice is for boundaries, not dangerous confrontation.",

"module_buttons": ["Practice a boundary", "Open SOS support", "Save and exit"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "A no does not need to become a courtroom argument.\n\nYou can be clear without making a case.",

"choices": [{ "key": "start", "label": "Start", "next": "concept" }]

},

{

"id": "concept",

"type": "concept",

"copy": "Many boundaries fail because they become explanations.\n\nA strong no is brief, repeatable, and connected to action.",

"next": "practice_1"

},

{

"id": "practice_1",

"type": "practice",

"copy": "What kind of pressure are you practicing for?",

"choices": [

{ "key": "time",         "label": "Pressure on my time",           "next": "practice_2" },

{ "key": "money",        "label": "Pressure for money",            "next": "practice_2" },

{ "key": "emotional",    "label": "Pressure for emotional access", "next": "practice_2" },

{ "key": "explain",      "label": "Pressure to explain myself",    "next": "practice_2" },

{ "key": "keeps_asking", "label": "Someone who keeps asking",      "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "Choose your boundary script.",

"choices": [

{ "key": "time",      "label": "Time",             "response": "I can't do that today.",                                       "next": "practice_3" },

{ "key": "money",     "label": "Money",            "response": "I'm not able to give money.",                                  "next": "practice_3" },

{ "key": "emotional", "label": "Emotional access", "response": "I'm not available for this conversation right now.",            "next": "practice_3" },

{ "key": "explain",   "label": "Explaining myself","response": "I don't need to explain this further. My answer is the same.", "next": "practice_3" },

{ "key": "repeat",    "label": "Repeat pressure",  "response": "I already answered. I'm not going to keep discussing it.",     "next": "practice_3" }

]

},

{

"id": "practice_3",

"type": "practice",

"copy": "What happens when you say it?",

"choices": [

{ "key": "they_push",        "label": "They push harder",              "response": "Repeat the same line once. Then stop responding or leave. You do not owe a better argument.",           "next": "synthesis" },

{ "key": "they_act_hurt",    "label": "They act hurt or disappointed", "response": "Guilt can show up even when the boundary is right. Their disappointment is not proof the no is wrong.",  "next": "synthesis" },

{ "key": "they_make_urgent", "label": "They make it urgent",           "response": "Urgency is a negotiation tactic. The no does not need to change because the pressure increases.",         "next": "synthesis" },

{ "key": "i_feel_guilty",    "label": "I feel guilty immediately",     "response": "That feeling is normal. It is not a signal to reverse the boundary. It is a signal to hold it.",         "next": "synthesis" },

{ "key": "they_stop",        "label": "They stop asking",              "response": "Good. The boundary worked. Note what made it work.",                                                       "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "Guilt can show up even when the boundary is right.\n\nDo not use guilt as the only measure of whether the no is allowed.",

"choices": [

{ "key": "softer_no",      "label": "Try a softer no",                "next": "synthesis" },

{ "key": "firmer_no",      "label": "Try a firmer no",                "next": "synthesis" },

{ "key": "follow_through", "label": "Choose how I'll follow through", "next": "practice_3" },

{ "key": "exit",           "label": "Save and exit",                  "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "The boundary is not real because it sounds perfect.\n\nIt is real because you follow it with action."

}

],

"outcome": {

"commit_copy": "I will give one clear no and not keep negotiating after it.",

"tiny_actions": [

{ "key": "save_script",  "label": "Save the script" },

{ "key": "mute_block",   "label": "Mute or block the thread" },

{ "key": "text_contact", "label": "Text a sober contact" },

{ "key": "plan_exit",    "label": "Plan how I'll leave" }

],

"saved_copy": "Saved. You can come back when the pressure is closer."

}

}

MODULE C: ask-for-help — v1.0.1

library_order: 3 library_description: "For when you need to reach out but do not know what to say. No speech required."

Change only: remove { "key": "open_sos", "label": "Open SOS support" } from tiny_actions. Update version to 1.0.1. Add library_description and library_order fields. No node changes.

MODULE D: declining-the-offer — v1.1.0

library_order: 6 library_description: "For direct substance or alcohol offers in social settings. Short is stronger."

Note: Module D is for direct substance/alcohol offers only. Ongoing boundary pressure is Module B.

{

"slug": "declining-the-offer",

"version": "1.1.0",

"title": "Declining the Offer",

"library_description": "For direct substance or alcohol offers in social settings. Short is stronger.",

"library_order": 6,

"voice_exemplar": "Short is stronger.\n\nYou do not need to make recovery understandable to everyone in the room.\n\nRepeat the line. Leave if needed.",

"contraindication": {

"global": false,

"block_on": ["physical_danger", "coercion", "unsafe_situation", "medical_emergency"],

"module_copy": "If saying no could make you unsafe, focus on leaving or contacting support first.\n\nA script is not more important than safety.",

"module_buttons": ["Practice a script", "Open SOS support", "Save and exit"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "You do not need to explain your recovery to decline an offer.\n\nShort is stronger.",

"choices": [{ "key": "start", "label": "Start", "next": "concept" }]

},

{

"id": "concept",

"type": "concept",

"copy": "The longer the explanation, the more room there is for negotiation.\n\nA good refusal is brief, calm, and repeatable.",

"next": "practice_1"

},

{

"id": "practice_1",

"type": "practice",

"copy": "What kind of offer are you preparing for?",

"choices": [

{ "key": "friend_inperson", "label": "A friend offering in person",  "next": "practice_2" },

{ "key": "text_dm",         "label": "A text or DM offer",           "next": "practice_2" },

{ "key": "date_social",     "label": "A date or social event",       "next": "practice_2" },

{ "key": "work_family",     "label": "Work or family setting",       "next": "practice_2" },

{ "key": "general",         "label": "Just want a general script",   "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "Choose your script.",

"choices": [

{ "key": "direct",    "label": "Direct: about my recovery", "response": "No thanks. I'm not drinking or using.",                  "next": "practice_3" },

{ "key": "soft",      "label": "Soft: no explanation",      "response": "I'm good, thank you.",                                   "next": "practice_3" },

{ "key": "boundary",  "label": "Boundary line",             "response": "Please don't offer that to me.",                         "next": "practice_3" },

{ "key": "exit_line", "label": "Exit line",                 "response": "I'm going to head out. I'll catch you later.",            "next": "practice_3" },

{ "key": "text",      "label": "Text reply",                "response": "I'm not doing that anymore. Please don't send me that.", "next": "practice_3" }

]

},

{

"id": "practice_3",

"type": "practice",

"copy": "If they push back, what do you do?",

"choices": [

{ "key": "repeat",         "label": "Repeat the same line",             "response": "Once more, same words. Then stop engaging. You do not need a better argument.",   "next": "synthesis" },

{ "key": "change_subject", "label": "Change the subject",               "response": "Move on without explanation. The redirect is the boundary.",                      "next": "synthesis" },

{ "key": "leave",          "label": "Leave the situation",              "response": "An early exit is not a failure. It is the right move.",                           "next": "synthesis" },

{ "key": "text_contact",   "label": "Text a sober contact for support", "response": "Contact before the situation gets harder. One message is enough.",                "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "Choose the version that creates the least drama and still protects you.",

"choices": [

{ "key": "im_good",       "label": "\"I'm good, thank you\"",     "response": "I'm good, thank you.",     "next": "synthesis" },

{ "key": "early_morning", "label": "\"I have an early morning\"", "response": "I have an early morning.", "next": "synthesis" },

{ "key": "taking_break",  "label": "\"I'm taking a break\"",      "response": "I'm taking a break.",      "next": "synthesis" },

{ "key": "head_out",      "label": "\"I need to head out\"",      "response": "I need to head out.",      "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "A refusal is not a debate. It is a door closing."

}

],

"outcome": {

"commit_copy": "I will use one short line and not negotiate with the offer.",

"tiny_actions": [

{ "key": "save_script", "label": "Save the script I picked" },

{ "key": "text_before", "label": "Text support before the event" },

{ "key": "plan_exit",   "label": "Plan an early exit" }

],

"saved_copy": "Saved. A simple line is ready when you need it."

}

}

MODULE E: lapse-vs-relapse — v1.1.0 (COUNCIL REQUIRED)

Title change: "After Something Happened" Slug unchanged: lapse-vs-relapse library_order: 8 library_description: "For when you are stable enough to understand what happened. Accountability without shame."

{

"slug": "lapse-vs-relapse",

"version": "1.1.0",

"title": "After Something Happened",

"library_description": "For when you are stable enough to understand what happened. Accountability without shame.",

"library_order": 8,

"voice_exemplar": "Something happened. That matters. It does not get to define the whole story.\n\nAccountability can be real without turning this into a verdict.\n\nThe next useful question is what keeps this from getting bigger.",

"contraindication": {

"global": false,

"block_on": ["active_use", "active_intoxication", "medical_emergency", "self_harm", "active_relapse_disclosure"],

"module_copy": "This practice is for understanding what happened, not for handling an active risky moment.\n\nIf this just happened or you are still at risk, use the relapse response flow first.",

"module_buttons": ["Open relapse response", "Open SOS support", "Continue anyway"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "Something happened. That matters.\n\nIt does not get to define the whole story.",

"choices": [{ "key": "start", "label": "Start", "next": "concept" }]

},

{

"id": "concept",

"type": "concept",

"copy": "A single event and a sustained pattern are different things. Both can be true at different times.\n\nAnchor does not decide which one this is. You do. But the next useful question is the same either way: what keeps this from getting bigger?",

"choices": [

{ "key": "makes_sense", "label": "That makes sense",       "next": "practice_1" },

{ "key": "not_sure",    "label": "I'm not sure yet",       "next": "practice_1" },

{ "key": "doesnt_fit",  "label": "This frame doesn't fit", "next": "repair_1" }

]

},

{

"id": "practice_1",

"type": "practice",

"copy": "Which is closest to what happened?",

"choices": [

{ "key": "one_use",         "label": "One event, then I stopped",          "response": "Then the next task is containment. Do not turn one event into a bigger pattern.",                          "next": "practice_2" },

{ "key": "kept_going",      "label": "I used and kept going for a while",  "response": "Then the next task is interruption. The goal is to stop the pattern from gaining more momentum.",        "next": "practice_2" },

{ "key": "lost_everything", "label": "I feel like I've lost everything",   "response": "That is the shame story. Accountability can be real without saying your prior work is erased.",          "next": "practice_2" },

{ "key": "dont_know",       "label": "I don't know yet",                   "response": "Not knowing yet is allowed. Start with what is observable. The label can come later.",                   "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "What would make this less likely to grow?",

"choices": [

{ "key": "tell_person",    "label": "Tell one safe person today",             "next": "synthesis" },

{ "key": "remove_access",  "label": "Remove access to what I used",          "next": "synthesis" },

{ "key": "meeting",        "label": "Go to a meeting or support call",       "next": "synthesis" },

{ "key": "reset_count",    "label": "Reset my day count and keep going",     "next": "synthesis" },

{ "key": "write_warnings", "label": "Write down the warning signs I missed", "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "That is fine. The frame does not need to fit.\n\nWhat is actually useful right now?",

"choices": [

{ "key": "be_safe",     "label": "I just need to be safe right now",    "next": "synthesis" },

{ "key": "stuck_shame", "label": "I'm stuck in shame",                  "next": "synthesis" },

{ "key": "my_program",  "label": "My program's own definition matters", "next": "practice_2" },

{ "key": "skip",        "label": "Skip this practice",                  "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "The useful question is not, \"What does this make me?\"\n\nThe useful question is, \"What action keeps this from getting bigger?\""

}

],

"outcome": {

"commit_copy": "I will take one honest action before this becomes a bigger pattern.",

"tiny_actions": [

{ "key": "text_person",    "label": "Text one safe person now" },

{ "key": "update_tracker", "label": "Update my tracker honestly" },

{ "key": "meeting_link",   "label": "Open a meeting link" },

{ "key": "write_missed",   "label": "Write down what I missed" },

{ "key": "relapse_flow",   "label": "Open the relapse response flow" }

],

"saved_copy": "Saved. You can come back when the shame is quieter."

}

}

MODULE F: what-to-do-after-slip — v1.1.0 (COUNCIL REQUIRED)

library_order: 7 library_description: "For immediately after a slip, or to rehearse the response. Containment, honesty, support."

{

"slug": "what-to-do-after-slip",

"version": "1.1.0",

"title": "What to Do After a Slip",

"library_description": "For immediately after a slip, or to rehearse the response. Containment, honesty, support.",

"library_order": 7,

"voice_exemplar": "Do not disappear with this.\n\nShame wants the slip to become a pattern. Contact interrupts that.\n\nOne honest action now matters.",

"contraindication": {

"global": false,

"block_on": ["active_slip_today", "still_at_risk", "medical_emergency", "self_harm"],

"module_copy": "If the slip just happened, use the relapse response flow first.\n\nThis practice is for rehearsing what to do after a slip, not for handling an active risky moment.",

"module_buttons": ["Open relapse response", "Practice anyway", "Open SOS support"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "After a slip, the next few moves matter.\n\nNot because everything is ruined — but because shame can make things worse fast.",

"choices": [{ "key": "start", "label": "Start", "next": "concept" }]

},

{

"id": "concept",

"type": "concept",

"copy": "The goal after a slip is not to punish yourself.\n\nThe goal is to stop hiding, reduce harm, and reconnect with support.",

"next": "practice_1"

},

{

"id": "practice_1",

"type": "practice",

"copy": "What is the first move?",

"choices": [

{ "key": "tell_person",    "label": "Tell one safe person",       "response": "Contact breaks the isolation loop. The message can be one sentence.",                 "next": "practice_2" },

{ "key": "water_food",     "label": "Water and food",             "response": "Stabilize the body first. A stabilized body tells a quieter story.",                  "next": "practice_2" },

{ "key": "move_away",      "label": "Move away from access",      "response": "Distance is the first intervention. You do not have to remove it forever. Just now.",  "next": "practice_2" },

{ "key": "update_tracker", "label": "Update my tracker honestly", "response": "Honesty with yourself before honesty with anyone else.",                              "next": "practice_2" },

{ "key": "meeting",        "label": "Get to a meeting",           "response": "A room of people who understand is one of the fastest ways to interrupt the pattern.", "next": "practice_2" },

{ "key": "write_sentence", "label": "Write one honest sentence",  "response": "One sentence is enough. You do not need to explain everything.",                       "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "Which shame thought usually shows up?",

"choices": [

{ "key": "ruined_everything", "label": "\"I've ruined everything\"",               "response": "Something happened. That is real. Your prior work is not erased by it. The next action still matters.",                                                "next": "practice_3" },

{ "key": "cant_tell_anyone",  "label": "\"I can't tell anyone\"",                  "response": "Secrecy is what lets the slip grow. Contact does not have to be a confession. One sentence is enough.",                                               "next": "practice_3" },

{ "key": "keep_going",        "label": "\"Might as well keep going\"",             "response": "That is the continuation trap. The earlier you interrupt the pattern, the easier it is to come back. Make the interruption now.",                      "next": "practice_3" },

{ "key": "couldnt_do_right",  "label": "\"I couldn't even do this right\"",       "response": "This is not a verdict on your capacity. It is a moment that needs a response, not a judgment.",                                                       "next": "practice_3" },

{ "key": "dont_think",        "label": "\"I just don't want to think about it\"", "response": "You do not need to analyze it fully. You need one honest action. That is all this asks.",                                                              "next": "practice_3" }

]

},

{

"id": "practice_3",

"type": "practice",

"copy": "What kind of accountability fits your recovery?",

"choices": [

{ "key": "reset_count",  "label": "Reset my day count",                        "next": "synthesis" },

{ "key": "record_only",  "label": "Record it without resetting",               "next": "synthesis" },

{ "key": "tell_sponsor", "label": "Tell my sponsor or accountability partner", "next": "synthesis" },

{ "key": "meeting",      "label": "Bring it to a meeting",                     "next": "synthesis" },

{ "key": "decide_later", "label": "Decide later — just stabilize now",         "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "Then do the smallest version.\n\nOne honest sentence. One glass of water. One message. No speech.",

"choices": [

{ "key": "write_sentence", "label": "Write one honest sentence",      "next": "synthesis" },

{ "key": "text_person",    "label": "Text one person",                "next": "synthesis" },

{ "key": "relapse_flow",   "label": "Open the relapse response flow", "next": "synthesis" },

{ "key": "exit",           "label": "Save and exit",                  "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "A slip asks for honesty, not self-destruction.\n\nThe next action helps keep this from getting bigger."

}

],

"outcome": {

"commitment_source_node_id": "practice_1",

"commit_copy": "If I slip, I will {choice} before I disappear with it.",

"commit_copy_fallback": "If I slip, I will tell one safe person before I disappear with it.",

"tiny_actions": [

{ "key": "save_message",   "label": "Save a short support message" },

{ "key": "cleanup_action", "label": "Choose one cleanup action" },

{ "key": "relapse_flow",   "label": "Open the relapse response flow" }

],

"saved_copy": "Saved. You have a plan for the moment shame tries to take over."

}

}

MODULE G: halt-check — v1.0.0 NEW (COUNCIL REQUIRED)

library_order: 1 library_description: "A quick check on the four conditions that most often make recovery harder. Hungry, angry, lonely, or tired."

{

"slug": "halt-check",

"version": "1.0.0",

"title": "HALT Check",

"library_description": "A quick check on the four conditions that most often make recovery harder. Hungry, angry, lonely, or tired.",

"library_order": 1,

"voice_exemplar": "Hungry, angry, lonely, tired.\n\nThese are not character flaws. They are conditions that can make the next choice harder.\n\nName the condition. Address it directly.",

"contraindication": {

"global": false,

"block_on": ["medical_emergency", "self_harm", "active_use_cannot_stop"],

"module_copy": "If you are in immediate danger, use SOS support now.\n\nThis practice is for noticing conditions that can make recovery harder before they become decision points.",

"module_buttons": ["Open SOS support", "Continue practice"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "Four conditions can make recovery harder fast.\n\nHungry. Angry or activated. Lonely. Tired.\n\nThis practice names the condition so you can address it directly.",

"choices": [{ "key": "start", "label": "Start", "next": "practice_1" }]

},

{

"id": "practice_1",

"type": "practice",

"copy": "Which is most true right now? Pick the closest one.",

"choices": [

{ "key": "hungry",   "label": "Hungry — I haven't eaten properly",  "response": "Eat something before you make any decisions. A stabilized body tells a quieter story.",                                             "next": "practice_2" },

{ "key": "angry",    "label": "Angry or activated — something hit", "response": "You are activated. That means the part of your brain making decisions is under pressure. Add time before acting.",               "next": "practice_2" },

{ "key": "lonely",   "label": "Lonely — isolated or disconnected",  "response": "Isolation is one of the most reliable paths back to using. Contact interrupts it, even brief contact.",                          "next": "practice_2" },

{ "key": "tired",    "label": "Tired — sleep-deprived or depleted", "response": "Fatigue makes every decision feel heavier. Rest is a recovery action, not an indulgence.",                                       "next": "practice_2" },

{ "key": "all",      "label": "Multiple — more than one",           "response": "More than one HALT condition can make things feel louder. Address the easiest one first. Do not try to solve all of them right now.", "next": "practice_2" },

{ "key": "not_sure", "label": "Not sure — just feel off",           "response": "Feeling off without a clear reason can be all four at once showing up quietly. Pick the one that might be true and address it.",  "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "What is the direct address for this condition?",

"choices": [

{ "key": "eat_now",      "label": "Eat something now",                    "response": "Before anything else. Even something small.",                                                    "next": "synthesis" },

{ "key": "contact",      "label": "Contact one person",                   "response": "One message. Not a speech. Contact before the isolation gets louder.",                           "next": "synthesis" },

{ "key": "rest",         "label": "Rest — lie down or step away",         "response": "Rest is a recovery action. You are not giving up. You are making the next choice easier.",      "next": "synthesis" },

{ "key": "move_body",    "label": "Move my body",                         "response": "Walk, stretch, step outside. Activated bodies need to move.",                                    "next": "synthesis" },

{ "key": "delay_choice", "label": "Delay any big decision for one hour",  "response": "No big decisions while any HALT condition is active. One hour minimum.",                        "next": "synthesis" },

{ "key": "drink_water",  "label": "Drink water and eat something",        "response": "Body first. Every time.",                                                                        "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "You do not have to fix the condition right now.\n\nYou only have to name it and choose one small address.",

"choices": [

{ "key": "eat",     "label": "Eat something",          "next": "synthesis" },

{ "key": "contact", "label": "Text one person",        "next": "synthesis" },

{ "key": "rest",    "label": "Lie down for 10 minutes","next": "synthesis" },

{ "key": "exit",    "label": "Save and exit",          "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "Name the condition. Address it directly.\n\nThat is the whole practice."

}

],

"outcome": {

"commitment_source_node_id": "practice_2",

"commit_copy": "I will {choice} before I make any decisions while this condition is active.",

"commit_copy_fallback": "I will address this condition before I make any decisions.",

"tiny_actions": [

{ "key": "eat_now",      "label": "Eat something now" },

{ "key": "drink_water",  "label": "Drink water" },

{ "key": "text_contact", "label": "Text one person" },

{ "key": "lie_down",     "label": "Lie down for 10 minutes" },

{ "key": "delay",        "label": "No big decisions for one hour" }

],

"saved_copy": "Saved. You know what condition to watch for."

}

}

MODULE H: dont-go-back — v1.0.0 NEW (COUNCIL REQUIRED)

library_order: 4 library_description: "For when you are about to text or re-engage with someone you should not. The pull feels urgent. It usually is not."

{

"slug": "dont-go-back",

"version": "1.0.0",

"title": "Don't Go Back",

"library_description": "For when you are about to text or re-engage with someone you should not. The pull feels urgent. It usually is not.",

"library_order": 4,

"voice_exemplar": "The pull to re-contact is almost never about the message.\n\nIt is about the discomfort of not knowing.\n\nYou can tolerate not knowing. That is what this practice builds.",

"contraindication": {

"global": false,

"block_on": ["immediate_safety_risk", "abuse", "coercion"],

"module_copy": "If this person makes you unsafe, prioritize safety and support first.\n\nThis practice is for emotional pull, not dangerous situations.",

"module_buttons": ["Practice anyway", "Open SOS support"]

},

"completion_node": "synthesis",

"nodes": [

{

"id": "hook",

"type": "hook",

"copy": "The urge to reach out can feel like it will not stop until you do.\n\nIt will stop. Not because you argued it down — because you gave it time.",

"choices": [{ "key": "start", "label": "Start", "next": "practice_1" }]

},

{

"id": "practice_1",

"type": "practice",

"copy": "Who is the pull toward?",

"choices": [

{ "key": "ex_partner",   "label": "An ex or past partner",        "next": "practice_2" },

{ "key": "using_friend", "label": "Someone I used with",          "next": "practice_2" },

{ "key": "source",       "label": "A dealer or source",           "next": "practice_2" },

{ "key": "conflict",     "label": "Someone I'm in conflict with", "next": "practice_2" },

{ "key": "dont_know",    "label": "I'm not sure why I want to",   "next": "practice_2" }

]

},

{

"id": "practice_2",

"type": "practice",

"copy": "What is the pull actually asking for?",

"choices": [

{ "key": "relief",     "label": "Relief from this feeling",     "response": "Relief is real. Reaching out to this person is not where it lives.",                                    "next": "practice_3" },

{ "key": "certainty",  "label": "To know how they feel",        "response": "The pull to know is the discomfort of uncertainty. You can tolerate not knowing. That is the practice.", "next": "practice_3" },

{ "key": "connection", "label": "To feel connected to someone", "response": "The need is real. This person is not the right address for it right now.",                             "next": "practice_3" },

{ "key": "make_right", "label": "To fix or explain something",  "response": "The urge to make it right can be real and still be bad timing. The explanation can wait.",             "next": "practice_3" },

{ "key": "not_sure",   "label": "Not sure — just compelled",    "response": "Compulsion without a clear reason is usually the urge for relief. Do not act on it for 20 minutes.",   "next": "practice_3" }

]

},

{

"id": "practice_3",

"type": "practice",

"copy": "What do you do instead?",

"choices": [

{ "key": "write_draft",  "label": "Write the message — do not send it", "response": "Write it. Get it out. Do not send it for at least 20 minutes. Most drafts stay drafts.",        "next": "synthesis" },

{ "key": "text_contact", "label": "Text a sober contact instead",       "response": "Redirect the contact urge to someone it is safe to reach.",                                     "next": "synthesis" },

{ "key": "delay_20",     "label": "Wait 20 minutes before deciding",    "response": "The 20-minute rule applies here too. If you still want to send it in 20 minutes, decide then.", "next": "synthesis" },

{ "key": "move_body",    "label": "Move my body",                        "response": "Physical movement interrupts the pull faster than thinking does.",                              "next": "synthesis" },

{ "key": "close_app",    "label": "Close the app or thread",             "response": "Access creates the illusion of decision. Remove the access.",                                  "next": "synthesis" }

]

},

{

"id": "repair_1",

"type": "repair",

"copy": "The pull feels urgent. It usually is not.\n\nChoose the smallest move that creates friction between the urge and the action.",

"choices": [

{ "key": "write_draft",  "label": "Write it without sending",  "next": "synthesis" },

{ "key": "text_contact", "label": "Text someone else instead", "next": "synthesis" },

{ "key": "delay",        "label": "Wait 20 minutes",           "next": "synthesis" },

{ "key": "exit",         "label": "Save and exit",             "next": "synthesis" }

]

},

{

"id": "synthesis",

"type": "synthesis",

"copy": "The pull is not a command.\n\nIt is a signal that something needs addressing — but not necessarily by reaching out to that person."

}

],

"outcome": {

"commitment_source_node_id": "practice_3",

"commit_copy": "I will {choice} instead of sending the message.",

"commit_copy_fallback": "I will not reach out to this person right now.",

"tiny_actions": [

{ "key": "write_draft",  "label": "Write a draft — do not send" },

{ "key": "text_contact", "label": "Text a sober contact instead" },

{ "key": "delay_timer",  "label": "Set a 20-minute timer" },

{ "key": "close_app",    "label": "Close the app or thread" }

],

"saved_copy": "Saved. The urge will pass. You do not have to act on it."

}

}

Commitment text personalization — implementation spec

Frontend logic (CompletionScreen.tsx)

When the module outcome has commitment_source_node_id:

Read the user's logged choices for this session from local state (the array of practice_choices entries recorded as the user progressed through the module)

Find the entry where node_id === commitment_source_node_id

If found: replace {choice} in commit_copy with that entry's choice_label

If not found: render commit_copy_fallback instead (no token replacement)

The resolved text becomes the editable commitment body displayed to the user before they confirm

Commitment creation (functional requirement)

"Commit to this" must POST to /api/commitments with the resolved commitment text as the body. The existing POST wiring from PR #65 must be verified as still functional after module JSON changes.

Test assertion required (AUTOMATED): After clicking "Commit to this", a commitment record exists for the user. This must be verifiable via a unit/integration test mocking the POST — not a live DB call. Assert the POST is called with the correct resolved text.

MANUAL_PLAYTEST_REQUIRED: After merge, verify on sobrietyanchor.com that the commitment appears on Home/Today after clicking "Commit to this" in a practice session.

Repair node routing — implementation spec

Current behavior (confirmed by audit)

5 of 6 modules have dead repair_1 nodes. Only lapse-vs-relapse routes to repair_1 from JSON. The DoesntFitEscape component does not route to any node — it logs an event and exits.

v2 behavior

The "This doesn't fit my situation" escape link must:

Be surfaced after every practice node (not on hook, concept, or synthesis nodes)

When the current module has a repair_1 node: route the session to repair_1 instead of abandoning

When the current module has no repair_1 node: exit normally (current behavior)

Preserve session progress (do not reset choices already made)

Implementation: modify the escape link / DoesntFitEscape component to check whether the current module JSON contains a repair_1 node. If yes, call getNextNode("repair_1") or equivalent state transition rather than triggering abandon. If no, exit as before.

The escape link is shown only on practice and repair node types. Hide on hook, concept, synthesis, outcome.

Library ordering and descriptions — implementation spec

Update PracticeLibrary.tsx:

Sort modules by library_order field (ascending)

Display library_description as a subtitle or secondary text on each module card

If library_order is missing from a module, sort to end

Module library_order values:

halt-check: 1

twenty-minute-urge: 2

ask-for-help: 3

dont-go-back: 4

holding-a-no: 5

declining-the-offer: 6

what-to-do-after-slip: 7

lapse-vs-relapse: 8

Acceptance Criteria

AUTOMATED

All 8 module JSON files parse as valid JSON

All 8 modules load via GET /api/practice/modules (no 503)

Module G and H appear in the modules list

Library order matches spec (halt-check first, lapse-vs-relapse last)

library_description appears on each library card

No module tiny_actions array contains { "key": "open_sos" }

{choice} token replacement uses the choice_label from commitment_source_node_id node, not last choice

{choice} fallback renders commit_copy_fallback when no matching source node choice is found

POST /api/commitments is called when "Commit to this" is selected (assert via mock)

repair_1 node is routable after practice nodes (assert state machine routes correctly)

repair_1 is not shown on hook, concept, or synthesis nodes

Module E title is "After Something Happened" (not "Lapse vs Relapse")

Typecheck clean. Build passes.

HUMAN_REVIEW (MANUAL_PLAYTEST_REQUIRED — do not block phase gates)

All 8 modules load and advance correctly in the app

{choice} personalization renders correctly in a real session

Commitment created from "Commit to this" appears on Home/Today

Repair node is reachable via "This doesn't fit" escape during a practice session

Library card descriptions display and module order is correct

Production smoke on sobrietyanchor.com

COUNCIL_REVIEW_REQUIRED — do not merge without

Modules E, F, G, H. Council prompt in BUILD_REPORT. See Council prompt section below.

Phase Plan

Phase A — Spec-reality reconciliation

PRE-FLIGHT: git status clean. pnpm install --frozen-lockfile. Cut branch: feat/practice-mode-v2. Create docs/run-notes/session-YYYY-MM-DD-practice-v2-plan.md, AUTONOMOUS_RUN_LOG.md, BLOCKERS_FOR_MARCUS.md.

SPEC-REALITY RECONCILIATION (required, section 1.13):

Read and log:

Exact path of module JSON files in repo (likely artifacts/api-server/data/modules/ — confirm)

How modules are loaded in the backend route (readdir + JSON.parse pattern or similar)

How frontend CompletionScreen.tsx reads module outcome data (prop, context, or API response)

How session choices are stored in frontend state during a practice session

CompletionScreen.tsx: current commit_copy render logic and POST /api/commitments call site

PracticeLibrary.tsx: current module card render pattern

Practice.tsx or equivalent: where DoesntFitEscape is invoked and what it currently does

Test runner (Vitest vs node:test), test directory, import/mock patterns from a peer test file

Log all SPEC_REALITY_DELTA entries to AUTONOMOUS_RUN_LOG.md. Adopt repo reality.

SMOKE ASSERTIONS WRITTEN FIRST: assert all 6 existing module JSON files are parseable and contain expected top-level keys (slug, version, nodes, outcome). Run.

IMPLEMENTATION: reconciliation only.

COMMIT:

chore(practice-v2): Phase A spec-reality reconciliation

Phase: A

Deferrals: 0

Tests: N passing, 0 skipped, 0 failing

Phase B — Module JSON updates

PRE-FLIGHT: Phase A commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

All 8 module JSON files parse without error

Each module has library_description (string) and library_order (integer)

No module tiny_actions contains key "open_sos"

halt-check.json exists with library_order 1

dont-go-back.json exists with library_order 4

Module E title is "After Something Happened"

Module A version is "1.1.0"

Module G version is "1.0.0"

commitment_source_node_id present in outcome for modules A, F, G, H

commit_copy_fallback present in outcome for modules A, F, G, H

Run all. Expect red. Implement.

IMPLEMENTATION:

Write the verbatim JSON content from this directive into each module file. Do not modify any field not specified. Do not invent content.

Modules being rewritten in place: A (twenty-minute-urge.json), B (holding-a-no.json), D (declining-the-offer.json), E (lapse-vs-relapse.json), F (what-to-do-after-slip.json).

Modules being updated minimally: C (ask-for-help.json) — remove open_sos from tiny_actions, add library_description and library_order, bump version to 1.0.1.

New files: G (halt-check.json), H (dont-go-back.json).

HEALTH CHECK: All assertions pass. Verify modules load via GET /api/practice/modules (run backend, curl or mock request). Typecheck clean. Build passes.

COMMIT:

feat(practice-v2): Phase B — module JSON rewrites, new modules G and H

Phase: B

Deferrals: N

Tests: P passing, S skipped, F failing

Phase C — Commitment text personalization

PRE-FLIGHT: Phase B commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

{choice} is replaced with choice_label from the node matching commitment_source_node_id

When commitment_source_node_id is "practice_3" and user chose "move my body" at practice_3, commit_copy renders "For the next 20 minutes, I will move my body before acting on the urge."

When no choice logged for commitment_source_node_id, commit_copy_fallback renders instead

commit_copy_fallback contains no {choice} token

POST /api/commitments is called when "Commit to this" is selected (assert via mock)

POST body contains the resolved commit text (personalized or fallback)

Run all. Expect red. Implement.

IMPLEMENTATION:

Modify CompletionScreen.tsx per commitment personalization spec above. Read session choices from local state (confirm shape in Phase A reconciliation). Find entry matching commitment_source_node_id. Replace {choice} or fall back. Pass resolved text to existing POST call.

Do not change the POST endpoint, auth, or error handling — only the text being submitted.

HEALTH CHECK: All assertions pass. Typecheck clean. Build passes.

COMMIT:

feat(practice-v2): Phase C — commitment text personalization via commitment_source_node_id

Phase: C

Deferrals: N

Tests: P passing, S skipped, F failing

Phase D — Repair node routing

PRE-FLIGHT: Phase C commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

After a practice node, the "This doesn't fit my situation" escape routes to repair_1 when repair_1 exists in the module

After a practice node in a module with no repair_1, the escape exits normally

The escape link is visible on practice nodes

The escape link is not visible on hook, concept, or synthesis nodes

Session choices made before triggering the escape are preserved (not reset)

repair_1 node renders its copy and choices correctly after routing

Run all. Expect red. Implement.

IMPLEMENTATION:

Modify DoesntFitEscape and/or Practice.tsx per repair routing spec above. Check module JSON for repair_1 node existence. Route to repair_1 if present, exit otherwise. Show escape only on practice and repair node types.

HEALTH CHECK: All assertions pass. Typecheck clean. Build passes.

COMMIT:

feat(practice-v2): Phase D — repair node routing via doesnt-fit escape

Phase: D

Deferrals: N

Tests: P passing, S skipped, F failing

Phase E — Library ordering and descriptions

PRE-FLIGHT: Phase D commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

Modules render in library_order order (halt-check first, lapse-vs-relapse last)

Each library card displays library_description text

Modules missing library_order sort to end (not crash)

Run. Expect red. Implement.

IMPLEMENTATION:

Update PracticeLibrary.tsx to sort by library_order and display library_description per card per spec above.

HEALTH CHECK: Assertions pass. Typecheck clean. Build passes.

MANUAL_PLAYTEST_REQUIRED (log, do not block):

Library card order and descriptions look correct on sobrietyanchor.com

COMMIT:

feat(practice-v2): Phase E — library ordering and module descriptions

Phase: E

Deferrals: N

Tests: P passing, S skipped, F failing

Phase F — BUILD_REPORT + PR

PRE-FLIGHT: All prior phase commits exist. Full test suite passes. Build passes.

Run full test suite for all affected workspaces. Record counts.

Generate BUILD_REPORT.md per AUTONOMY_LAYER.md section 5. Include:

SPEC_REALITY_DELTA entries from AUTONOMOUS_RUN_LOG.md

MANUAL_PLAYTEST_REQUIRED items

COUNCIL_REVIEW_REQUIRED block with verbatim Council prompt below

Note: no migrations, no Fly secrets, no Vercel env changes required

Note: commitment round-trip (POST → Home display) is MANUAL_PLAYTEST_REQUIRED, not automated

COMMIT:

docs(practice-v2): BUILD_REPORT and working files

Phase: F

Deferrals: N

Tests: P passing, S skipped, F failing

Council review: required before merge

Open PR:

gh pr create --title "feat(practice-v2): Practice Mode V2 — new modules, repair routing, commitment personalization" --body "$(cat BUILD_REPORT.md)"

Log PR URL. Stop. Do not merge. Council review required for Modules E, F, G, H.

Council Review Prompt

Include verbatim in BUILD_REPORT.md under "Council Review Required." Marcus runs this across Claude, GPT, Gemini, and Grok before merging.

You are reviewing Practice Mode V2 content for Anchor, a sobriety support app.

Four modules require Council review before this PR merges. Review each for safety and appropriate framing — not technical implementation.

MODULES UNDER REVIEW:

E — "After Something Happened" (slug: lapse-vs-relapse): post-event processing, accountability without shame F — "What to Do After a Slip": immediate post-slip containment and response G — "HALT Check": hunger, anger, loneliness, tiredness as recovery conditions H — "Don't Go Back": managing the pull to re-contact an ex, source, or unsafe person

REVIEW CRITERIA FOR ALL FOUR MODULES:

Does any copy make definitive pattern claims or predictive statements about user behavior? If so, what specific language should change?

Is there any shaming or failure framing? Any language that implies the user should have done something differently, or that past work is erased?

Is contraindication routing safe and complete? Does every module that could apply during an active crisis correctly route to SOS or relapse response before entering the practice?

Is repair node copy non-judgmental? Does it offer genuine next options rather than implying the user failed at the practice?

Are completion tiny actions appropriate for a post-practice state? No crisis-coded options (SOS has been removed from tiny actions — confirm this is reflected in the content you are reviewing).

ADDITIONAL CHECK FOR MODULE H (Don't Go Back) ONLY:

For the choice "A dealer or source" — does the module handle this safely? The practice routes this to the same flow as an ex or conflict person. Given that re-contacting a dealer/source is higher-stakes than re-contacting an ex, is the content appropriate, or does this choice need a different response path or a stronger contraindication?

RESPONSE FORMAT:

For each module (E, F, G, H):

APPROVED: no changes needed

APPROVED WITH NOTES: minor suggested changes (list them)

NEEDS REVISION: specific issues that must be resolved before merge (list them with suggested copy)

GO

Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3. Credentials preflight scope: gh only. Cut branch from main: feat/practice-mode-v2. Create docs/run-notes/session-YYYY-MM-DD-practice-v2-plan.md and AUTONOMOUS_RUN_LOG.md at repo root. Create BLOCKERS_FOR_MARCUS.md at repo root. Begin spec-reality reconciliation.
