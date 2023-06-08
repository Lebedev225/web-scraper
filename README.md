# Web Scraper

Web scraper takes any Adafruit product and sends a text message followed by a call when the target product becomes available in stock.

## Installation

Make sure your environment has the following installed:

<!-- Beautiful Soup for scraping -->

from bs4 import BeautifulSoup
import requests

<!-- Twilio to send text message -->

from twilio.rest import Client
import os

 <!-- .env for Twilio credentials -->

from dotenv import load_dotenv

 <!-- Time for the delay -->

import time

## Usage

```python

# You will be prompted for an URL of the target product
URL = input("Paste the URL of the target product from the Adafruit.com website: ")

# Change the Twilio credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
my_number = os.environ['PERSONAL_NUMBER']

# Customize the text message
        message = client.messages \
            .create(
                body=f"{product_name} {availability_message} ",
                from_=twilio_number,
                to=my_number
            )

# Customize the robo-call
        call = client.calls.create(
            twiml=f"<Response><Say>{product_name} is back in Stock on Adafruit, hurry up!</Say></Response>",
            from_=twilio_number,
            to=my_number
        )

# Edit the interval between requests (don't abuse it!)
time.sleep(300)

# Note - Use twilio-test.py to trst and troubleshoot Twilio service

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
