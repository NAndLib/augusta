"""
Manager that works with files saved in "data" folder and parsing commands.

- Files include:
    - Slack students: files containing map from SlackID -> Full Name/ID
    - Student info: file containing map from Full Name/ID -> academic info.
    - Class schedule: file containing class' schedule for the academic period.
    - Deadlines: file containings deadlines.
"""

import os

class Manager(object):
    # All the commands that we will allow for the bot
    def __init__(self):
        self.commands = {
            "deadline"              : "Display the nearest assignment deadline.",
            "grades"                : "Sends a private message with your current grades for the class.",
            "GPA"                   : "Sends a private message with your current GPA for the class.",
            "add LAST, FIRST"       : "Adds NAME as a student that Augusta recognizes.",
            "exams [LOCATION|TIME]" : "Display exam information. Will only provide the LOCATION or TIME if one of them is "
                                      "asked for.",
            "help [COMMAND]"        : "Display this help block with useful information. If a command is provided then "
                                      "only the information for that command will be displayed.",
        }
        self.keywords = [key.split(" ")[0] for key in self.commands.keys()]

    def help(self, command = ""):
        """
        Constructs a string that is a list of helpful features

        :param command: specific command for help information
        :return: string that lists helpful commands
        """
        if command:
            if self.commands.get(command):
                return "{}: \n\t\t{}\n".format(command, self.commands[command])
            else:
                return "Command {} not found. Type @augusta help for list of all commands."

        s = "You can tell me to do these commands by mentioning me in a channel I'm invited to, or sliding right into" \
            "my DMs with a sentence that contains the command you want.\n"
        s += "Please wrap any arguments you have for the commands in braces [] (e.g @augusta add [Bot, Augusta]).\n"
        for command in self.commands:
            s += "{}: \n\t\t{}\n".format(command, self.commands[command])
        return s