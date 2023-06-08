# --------------------------------------------------------------
# ------USE THIS FILE TO TEST TWILIO SERVICE FUNCTIONALITY------
# --------------------------------------------------------------

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import time
from dotenv import load_dotenv
load_dotenv()

# Set environment variables for your credentials
# Read more at http://twil.io/secure

# Twilio credentials and client set up
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
my_number = os.environ['PERSONAL_NUMBER']

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="The product is back in Stock on Adafruit, hurry up!",
    from_=twilio_number,
    to=my_number
)
print(message.sid)
time.sleep(5)

call = client.calls.create(
    twiml=f"<Response><Say>The product is back in Stock on Adafruit, hurry up!</Say></Response>",
    from_=twilio_number,
    to=my_number
)

print(call.sid)
