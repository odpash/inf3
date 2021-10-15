import random
import json
import re
import os
import shutil
from colorama import init
from termcolor import colored
import AdditionalTaskOne
import AdditionalTaskTwo
import taskMain

init()  # init colorful output
# Globals
lab3globals = json.loads(open('lab3Globals.json', mode='r', encoding='UTF-8').read())
eyes = lab3globals['eyes']
noses = lab3globals['noses']
mouthes = lab3globals['mouthes']
messages = lab3globals['messages']
isu_number = lab3globals['isu_number']
directoryName = lab3globals['directoryName']
path = os.getcwd()
# delete directories at start


def resetToZero():
    if os.path.exists(path + f'/{directoryName}'):
        shutil.rmtree(path + f'/{directoryName}')




# Start function
def main():
    resetToZero()
    while True:
        print(colored(messages['ok']['modeGet'], 'cyan'), end='')
        mode = input()
        if mode.isdigit() and int(mode) in (1, 2, 3):
            mode = int(mode)
            break
        else:
            print(colored(messages['error']['input'], 'red'))

    if mode == 1:
        taskMain.main(eyes, isu_number, mouthes, messages, path, directoryName, noses)
    elif mode == 2:
        AdditionalTaskOne.main(messages)
    elif mode == 3:
        AdditionalTaskTwo.main()


if __name__ == "__main__":
    main()
