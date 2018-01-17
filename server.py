""" Twilio SafeReject -- Safely reject their advances!

    SafeReject lets registered users exchange fake contact information with
    persistent would-be suiters, aka Harassers.

    The user sends an SMS to the Twilio number with their credentials, the
    harasser's phone number (and name, if available), and the short place name
    where the exchange took place (eg: 'the bar' or 'BART'). SafeReject updates
    its database with the information and then texts the harasser from a 'fake
    phone number' while impersonating the user. This allows the user time to
    safely get away from the harasser before the genius act of treachery is
    discovered.

    NEW USERS can sign up online ONLY at this time. We need to be able to
    verify real users, and also to have a list of people who can't use the
    service because they have been flagged as a harasser. Online signup
    uses two-step authentication to verify the device.

    REGISTERED USERS can get a new fake phone number or initiate a number
    exchange between a fake phone number and a harasser. We verify users
    by the 'From' and their PIN.

    HARASSERS have been previously texted by a fake phone number via a
    registered user -- eg the user has tried to avoid exchanging contact
    info, but the harasser just doesn't get it and was then passed into the
    system by the registered user. The harasser is now trying to converse
    with the registered user.

    UNKNOWNS are probably would be harassers trying to get the numbers so
    they can "catch" registered users. And also spambots. Jerks.

"""

from flask import Flask, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse, Message, Body


app = Flask(__name__)
app.config.from_object(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "twilio safe reject"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """ Respond to texts from new users, registered users, and harassers. """

    msg_from = request.values.get('From')
    msg_body = request.values.get('Body', None)

    # I'm pretty sure there is an error for empty messages, but I want them
    # to fail silently so as not to alert harassers.
    if not msg_body:
        return

    # Check if from number is in database, as user or harasser






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
    app.debug = True

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
