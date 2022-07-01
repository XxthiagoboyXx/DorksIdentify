from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

def getDorks():
    site = 'https://www.exploit-db.com/ghdb/'
    session = HTMLSession()
    file = open('dorks.txt', 'w')


    for ghdbNow in range(7955,7960):
        try:
            r = session.get(site+str(ghdbNow)) #walking for the list
            soup = BeautifulSoup(r.text, 'html.parser')
            dork = str(soup.title)
            dork = re.split(r" - ", dork)
            dork = dork[0][7:]
                #dork = str(soup.title).split("-")[0]
                #dork = dork[7:]
            file.write(dork+"\n")
            print(dork)
        except Exception as e:
            print("Erro Encontrado!", e)
            #continue | pass
        finally:
            print("---------------------------------------------------------------------")

    file.close()