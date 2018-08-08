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

    def parse_command(self, text):
        """
        Parses the message to find the correct command to pass to the manager

        :param text: the text to be parsed
        :return: the result of the command that was parsed
        """
        command = [cmd for cmd in manager.commands if cmd in text]
        if len(command) > 1 and "help" not in command:
            return "Too many commands pls no :cry:"
        elif len(command) > 1 and "help" in command:
            command.remove("help")
            s = ""
            for cmd in command:
                s += manager.help(cmd)
            return self.code_block(s)

        print("Command: {}".format(command))
        if command:
            function = getattr(manager, command.pop(), None)
            args = text[text.index("[") + 1:text.index("]")] if "[" in text and "]" in text else ""

            if function:
                return self.code_block(function(args) if args else function())

        return "I don't understand \"{}\"... Type `help` for a list of commands.".format(text)


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