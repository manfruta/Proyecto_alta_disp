from credentials import database_auth
import requests, re, time, datetime
from bs4 import BeautifulSoup


number_pattern = "^\\d+$"
re.match(number_pattern, "42")
re.match(number_pattern, "notanumber")
number_extract_pattern = "\\d+"


def weather():
    link = "https://www.meteored.cl/tiempo-en_Santiago+de+Chile-America+Sur-Chile-Region+Metropolitana+de+Santiago-SCEL-1-18578.html"
    html = requests.get(link).content
    
    #getting rough data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('span', attrs={'class': 'dato-temperatura changeUnitT'}).text
    temp = re.findall(number_extract_pattern, temp)[0]
    epoch_time = float(int(time.time()))
    #INsert into DB
    #insert into weather (temp) values (temp)
    cur.execute("INSERT INTO weather (temp) VALUES ('"+str(temp)+"')" )
    conn.commit()

    return print("Temp: " + temp) 



def cash():
    #ULS for cash
    link = "https://www.google.com/search?q="+"dolar clp"
    #Getting data
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    dolar_arr = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    aux = dolar_arr.split(' ')
    dolar = aux[0]
    #Insert into DB
    cur.execute("INSERT INTO cash (dolar) VALUES ('"+str(dolar)+"')")
    conn.commit()
    #Confirmation
    #print("Dolar: " + dolar )
    return print("Dolar: " + dolar) 


def uf():
    #ULS for cash
    link = 'https://www.google.com/search?q=%22+'+'%'+'22uf'+'%'+'20clp'
    #Getting data
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    dolar_arr = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    aux = dolar_arr.split(' ')
    uf = aux[0]
    #Insert into DB
    cur.execute("INSERT INTO uf (uf) VALUES ('"+str(uf)+"')")
    conn.commit()
    #Confirmation
    #print("Dolar: " + dolar )
    return print("Uf: " + uf) 

def url():
    return 'https://www.sudoku-online.org/'

if __name__ == '__main__':
    conn = database_auth.get_db()
    cur = conn.cursor()
    weather()
    cash()
    uf()
    print(url())
    print('EL CRONJOB ESTÁ FUNCIONANDO')