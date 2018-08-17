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

students_file_name = "data/students.csv"
users_file_name = "data/users.csv"

class Manager(object):
    # All the commands that we will allow for the bot
    def __init__(self):
        self.commands_list = {
            "deadline"                  : "Display the nearest assignment deadline.",
            "grades"                    : "Sends a private message with your current grades for the class.",
            "GPA"                       : "Sends a private message with your current GPA for the class.",
            "add LAST, FIRST"           : "Adds you as a student that Augusta recognizes. You must type the same last "
                                          "first name as the one you have on the student page.",
            "addSID [SID]"              : "Only works with direct messages to Augusta. Adds you using your SID instead "
                                          "of name. Use when you get \"Duplicate name\" when trying to add yourself",
            "exams [LOCATION|TIME]"     : "Display exam information. Will only provide the LOCATION or TIME if one of them is "
                                          "asked for.",
            "help [COMMAND]"            : "Display this help block with useful information. If a command is provided then "
                                          "only the information for that command will be displayed.",
        }

        # Parsed dictionary of { command : [args] }
        self.commands = {}
        for key in self.commands_list:
            command, *args = key.split(' ')
            self.commands[command] = args

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
        :return: (True, "Success") iff the user was linked successfully (False, "Reason") otherwise
        """
        # Removing the trailing ','
        name = "{first} {last}".format(last=last[:len(last) - 1], first=first)

        # Getting the SID if a student file exists
        sid = None
        if os.path.isfile(students_file_name):
            found = False
            with open(students_file_name, 'r', newline='') as s_file:
                student_data = csv.reader(s_file)
                for row in student_data:
                    if name == row[1]:
                        if not found:
                            found = True
                            sid = row[0]
                        else:
                            return (False, "Duplicate name: {}".format(name))
            if not found:
                return (False, "No student information found")
        else:
            print("No students file.")

        # Checking if the user already exists
        if os.path.isfile(users_file_name):
            with open(users_file_name, 'r', newline='') as u_file:
                user_data = csv.reader(u_file)

                #### Each row should look like this:
                ## ['Slack_ID', 'Name', 'SID']
                for row in user_data:
                    if row[0] == user_id:
                        return (False, "User already exists.")
        with open(users_file_name, 'a+', newline='') as u_file:
            csv_writer = csv.writer(u_file)

            new_row = [user_id, name, sid if sid else "None"]
            csv_writer.writerow(new_row)

        return (True, "Success")