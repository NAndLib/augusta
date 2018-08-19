#### Week 2 Progress [August 9th - August 16th]
### Last week's accomplishments: [week 1](week1.md)
It seems like last week had a bit too much going on when also paired with my
personal schedule, this week I will tone it down a bit and see how I will fair.
<details><summary><b>Details</b></summary>

## Augusta:
- Repo up and running.
- Augusta **now has an architecture** and she can already receive events from
Slack.
- Foundation for parsing commands.

## Teaching Assistance:
- Completed application.

## Employment:
- Resume has been reformatted and updated.
- Contacts section on website is done. Website now has dark theme.

## Cozy:
- Redesigned nightly run.
- Ran `lazy_filter` and `swapping_foldsum` for 8 hours. _NO_ change. However,
`lazy_filter` requires at least 3-5 hours to reach the same solution as
without the flag.
</details>

### TODO's
## Cozy:
- [x] Finish designing and testing nightly run.
    - [x] Should add a way for it to notify us of performance drops.
    - [x] Add a way for it to mark and report failed runs.
- [x] Run more micro-benchmarks for 8 hours.
    - [x] Email Calvin and ask which one he suspects to change. Because attu can't
    handle too many 8-hour runs.
    - [x] Email support@cs.washington.edu about attu6 being slow.
- [x] Get looking at the real world case studies ASAP. Preferably by Aug 12th.
    - [x] Check Calvin's email on what to do:
        - [x] Fork the repos for Myria and Bullet.
        - [x] Create two branches `cozy-original` and `cozy-synth` on the
        specific commits.
        - [x] The `cozy-synth` branch should have extra `specs` files and
        benchmark files -> Check the `Makefile` in the `original` folder.
- [x] Email Calvin and Mike about progress on Aug 13th.

## Augusta:
- [x] Design a good command parsing algorithm
    - [x] This should make our lives A LOT easier.
    - [x] Parsing commands moved to Bot. Message now just makes the message
    given a command.
        - This makes it so we only have to add a few lines in make_message to
        for every command because the bulk work is done by the manager method.
- [x] Finish `Add` command.
- [x] Manager now able to link `[STUDENT_ID] -> [SLACK_ID]` and vice versa.
    - [x] Design a proper information storage for Augusta.
        - [x] CSV.
        - [ ] MySQL.

## Employment:
- [ ] See what
[this](https://www.cs.washington.edu/academics/ugrad/enrichment/research)
is all about
- [ ] Do _at least_ 3 `medium` coding problems.
- [x] Finish `Home` and `About` pages on website.
    - Website is pretty complete, with the exception of continuing the blurb on
    the `About` page.
- [ ] Look at job descriptions and research companies.

## Teaching Assistance:
- [ ] Read the first page of the manual.
