import requests
import bs4
import random
import re
from termcolor import colored
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
            if i == '—':
                continue
            if random.randint(0, 1) == 1:
                if i[-1] in (':', ';', ',', '.', '!', '?'):
                    newCytate.append(i.replace(':', '', -1).replace(';', '', -1).replace(',', '', -1).replace('.', '', -1).replace('!', '', -1).replace('?', '', -1))
                else:
                    newCytate.append(i)
            newCytate.append(i)
        ans.append(' '.join(newCytate))
    return ans


def findAndDestroy(cytate):
    return re.sub(r'\b([\%\d\w]+)(\s+\1)+\b', r'\1', cytate, flags=re.I)

    


def main(messages):
    cytates = parseCytates()
    cytatesWithErrors = generateErrors(cytates)
    for i in range(len(cytates)):
        print(colored(messages['ok']['cytatesCount'] + ' ' + str(i + 1), 'cyan'))
        print('\n')
        print(colored('- ' + cytatesWithErrors[i], 'red'))
        print('\n')
        print(colored('+ ' + findAndDestroy(cytatesWithErrors[i]), 'green'))
        print('-' * 50)
