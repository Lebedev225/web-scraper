# Web Scraper

Web scraper takes any MicroCenter product and sends an email when it becomes available in stock.

## Installation

Make sure your environment has the following installed:

-   Beautiful Soup 4
-   Twilio
-   Dotenv

## Usage

```python
# Change this line with the url of the product you are interested in
url = "https://www.microcenter.com/product/637834/raspberry-pi-4-model-b-4gb-ddr4?rd=1"

# Change the Twilio credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
my_number = os.environ['PERSONAL_NUMBER']

# Customize the text message
        message = client.messages \
            .create(
                body=f"{product_name} is back in Stock in {local_store[0]}, hurry up before it's gone!",
                from_=twilio_number,
                to=my_number
            )
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
