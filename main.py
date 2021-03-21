import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


target_price = 2000.0
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


# Product url of your own choice from amazon
product_url = "https://www.amazon.in/Red-Dead-Redemption-2-PS4/dp/B07BFGGNT9/ref=sr_1_1?crid=3HNULJKDP8J1K&dchild=1&keywords=red+dead+redemption+2+ps4+game&qid=1610449678&sprefix=red+dea%2Caps%2C300&sr=8-1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,te;q=0.7"
}
response = requests.get(url=product_url,headers=headers)
product_markup = response.text

soup = BeautifulSoup(product_markup,"lxml")
product_title = soup.find(name="span", id="productTitle").getText().strip()
product_price = float(soup.find(name="span", id="priceblock_ourprice").get_text().replace(',', '').replace('₹','').strip())

print(product_title)
print(product_price)

if product_price < target_price:
    message = f'Subject: Amazon Price Alert!\n\n{product_title} is now ₹{product_price}\n{product_url}'.encode("utf-8")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=message
    )
