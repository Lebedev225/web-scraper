from bs4 import BeautifulSoup
import requests

url = "https://www.microcenter.com/product/663023/hp-victus-15-fa0031dx-156-gaming-laptop-computer-silver"


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

available = doc.find_all(string="Available for In-Store Pickup Only.")

if not available:
    print("Not found")
# else:
    # Send Twillio message
