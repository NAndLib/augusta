#### Week 3 Progress [August 17th - August 24th]
### Last week's accomplishments: [week 2](week2.md)
Week 2's schedule was a lot more manageable with all the other things that's
been going on. However, I hit a few snags along the way in terms of motivation
and technical issues.
<details><summary><b>Details</b></summary>

## Cozy:
- Forked and cloned the Myria and Bullet repository.
- Resolved all of the dependency issues that was going on with the followup
evaluation.
- Took a look at what the hell is going on, but it's still relatively hard.
- Nightly run should be at a solid state now, everything seems to be running
fine.
- Sent out progress report to Mike, still waiting for his response.

## Augusta:
- Redesigned how command parsing works. The parsing is now done by the Bot
object, while the Message object simply acts as the middle-man to pass the
command to the Manager, and pass the output back to the Bot.
- I have an idea for a way to test the bot without having to port it through to
Slack and testing on there.
- Several commands have been finished: `Add`, `Help`.
- Manager now handles adding users correctly. There is also an easy way to
change the indices of the information based on the format of the CSV file.

## Employment:
- Website now has Contacts, About, and Projects section.
- Adjusted a few colors on website.
- Added most of the projects on to website.

## Teaching Assistance:
- I really need to get on this.
</details>

### TODO's
## Cozy:
- [ ] Primary focus is the followup evaluation
    - [ ] Write Cozy specs for Myria
        - [ ] Figure out which parts needs to be converted to specs. This might
            include reverse engineering the `original` folder.
        - [ ] Write the Spec.
        - [ ] Make the sub-module in Cozy.
        - [ ] Write the necessary Makefile portion.
    - [ ] Write Cozy specs for Bullet
        - [ ] Figure out which parts needs to be converted to specs. This might
            include reverse engineering the `original` folder.
        - [ ] Write the Spec.
        - [ ] Make the sub-module in Cozy.
        - [ ] Write the necessary Makefile portion.
- [ ] Continue running the nightly.
    - [ ] Set up Cron job to do it so we can just forget about it.
- Check out what the hell is going on with the `runtime` evaluation for `list`s.

## Augusta:
- [ ] Add the rest of the commands.
- [ ] Testing framework: Tests things that can reasonably be tested locally.
    - [ ] Add tests for Manager.
    - [ ] Add tests for Message.
    - [ ] Add tests for Bot.
- [ ] Continuous integration:
    - [ ] Travis job for tests once they are up.
    - [ ] Flake.

## Employment:
- [ ] At least **1** `medium` coding challenge. Please.
- [ ] About section on website complete.
- [ ] Project section has CSE 152 project.
- [ ] Job descriptions.

## Teaching Assistance:
- [ ] One page of the manual.
- [ ] Learn Eclipse. _shudders_
