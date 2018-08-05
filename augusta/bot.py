"""
The body of AugustaBot

This file stores the necessary information about the Bot as well as the user. This class works directly with the Python
Slack Client API.

~~ This file was made referencing the PythOnboarding bot tutorial ~~
"""
import os
from slackclient import SlackClient

import message
import manager

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

    def send_message(self, team_id, user_id, text = ""):
        if self.messages.get(team_id):
            self.messages[team_id].update({user_id : message.Message(channel=team_id, text=text)})
        else:
            self.messages[team_id] = {user_id : message.Message(channel=team_id, text=text)}

        message_obj = self.messages[team_id][user_id]
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