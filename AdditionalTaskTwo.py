import re
from termcolor import colored


def main(cytates, messages):
    for i in range(len(cytates)):
        print(colored(messages['ok']['sourceCytate'], 'red'), cytates[i])
        cytates[i] = re.split('\s', cytates[i])
        pattern = re.compile(r'([ауоыиэяюёе])', flags=re.I)
        for j in range(len(cytates[i])):
            regular = set(pattern.findall(cytates[i][j]))
            if len(regular) == 1:
                try:
                    print(colored(re.match('\w+', cytates[i][j]).group(), 'cyan'), '-', colored(messages['ok']['additionalSecondPlus'], 'green'), colored(messages['ok']['additionalSecondFinal'], 'yellow'), regular)
                except:
                    pass
        print('-' * 50)