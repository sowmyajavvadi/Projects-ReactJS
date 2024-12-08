import requests
import pandas
from bs4 import BeautifulSoup
response= requests.get("https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles")
print(response)
