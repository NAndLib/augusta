#### Week 4 Progress [August 28 - September 4th]
### Last week's accomplishments: [week 3](week3.md)
Oh boy! Where do I even start? I fell way behind in week 3 for several reasons,
one of which is due to my own incompetence. This week I will primarily focus on
catching up on the things that I missed in week 3. The details will mostly
encompass what I missed, more so than what I had done.

This week, I will unfortunately not have much time to do things because I will
be on vacation. However, I will push to get as much done as possible.
<details><summary><b>Details</b></summary>

## Cozy
- Emailed Calvin about how to proceed for Myria case study.
- Wrote the spec file and now I only have to make several tweaks to it.
- Now I will have to make the submodule and port the scripts over.
- I asked Calvin about how to handle splitting up my work better and got some
really good advice. Will try to do that.

## Augusta
- I have decided to use SQLite for storing the user data. Frankly I don't know
why I thought I could do it with just CSVs alone. I have made many mistakes
as a man.
- Added `addSID` and updated the README for Augusta.
- Need to get started on the testing framework.

## Employment
- I actually haven't even got here.

## Teaching Assistance:
- I only did a little of reading on the manual page.
</details>

### TODO's
## Employment:
- [x] Add the CSE 132 project to website.
- [x] Complete `About` section on website.
    - [x] Write about Relationships.
    - [x] Conclude the page with emphasis on humor.
    - [x] Proof read.

## Cozy:
- [ ] Myria case study:
    - [ ] Copy over `myria-microbenchmarks` source tree.
    - [ ] Copy over `Makefile` rules for Myria.
    - [ ] Doctor the rule for $(GENDIR)/benchmark/DataStructure.java to use
    new Cozy. Make any changes necessary.
    - The structure for the old folder is: `CASESTUDY-effort.sh` and
    `{gen,run}-CASESTUDY.sh`
        - [ ] Convert `gen*.sh` files into `Makefile` rules that synthesizes the
        data structure.
        - [ ] Convert `*effort.sh` files into `Makefile` rules that run the
        benchmarks.
    - [ ] Pipe the `myria-query*.txt` files over to the new module.
    - In terms of the Spec:
        - [ ] Remove handles and just use normal objects.
        - [ ] Remove `rm` and `update*` mutators.
        - [ ] Change `events` to be a `Bag` instead of `List`.

## Augusta:
- [ ] Implement the SQLite database:
    - [ ] Design a database that makes the most sense for what we're trying to
    achieve.
    - [ ] Write Python methods to handle the database:
        - [ ] Connection.
        - [ ] Transactions.
    - [ ] Refactor `add` and `addSID` to use the new database instead of CSVs.

## Teaching Assistance:
- [ ] BOY. THE MANUAL. Another page.
- [ ] _more shuddering_ Eclipse.
