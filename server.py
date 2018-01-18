""" Twilio SafeReject -- Safely reject their advances!

    SafeReject lets registered users exchange fake contact information with
    persistent would-be suiters, aka Harassers.

"""

from flask import Flask, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse, Message, Body


app = Flask(__name__)
app.config.from_object(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "twilio safe reject"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """ Respond to texts from new users, registered users, and harassers. """

    msg_body = request.form.get('Body', None)

    # There is an error for empty messages, but instead we fail silently
    # so as not to alert harassers.
    if not msg_body:
        return

    # Check if from number is in database, as user or harasser
    msg_from = request.form.get('From')
    if is_known_number(msg_from) == "reguser":
        return parse_reguser_msg(msg_from, msg_body)
    if is_known_number(msg_from) == "harasser":
        return





    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("copy that")

    return str(resp)


#########
# Helper Functions
#########

if __name__ == "__main__":
    # import sys

    # app.debug has to be True at the point we invoke the DebugToolbarExtension
    app.debug = False

    # Ensure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # connect to test db if testing
    # if 'test' in sys.argv[-1]:
    #     connect_to_db(app, 'postgres:///twilioTEST')
    # else:
    #     connect_to_db(app, 'postgres:///twilioLIVE')

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # Set server to localhost:5000
    app.run(port=5000, host='0.0.0.0')
