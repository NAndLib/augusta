"""
Primary file that handles message creation and information

~~ This file was made referencing the PythOnboarding bot tutorial ~~
"""

import yaml
from manager import Manager

manager = Manager()

class Message(object):
    """
    A message object that keeps track of information about messages in the group

    """
    def __init__(self, channel, time_stamp = "", text = "", attachments = [], **kwargs):
        """
        Initiates the message object

        :param channel:     the channel the message is currently in
        :param time_stamp:  the message time stamp
        :param text:        the message's text
        :param attachments: the message's attachments
        :param kwargs:      any extra attachments that might be emojis, pins, or shares
        """
        self.channel = channel
        self.text = text
        self.ts = time_stamp
        self.attachments = attachments
        vars = ["emoji_attachments", "pin_attachments", "share_attachments"]
        for var in vars:
            attachment = kwargs.get(var)
            if attachment:
                self.attachments.append(attachment)

    def make_message(self, command, *args):
        """
        Calls the command passed with the necessary arguments

        :param commmand: the command for the manager
        :param kwargs:   any parameters needed
        :return: the message that is going be sent
        """
        if args:
            print("Args: {}".format(args))

        s = "I don't understand what \"{}\" is...".format(command)
        if manager.commands.get(command):
            if command == "addSID":
                # need sid, user_id, is_dm
                if len(args) < 3:
                    s = "You didn't give me enough info for \"addSID\""
                else:
                    success, message = manager.addSID(args[0], args[1], args[2])
                    if not success:
                        s= message
                    else:
                        return "You've been successfully added :smile:"
            if command == "add":
                # need last, first, user_id
                if len(args) < 3:
                    s = "You didn't give me enough info for \"add\""
                else:
                    success, message = manager.add(args[0], args[1], args[2])
                    if not success:
                        s = message
                    else:
                        return "You've been successfully added :smile:"
            if command == "help":
                if args:
                    s = manager.help(args[0])
                else:
                    s = manager.help()
                return self.code_block(s)

        return s + "\nType \'@augusta help\' for a list of things I can do."

    def code_block(self, message):
        """
        Wraps a message in a code block

        :param message: the message to wrap
        :return: a message wrapped in the form
            ```
            message
            ```
        """

        return "```\n{}\n```".format(message)