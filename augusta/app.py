"""
A routing layer for the AugustaBot using the Flask micro-framework and Slack's Event API

This file handles listening to events coming from Slack and works with passing on information to help the Bot get
through OAuth2.

~~ This file was made referencing the PythOnboarding bot tutorial ~~
"""

import os
import json
from flask import Flask, request, make_response, render_template

import bot

augusta = bot.Bot()
app = Flask(__name__)

def check_bot():
    no = []
    for thing in augusta.oauth:
        if not augusta.oauth[thing]:
            no.append(thing)
    if no:
        for thing in no:
            print("No \'{}\' found.".format(thing))
        print("Exiting Program...")
        os.sys.exit(1)

def _event_handler(event_type : str, slack_event : dict):
    """
    Routes the correct event to the corresponding bot action

    :param event_type:  the event type that will be used to handle events
    :param slack_event: the slack event object that we will use to gather the necessary information
    :return: Response object with 200 - OK or 500 - No Event Handler Error
    """
    print('Event Type: {}'.format(event_type))
    if event_type == "app_mention":
        user_id = slack_event["event"].get("user")
        team_id = slack_event["event"]["channel"]
        event_text = slack_event["event"]["text"]

        if user_id:
            augusta.send_message(team_id, user_id, event_text)
        return make_response("Message Sent", 200,)
    if event_type == "pin_added":
        return make_response("Pin Updated", 200,)
    if event_type == "star_added":
        return make_response("Star Updated", 200,)
    if event_type == "message":
        if slack_event["event"]["channel_type"] == "im":
            user_id = slack_event["event"].get("user")
            team_id = slack_event["event"]["channel"]
            event_text = slack_event["event"]["text"]

            if user_id:
                augusta.send_message(team_id, user_id, event_text, True)
            return make_response("IM Message Sent", 200,)

    return make_response("No Event Handler For {}".format(event_type), 404,)

@app.route("/install", methods=["GET"])
def install():
    """This route renders the installation page with 'Add to Slack' button."""
    # Method implementation borrowed from PythOnboarding

    # Since we've set the client ID and scope on our Bot object, we can change
    # them more easily while we're developing our app.
    client_id = augusta.oauth["client_id"]
    scope = augusta.oauth["scope"]
    # Our template is using the Jinja templating language to dynamically pass
    # our client id and scope
    return render_template("install.html", client_id=client_id, scope=scope)

@app.route("/thanks", methods=["GET", "POST"])
def thanks():
    """
    This route is called by Slack after the user installs our app. It will
    exchange the temporary authorization code Slack sends for an OAuth token
    which we'll save on the bot object to use later.
    To let the user know what's happened it will also render a thank you page.
    """
    # Method implementation borrowed from PythOnboarding

    # Let's grab that temporary authorization code Slack's sent us from
    # the request's parameters.
    code_arg = request.args.get('code')
    # The bot's auth method to handles exchanging the code for an OAuth token
    augusta.auth(code_arg)
    return render_template("thanks.html")

@app.route("/listening", methods=["GET", "POST"])
def listening():
    """
    This route listens for incoming events from Slack and uses the event
    handler helper function to route events to our Bot.
    """
    slack_event = json.loads(request.data.decode('utf-8'))

    # ============= Slack URL Verification ============ #
    # In order to verify the url of our endpoint, Slack will send a challenge
    # token in a request and check for this token in the response our endpoint
    # sends back.
    #       For more info: https://api.slack.com/events/url_verification
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                             "application/json"
                                                             })

    # ============ Slack Token Verification =========== #
    # We can verify the request is coming from Slack by checking that the
    # verification token in the request matches our app's settings
    if augusta.oauth["verification_token"] != slack_event.get("token"):
        message = "Invalid Slack verification token: %s \npyBot has: \
                   %s\n\n" % (slack_event["token"], augusta.oauth["verification_token"])
        # By adding "X-Slack-No-Retry" : 1 to our response headers, we turn off
        # Slack's automatic retries during development.
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    # ====== Process Incoming Events from Slack ======= #
    # If the incoming request is an Event we've subcribed to
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        # Then handle the event by event_type and have your bot respond
        return _event_handler(event_type, slack_event)

    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    check_bot()
    app.run(debug=True, port=2848)