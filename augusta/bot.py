"""
The body of AugustaBot

This file stores the necessary information about the Bot as well as the user. This class works directly with the Python
Slack Client API.

~~ This file was made referencing the PythOnboarding bot tutorial ~~
"""
import os
from slackclient import SlackClient

from message import Message, manager


authed_teams = {}

class Bot(object):
    def __init__(self):
        """
        Initiates the bot object
        """
        super(Bot, self).__init__()
        self.name = "augustaalpha"
        self.oauth = {"client_id" : os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      "verification_token": os.environ.get("VERIFICATION_TOKEN"),
                      "scope": "bot"}
        self.client = SlackClient("")   # this is a valid token until we can get the temp token from slack
        self.messages = {}              # messages that have been sent so far

    def auth(self, code):
        """
        Authenticate with OAuth and assign correct scopes.
        Save a dictionary of authed team information in memory on the bot
        object.

        :param code: temporary authorization code sent by Slack to be exchanged for an OAuth token
        """
        # Method implementation borrowed from PythOnboarding

        # After the user has authorized this app for use in their Slack team,
        # Slack returns a temporary authorization code that we'll exchange for
        # an OAuth token using the oauth.access endpoint
        auth_response = self.client.api_call(
                                "oauth.access",
                                client_id=self.oauth["client_id"],
                                client_secret=self.oauth["client_secret"],
                                code=code)
        # To keep track of authorized teams and their associated OAuth tokens,
        # we will save the team ID and bot tokens to the global
        # authed_teams object
        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                 auth_response["bot"]["bot_access_token"]}
        # Then we'll reconnect to the Slack Client with the correct team's
        # bot token
        print("Restarting Client")
        self.client = SlackClient(authed_teams[team_id]["bot_token"])

    def slide_into_dm(self, user_id):
        """
        Opens a direct message channel to a user
        :param user_id: the user that we want to slide into the DM's of
        :return: the channel ID of the user's DM
        """
        user_dm = self.client.api_call("im.open", user=user_id)

        return user_dm["channel"]["id"]

    def send_message(self, team_id, user_id, text ="", is_dm = False):
        """
        Creates a new message from whatever the text is and send it to the correct channel

        :param team_id: the channel for the message
        :param user_id: the user that invoked Augusta
        :param text:    the text to be parsed
        :param is_dm:   whether it is a direct message
        """
        team_id = self.slide_into_dm(user_id) if is_dm else team_id

        msg = self.parse_message(message=text, team_id=team_id, user_id=user_id)

        posted_message = self.client.api_call("chat.postMessage",
                                              channel=msg.channel,
                                              username=self.name,
                                              text=msg.text)
        if posted_message["ok"]:
            time_stamp = posted_message["ts"]
            msg.ts = time_stamp
        else:
            print("Message Sending Unsuccessful")
            print("Error: {error}".format(error=posted_message["error"]))

    def parse_message(self, message, team_id, user_id):
        """
        Parses the message and filters out commands and arguments

        :param message: the message to be parsed
        :param team_id: the channel
        :param user_id: the user_id
        :return: A message object with the command output
        """
        if self.messages.get(team_id):
            self.messages[team_id].update({user_id : Message(channel=team_id)})
        else:
            self.messages[team_id] = {user_id : Message(channel=team_id)}

        message_obj = self.messages[team_id][user_id]

        command = [cmd for cmd in manager.commands if cmd in message]
        if len(command) > 1 and "help" not in command:
            message_obj.text = message_obj.make_message('error')
        elif len(command) == 2 and "help" in command:
            message_obj.text = message_obj.make_message('help', command[1])

        print("Trying to parse command: {}".format(command))

        args_text = message[message.index('[') + 1:message.index(']')] if '[' in message and ']' in message else ''

        message_obj.text = message_obj.make_message(command.pop(), *args_text.split(' '), user_id)

        return message_obj

    def echo_dm(self, user_id, message=""):
        team_id = self.slide_into_dm(user_id)

        self.echo_message(team_id, user_id, message)

    def echo_message(self, team_id, user_id, message =""):
        message_obj = self.parse_message(message, team_id, user_id)
        posted_message = self.client.api_call("chat.postMessage",
                                              channel=message_obj.channel,
                                              username=self.name,
                                              text=message_obj.text)
        if posted_message["ok"]:
            time_stamp = posted_message["ts"]
            message_obj.ts = time_stamp
        else:
            print("Message Sending Unsuccessful")
            print("Error: {error}".format(error=posted_message["error"]))