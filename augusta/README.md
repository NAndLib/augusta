# AugustaBot, Slack Teaching Assistant Assistant
## Introduction 
AugustaBot is a slack bot that helps oversee a Slack channel made for
communication between TAs and students of a class. Specifically, Augusta
provide help with managing student, class, assignments, and helpful other
helpful information.

Augusta allows students to ask for general information when the TA is
unavailable to provide assistance.

## Instructions
### Installation:
To install Augusta, click the button below and select which channel to let Augusta talk on.

<a href="https://slack.com/oauth/authorize?scope=incoming-webhook,commands,bot&client_id=373725849472.409848327092"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>

### Usage: 
Commands can be issued to AugustaBot by doing `@AugustaBot <command>`. 

The commands that be used with AugustaBot are:

All arguments must be wrapped in `[]` blocks.

|**Command**|**Description**|
|:-|:-|
|help|Prints out a message with commands|
|add [Last, First]|Links the user's full name to their Slack ID, if the user is a student, then the name MUST match the one in the school's database.|
|addSID [SID]|Same as `add` but using the Student's Identification number. Only works when the command is issued in a direct message channel.|
|deadline|Displays the nearest assignment deadline.|
|grades|Reports the Student's grades through the direct message channel.|
|GPA|Displays the Student's current GPA for the class. Also shows which assignments are not being considered.|
|exams [Location|Time]|Displays upcoming exams/quizzes information. If `Location` or `Time` is provided, then only display that information.|
