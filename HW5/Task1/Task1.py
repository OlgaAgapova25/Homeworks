# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def delword(text):
    if 'абв' in text.lower():
        text = text.replace(text,'')
    return text

def main():
    text = 'абврол иролирл гшгитолдабв иролри гулвюч'
    text = list(map(delword, text.split()))
    print(' '.join(text))

if __name__ == "__main__":
    main()