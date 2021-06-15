import numpy as np
import random
import sys


def caesar(text, val):
    encrypted = ''
    for char in text:
        pos = get_char(char, val)
        encrypted += chr(pos)
    print('Caesar Encryption: ' + encrypted)
    print('')
    get_input()


def get_char(char, val):
    pos = (ord(char) + val - 97) % 26 + 97
    return pos


def square(text):
    matrix = ['a', 'b', 'c', 'd', 'e',
              'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y']
    encoded = []
    for char in text:
        # ignore Z
        if char != 'z':
            encoded.append(matrix.index(char))
        else:
            encoded.append('z')
    algo = input('Enter Algo to Use (N for NumPy, F for Fisher Yates): ').strip()
    if algo == 'F':
        fisher_yates(matrix, encoded)
    if algo == 'N':
        shuffle_matrix(matrix, encoded)
    else:
        get_input()


def encrypted_square(shuffled, encoded):
    encrypted = ''
    for i in encoded:
        # ignore Z
        if i != 'z':
            encrypted += shuffled[i]
        if i == 'z':
            encrypted += 'z'
    print('Square Encryption: ' + encrypted)
    print('')
    get_input()


def fisher_yates(matrix, encoded):
    seed = input('Enter Seed: ')
    random.seed(seed)
    shuffled = matrix
    # shuffles an array without using numpy.
    N = 24  # const for len of array
    for i in range(N-1, 0, -1):
        j = random.randint(0, i+1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    shuffle_print(shuffled)
    return encrypted_square(shuffled, encoded)


def shuffle_matrix(matrix, encoded):
    shuffled = np.random.permutation(matrix)
    shuffle_print(shuffled)
    return encrypted_square(shuffled, encoded)


def shuffle_print(shuffled):
    print('')
    print('SHUFFLED SQUARE: ')
    print('---------------------')
    print('| ' + ' | '.join(shuffled[:5]) + ' |')
    print('---------------------')
    print('| ' + ' | '.join(shuffled[5:10]) + ' |')
    print('---------------------')
    print('| ' + ' | '.join(shuffled[10:15]) + ' |')
    print('---------------------')
    print('| ' + ' | '.join(shuffled[15:20]) + ' |')
    print('---------------------')
    print('| ' + ' | '.join(shuffled[20:25]) + ' |')
    print('---------------------')
    print('')
    print('JavaScript Array: ')
    print(shuffled)
    print('')
    return


def get_input():
    choose = input('Enter Cipher Type (C or S or exit): ')
    if choose == 'C':
        text = input('Enter Text to Encrypt: ').lower().strip()
        val = int(input('Enter Number between 0-25: '))
        caesar(text, val)
    if choose == 'S':
        text = input('Enter Text to Encrypt: ').lower().strip()
        square(text)
    if choose == 'exit':
        print('Have a Good Day')
        sys.exit()
    else:
        get_input()


def main():
    get_input()


main()
