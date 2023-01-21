# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def input_import (file_name):
    with open (f'{file_name}.txt', 'r') as file_name:
        for line in file_name:
            input = str(line)
    return input

def RLE_compact(data):
   compacted = ''
   previous_char = ''
   count = 0
   for char in data:
       if char != previous_char:
           if previous_char:
               compacted += str(count) + previous_char
           previous_char = char
           count = 1
       else:
           count += 1
   compacted += str(count) + previous_char
   return compacted

def RLE_restore(data):
    decoded = ''
    number = ''
    for char in data:
        if char.isdigit():
            number += char
        else:
            decoded += int(number)*char
            number = ''
    return decoded


def main():
    input = input_import('input_for_RLEcompact')
    print(input)
    encoded = RLE_compact(input)
    print(encoded)
    with open('output_RLEcompact.txt', 'a') as file:
        file.write(f'{encoded}\n')
    input = input_import('input_for_RLErestore')
    print(input)
    decoded = RLE_restore(input)
    print(decoded)
    with open('output_RLErestore.txt', 'a') as file:
        file.write(f'{decoded}\n')

if __name__ == "__main__":
    main()