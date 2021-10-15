import random
import re
from termcolor import colored
import os


# Generator for mainTask
def generateTests(eyes, mouthes, noses):
    texts = []
    for _ in range(5):
        testData = []
        [testData.append(eyes[str(random.randint(1, len(eyes) - 1))] + noses[str(random.randint(1, len(noses) - 1))] +
                         mouthes[str(random.randint(1, len(mouthes) - 1))]) for _ in range(0, random.randint(30, 1000))]
        texts.append(''.join(testData))
    return texts




# Task #1 (60 points)
def main(eyes, isu_number, mouthes, messages, path, directoryName, noses):
    eye = eyes[str(isu_number % 5)]
    nose = noses[str(isu_number % 4)]
    mouth = mouthes[str(isu_number % 7)]
    smile = eye + nose + mouth
    print(colored(messages['ok']['smileInfo'] +
          ' ' + colored(smile, 'magenta'), 'green'))

    texts = generateTests(eyes, mouthes, noses)
    os.mkdir(path + f'/{directoryName}')
    for i in range(len(texts)):
        answer = len(re.findall(smile, texts[i]))
        with open(f'{path}/{directoryName}/{i + 1}.txt', mode='w', encoding='UTF-8') as f:
            f.write(texts[i])
        f.close()
        print(colored(f'№{i + 1}', 'magenta'), colored(
            messages['ok']['finalMessageMainTask'], 'cyan'), colored(answer, 'green'))
