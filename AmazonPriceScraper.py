import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Practical-Malware-Analysis-Hands-Dissecting/dp/1593272901/ref=sr_1_3?keywords=practical+malware&qid=1579485026&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0'}


def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="header_price").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 39.40):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mail@exaple', 'superPassword')
    subject = 'Price Fall down!'
    body = 'Check the amazon link: https://www.amazon.com/Practical-Malware-Analysis-Hands-Dissecting/dp/1593272901/ref=sr_1_3?keywords=practical+malware&qid=1579485026&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
    'mail@exaple',
    'mail@exaple',
    msg
    )
    print("Hey, Email has been sent!")
    server.quit()
while True:
    check_price()
    time.sleep(3600)
