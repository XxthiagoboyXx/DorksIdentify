from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re


def getDorks():
    site = 'https://www.exploit-db.com/ghdb/'
    session = HTMLSession()
    file = open('dorks.db', 'a')

    dork = ''
    count404 = 0
    ghdbNow = getMinGHDB()

    while True:
        try:
            print(ghdbNow)
            r = session.get(site+str(ghdbNow), timeout=3) #walking for the list ->1
            print(r.status_code)
            soup = BeautifulSoup(r.text, 'html.parser')
            dork = str(soup.title)
            dork = re.split(r" - ", dork)
            dork = dork[0][7:]
            if r.status_code == 404 and count404 == 10: #flag to stop 10
                break
            if r.status_code == 404: #flag to pass for the foward ghdb
                count404 += 1
                ghdbNow += 1 #foward ghdb
                continue
            count404 = 0 #reset count
            file.write(dork+"\n")
            print(dork)
            ghdbNow += 1
        except Exception as e:
            print("Erro Encontrado!", e)
            ghdbNow += 1
        finally:
            print("---------------------------------------------------------------------")
            session.close()

    file.write(str(ghdbNow-10)+"\n") #save the next min for a next update
    file.close()

def getMinGHDB():
    try:
        file = open('dorks.db', 'r')
    except FileNotFoundError:
        print('File "dorks.db" not found!')
        exit()

    with open("dorks.db", 'r') as file: #read file to find the last ghdb downloaded
        min = file.readlines()[-1]
        file.seek(0)
        data = file.readlines()
        data.pop()
    with open("dorks.db", 'w') as file: #removing flag ghdb
        file.writelines(data)

    return int(min)