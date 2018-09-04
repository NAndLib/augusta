"""
Manager that works with files saved in "data" folder and parsing commands.

- Files include:
    - Slack students: files containing map from SlackID -> Full Name/ID
    - Student info: file containing map from Full Name/ID -> academic info.
    - Class schedule: file containing class' schedule for the academic period.
    - Deadlines: file containings deadlines.
"""

import os
import csv

from utility.database import Database

STUDENTS_FILE = "data/students.csv"
USERS_FILE = "data/users.csv"

# Keeps track of the indices of the CSV file
# This is to account for difference formatting of the student.csv file
class Student(enumerate):
    ID      = 0
    NAME    = 1

class Manager(object):
    # All the commands that we will allow for the bot
    def __init__(self):
        self.commands_list = {
            "deadline"                  : "Display the nearest assignment deadline.",
            "grades"                    : "Sends a private message with your current grades for the class.",
            "GPA"                       : "Sends a private message with your current GPA for the class.",
            "add [LAST, FIRST]"         : "Adds you as a student that Augusta recognizes. You must type the same last."
                                          "first name as the one you have on the student page.",
            "addSID [SID]"              : "Only works with direct messages to Augusta. Adds you using your SID instead "
                                          "of name. Use when you get \"Duplicate name\" when trying to add yourself",
            "exams [LOCATION|TIME]"     : "Display exam information. Will only provide the LOCATION or TIME if one of them is "
                                          "asked for.",
            "help [COMMAND]"            : "Display this help block with useful information. If a command is provided then "
                                          "only the information for that command will be displayed.",
            "suggest [FEATURE:DESC]"    : "Suggests a feature that you would like Augusta to have with a brief description of the feature."
        }

        # Parsed dictionary of { command : [args] }
        self.commands = {}
        for key in self.commands_list:
            command, *args = key.split(' ')
            self.commands[command] = args

        self.database = Database()
        if not self.database.connect('data/augusta.db'):
            raise Exception("Connection to database unsuccessful")

    def close_db(self):
        self.database.disconnect()

    def help(self, command = ""):
        """
        Constructs a string that is a list of helpful features

        :param command: specific command for help information
        :return: string that lists helpful commands
        """
        if command:
            if self.commands.get(command):
                s = "Here's some help\n"
                return s + "{}: \n\t\t{}\n".format(command,
                                               self.commands_list["{cmd} {args}".format(
                                                   cmd=command, args=" ".join(self.commands[command]))])
            else:
                return "Command {} not found. Type @augusta help for list of all commands.".format(command)

        s = "You can tell me to do these commands by mentioning me in a channel I'm invited to, or sliding right into" \
            " my DMs with a sentence that contains the command you want.\n"
        s += "Please wrap any arguments you have for the commands in braces [] (e.g @augusta add [Bot, Augusta]).\n"
        for command in self.commands_list:
            s += "{}: \n\t\t{}\n".format(command, self.commands_list[command])
        return s

    def add(self, last, first, user_id):
        """
        Links the users's Slack_ID with their Name. If a student file exists (recommended), then the student's data
        will also be linked the Slack_ID.

        This requires the user to enter their full name correctly. In case of matching names, method will return false

        :param last:    the user's last name
        :param first:   the user's first name
        :param user_id: the Slack user ID
        :return: (True, "Success") iff the user was linked successfully (False, "Reason") otherwise
        """
        if self.database.user_known(user_id):
            return (False, "I ALREADY KNOW YOU, MAN!")

        return self.database.add_user(user_id, first=first, last=last)


    def addSID(self, sid, user_id, is_dm):
        """
        Adds a student by their SID instead of their first and last name. Only works if the command was invoked
        inside a direct message channel.

        :param sid:     the Student's Identification Number
        :param user_id: the Slack user ID
        :return: (True, "Success") iff the user was linked successfully (False, "Reason") otherwise
        """
        if not is_dm:
            return (False, "I can't do that in public :frowning:")

        if self.database.user_known(user_id):
            return (False, "I ALREADY KNOW YOU, MAN!")

        return self.database.add_user(user_id, student_id=sid)

def write_user(user_id, name, sid = None):
    """
    Handles checking the USER_FILE for users and adding them if they don't exist

    :param user_id: the Slack user ID
    :param name:    the user's full name
    :param sid:     the student number
    :return: (True, "Success") iff the user was added successfully. (False, "User already exists.") if the user already
            exists
    """
    # Checking if the user already exists
    if os.path.isfile(USERS_FILE):
        with open(USERS_FILE, 'r', newline='') as u_file:
            user_data = csv.reader(u_file)

            #### Each row should look like this:
            ## ['Slack_ID', 'Name', 'SID']
            for row in user_data:
                if row[0] == user_id:
                    return (False, "User already exists.")

    with open(USERS_FILE, 'a+', newline='') as u_file:
        csv_writer = csv.writer(u_file)

        new_row = [user_id, name, sid if sid else "None"]
        csv_writer.writerow(new_row)

    return (True, "Success")
