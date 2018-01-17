import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_TEST_SID']  # os.environ['TWILIO_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_TEST_TOK']  # os.environ['TWILIO_TOK']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=os.environ['TWILIO_TEST_MOB'],  # os.environ['TWILIO_MOB'],
    from_=os.environ['TWILIO_TEST_BOT'],  # os.environ['TWILIO_BOT'],
    body="Hello from Python!")

print(message.sid)