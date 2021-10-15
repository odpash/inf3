import requests
import bs4
import random


def parseCytates():
    cytatesList = []
    h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    r = bs4.BeautifulSoup(requests.get('https://ain.ua/2016/05/28/48-shutok-i-citat-programmistov-o-programmirovanii/', headers=h).text, features='html.parser')
    [cytatesList.append(i.text) for i in r.find('ol').find_all('li')]
    return cytatesList
        

def generateErrors(cytates):
    ans = []
    for c in cytates:
        newCytate = []
        c = c.split()
        for i in c:
            if random.randint(0, 1) == 1:
                newCytate.append(i.replace(':', '').replace(';', '').replace(',', '').replace('.', '').replace('!', '').replace('?', ''))
            newCytate.append(i)
        ans.append(' '.join(newCytate))
    return ans


def findAndDestroy(cytate):
    pass



def main():
    cytates = parseCytates()
    cytatesWithErrors = generateErrors(cytates)
    findAndDestroy(cytatesWithErrors[0])


main()
