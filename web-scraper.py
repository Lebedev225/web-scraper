# Beautiful Soup for scraping
from bs4 import BeautifulSoup
import requests
# Twilio to send text message
from twilio.rest import Client
import os
# .env for Twilio credentials
from dotenv import load_dotenv
# Time for delay
import time

load_dotenv()

# URL with the scarce product
url = "https://www.microcenter.com/product/637834/raspberry-pi-4-model-b-4gb-ddr4?rd=1"

while True:
    # Parsing the page
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    # Scraping the product name
    name_div = doc.find_all("div", {"class": "product-header"})
    name_instance = name_div[0]
    product_name = name_instance.find("span").string

    # Testing
    print(product_name)

    # Finding our local store from the dropdown menu
    local_store = doc.find_all(string="CA - Tustin ")
    parent = local_store[0].parent

    # Checking our local store's availability of this item and extracting text
    available = parent.find("span").string

    # Testing
    print(available)

    # In case it is in stock, sending a text message with Twilio
    if available == "(in stock)":
        # Twilio credentials and client set up
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        twilio_number = os.environ['TWILIO_NUMBER']
        my_number = os.environ['PERSONAL_NUMBER']

        client = Client(account_sid, auth_token)

        # Text message to be sent
        message = client.messages \
            .create(
                body=f"{product_name} is back in Stock in {local_store[0]}, hurry up before it's gone!",
                from_=twilio_number,
                to=my_number
            )
        # Testing
        print(message.sid)

        # Testing
        print("Success")

    # In case it is out of stock, print error message
    else:
        print("Out of Stock")
    # Scraper interval
    time.sleep(300)
