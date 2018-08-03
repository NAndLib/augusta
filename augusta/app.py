"""
A routing layer for the AugustaBot using the Flask micro-framework and Slack's Event API

This file handles listening to events coming from Slack and works with passing on information to help the Bot get
through OAuth2.
"""

import json
from flask import Flask, request, make_response, render_template

import bot

app = Flask(__name__)
