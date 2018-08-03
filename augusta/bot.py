"""
The body of AugustaBot

This file stores the necessary information about the Bot as well as the user. This class works directly with the Python
Slack Client API.
"""
import os
from slackclient import SlackClient

import message
import manager