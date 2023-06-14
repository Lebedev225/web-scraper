# Adafruit.com Restock Alert

The web scraper monitors a selected Adafruit product and sends a text message followed by a phone call when the desired item is back in stock.  
Note: It only took me two days to snag a Raspberry Pi 4 at MSRP 😇

Check out https://rpilocator.com/ for the last restock date

## Installation

Make sure your environment has the following installed:

-   Beautiful Soup
-   Twilio
-   Dotenv

## Usage

**IMPORTANT**  
**Message from Adafruit.com website**  

**Please note! We are now requiring a verified account with two-factor authentication enabled in order to purchase certain high-demand products due to a large number of bot-purchasers making it difficult for Makers and Engineers to order these products.**  

**Please make sure you have a verified Adafruit account and enable two-factor authentication. Finally, you will need to sign out and back in to activate the account verification.** 

- Step 1: Create a Twilio account (Free) at https://www.twilio.com/en-us 
- Step 2: Get a Twilio phone number, verify your own phone number via Twilio ([Docs](https://support.twilio.com/hc/en-us/articles/223180048-How-to-Add-and-Remove-a-Verified-Phone-Number-or-Caller-ID-with-Twilio#h_01GQT9YZMY444KNH3M5AK065GX))
- Step 3: Create an .env file and add your Twilio credentials
- Step 4: Run the script
- Step 5: Paste the target product's URL and press Enter

You should receive a text which will be followed by a call notifying you of the product becoming available.
```python
# Include your Twilio credentials
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

# Customize the robo-call message
        call = client.calls.create(
            twiml=f"<Response><Say>{product_name} is back in Stock on Adafruit, hurry up!</Say></Response>",
            from_=twilio_number,
            to=my_number
        )

# Edit the interval between requests (don't abuse it!)
time.sleep(30)

# Note - Use twilio-test.py to test and troubleshoot Twilio service
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
