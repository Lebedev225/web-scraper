# Beautiful Soup for scraping
from bs4 import BeautifulSoup
import requests
# Twilio to send text message and a call
from twilio.rest import Client
import os
# .env for Twilio credentials
from dotenv import load_dotenv
# Time for delay
import time

# Loading .env with secrets
load_dotenv()

# Set the interval time
INTERVAL = 30


# Twilio credentials and client set up
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
my_number = os.environ['PERSONAL_NUMBER']

client = Client(account_sid, auth_token)


# Scraping the product name
def get_name(doc):

    # Finding h1 with product name
    name_div = doc.find("h1", {"class": "product-name-large"})

    # Testing whether the h1 is found
    print(name_div)

    # Extracting text from product name h1
    product_name = name_div.text

    # Testing the product name extraction
    print(product_name)

    return product_name


# Checking if the item is available
def item_availability(doc):
    # Looking for the "Add to Cart" button, which is unavailable if item is out of stock
    availability = doc.find(string="Add to Cart")

    # Checking ehther it is found
    print(availability)

    # If the button is found, function return True to signal that the item is available
    if availability:
        return True
    else:
        print("Out of stock")


def send_message(item_availability, get_name):
    # Getting product name from the get_name function
    product_name = get_name(doc)

    # Checking whether item_availability function confirms that the item is in stock
    if item_availability(doc):
        availability_message = "is in Stock!"
        # Text message to be sent
        message = client.messages \
            .create(
                body=f"{product_name} {availability_message} ",
                from_=twilio_number,
                to=my_number
            )
        # Twilio message log
        print(message.sid)

        # Text confirmation
        print("Success")

        # Waiting 5 seconds before calling
        time.sleep(5)

        # Initiating a call with robo voice reading the twiml prompt
        call = client.calls.create(
            twiml=f"<Response><Say>{product_name} is back in Stock on Adafruit, hurry up!</Say></Response>",
            from_=twilio_number,
            to=my_number
        )
        # Twilio call log
        print(call.sid)

        # Call confirmation
        print("Success")

    # Timestamp
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)


# Prompt user for an URL with the target product
URL = input("Paste the URL of the target product from the Adafruit.com website: ")

# Main loop
while True:
    # Parsing the page
    result = requests.get(URL)
    doc = BeautifulSoup(result.text, "html.parser")
    print(result)

    # Calling the main function which calls other to perform all the checks
    send_message(item_availability, get_name)

    # Scraper interval
    time.sleep(INTERVAL)
