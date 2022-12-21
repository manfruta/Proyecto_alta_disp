import requests
from bs4 import BeautifulSoup


url1 = "https://www.google.com/search?q=valor+del+dolar"
response1 = requests.get(url1)
html1 = response1.text

url2 = "https://www.google.com/search?q=temperatura+actual+en+santiago&oq=temperatura+actual+en+santiago&aqs=chrome..69i57j0i512l9.8040j1j7&sourceid=chrome&ie=UTF-8"
response2 = requests.get(url2)
html2 = response2.text

url3 = "https://www.google.com/search?q=valor+uf+actual+chile&sxsrf=ALiCzsYK-ThcBg5CajEfG2mcTu4k35forA%3A1671564081377&ei=MQuiY9LTFsrX5OUP4Ne0oA4&ved=0ahUKEwiSsKi69Yj8AhXKK7kGHeArDeQQ4dUDCBA&uact=5&oq=valor+uf+actual+chile&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQRhCCAjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoECCMQJzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOgQIABBDOgQILhAnOgoIABCxAxCDARBDOgcIABCxAxBDOgoIABCABBCHAhAUOggIABCxAxCDAToFCAAQgAQ6DQgAEIAEELEDEEYQggI6CwgAEIAEELEDEMkDSgQIQRgASgQIRhgAUABYzRpgrhtoAHABeACAAWiIAYUJkgEEMjAuMZgBAKABAcABAQ&sclient=gws-wiz-serp"
response3 = requests.get(url3)
html3 = response3.text


soup1 = BeautifulSoup(html1, "html.parser")
results1 = soup1.find_all("div", class_="BNeawe iBp4i AP7Wnd")

soup2 = BeautifulSoup(html2, "html.parser")
results2 = soup2.find_all("div", class_="BNeawe iBp4i AP7Wnd")

soup3 = BeautifulSoup(html3, "html.parser")
results3 = soup3.find_all("div", class_="BNeawe iBp4i AP7Wnd")
a = 0

results = results1 + results2 + results3

for result in results:
    if a%2==0:
        print(result.text)
    a=a+1
    