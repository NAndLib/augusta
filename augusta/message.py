"""
Primary file that handles message creation and information

~~ This file was made referencing the PythOnboarding bot tutorial ~~
"""

import yaml

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