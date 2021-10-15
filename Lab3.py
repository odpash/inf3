import random
import json
import re
import os
import shutil
from colorama import init
from termcolor import colored
#


init() # init colorful output
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
#

# Generator for mainTask
def generateTests():
    texts = []
    for _ in range(5):
        testData = []
        [testData.append(eyes[str(random.randint(1, len(eyes) - 1))] + noses[str(random.randint(1, len(noses) - 1))] + mouthes[str(random.randint(1, len(mouthes) - 1))]) for _ in range(0, random.randint(30, 1000))]
        texts.append(''.join(testData))
    return texts


# Task #1 (60 points)
def mainTask():
    eye = eyes[str(isu_number % 5)]
    nose = noses[str(isu_number % 4)]
    mouth = mouthes[str(isu_number % 7)]
    smile = eye + nose + mouth
    print(colored(messages['ok']['smileInfo'] + ' ' + colored(smile, 'magenta'), 'green'))
    
    texts = generateTests()
    os.mkdir(path + f'/{directoryName}')
    for i in range(len(texts)):
        answer = len(re.findall(smile, texts[i]))
        with open(f'{path}/{directoryName}/{i + 1}.txt', mode='w', encoding='UTF-8') as f:
            f.write(texts[i])
        f.close()
        print(colored(f'№{i + 1}', 'magenta'), colored(messages['ok']['finalMessageMainTask'], 'cyan'), colored(answer, 'green'))
    
# Task #2 (18 points)
def additionalTaskOne():
    pass


# Task #3 (22 points)
def additionalTaskTwo():
    pass





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
        mainTask()
    elif mode == 2:
        additionalTaskOne()
    elif mode == 3:
        additionalTaskTwo()


if __name__ == "__main__":
    main()
