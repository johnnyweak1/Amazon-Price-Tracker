import requests
from bs4 import BeautifulSoup
import smtplib
import os

target = 100
my_link = "https://www.amazon.pl/dp/0984358102/"
my_password = os.environ.get('email_password')
my_adress = 'emailsendertest858@gmail.com'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    "Accept-Language": 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
}
data = requests.get(url=my_link, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
price = soup.find(name='span', class_="a-size-medium a-color-price header-price a-text-normal")
price = price.text
price = price.split()
price = price[0].replace(',', '.')
price = float(price)

if price < target:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_adress, password=my_password)
        connection.sendmail(from_addr=my_adress, to_addrs='jskay111@gmail.com', msg=f'Subject: Book sale! \n\n\n {abs(round(target-price, 2))}zl below your target price!')