from googlesearch import search
#dorks = ['index of /wp-admin.zip','intitle:"index of "cloud-config.yml"','intitle:"index of" "catalina.out"']
dorks = []


def searchDorks():
  for dork in dorks:
    print(f'For {dork}:')
    print('-------------------------------------')
    for resultado in search(dork+' site:"chromadek.co.zw"', stop=5):
    #for resultado in search(dork+' site:"chromssaadek.co.zw"'):
      print(resultado)
    print('\n')

def getListInFile():
  with open("dorks.db") as file:
    data = file.readlines()
    for dork in data:
      dorks.append(dork[:-1]) #removing the break line of string
    #print(dorks)