#### Week 1 Progress [August 1st - August 8th]
### TODO's:
## Augusta:
- [x] Get repository up and running.
- [x] Sketch architecture and design for AugustaBot.
    - [x] Make VirtualEnv.
    - [x] Read documentations and tutorials.
    - [x] Specify functionality.
    - [x] Architecture.
        - [x] app.py: Calls upon bot.py
            - Manages the Flask microframework for Augusta.
            - Listens to events and processes them: parsing, event type, user
            information, etc.
            - Handles parsed events to the bot.
        - [x] bot.py:
            - Bot object:
                - Bot name: Name of the bot
                - Client: The actual SlackClient Event API
                - Authorized teams: List of teams/workspaces that authorized the
                bot
            - Stores information necessary for OAuth.
                - Client ID.
                - Client secret.
                - Verification token.
            - Handles opening and switching between channels.
            - Handles updating messages and statuses.
            - Handles storing information about channels and users.
        - [x] message.py:
            - Message object:
                - Channel: the channel the message is currently in.
                - Time stamp: the time the message was sent.
                - Text: actual message text.
                - Attachments:
                    - Attachments are often JSON objects that can be premade.
                    - Emoji attachment: any emojis.
                    - Pin attachment: pinned message.
                    - Share attachment: shared message.
            - Handles crafting more complicated message and keeping track of
            which message belongs to who.
        - [x] manager.py: BIG ONE might have to split into smaller sub-files
            - Manager object:
                - All fields are loaded files.
                - Student IDs.
                - Student grades.
                - Class Schedule.
            - Handles mapping UserID from slack to student's names stored in
            file.
            - Handles converting grades into DM attachments for students.
            - Handles scheduling and useful information such as locations and
            deadlines.

## Teaching Assistance:
- [ ] Read 3 sections of the TA manual:
    - [ ] Getting started.
    - [ ] General responsibilities.
    - [ ] Assignments.
- [ ] Take a look at past assignments.

## Employment:
- [x] Rewrite "Experience" section for Resume.
    - [x] Reformatted the entire resume
- [ ] Finish "Contacts" section for webpage.
- [ ] Finish at least 4 `medium` coding problems.

## Cozy:
- [ ] Read: "[Dimensions in Program Synthesis](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/ppdp10-synthesis.pdf)".
- **NEW**: Redesigned nightly run. Ran `lazy_filter` and `swapping_foldsum` for
8 hours on micro benchmarks.
    - No changes. However, `lazy_filter` needs at least 5 hours to find the
        `exist` solution.
