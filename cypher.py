import numpy as np
import random
import sys


def caesar(text, val):
    encrypted_text = []
    for word in text:
        encrypted_word = ''
        for char in word:
            pos = get_char(char, val)
            encrypted_word += chr(pos)
        encrypted_text.append(encrypted_word)
    print('Caesar Encryption: ' + ' '.join(encrypted_text))
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
    encoded_text = []
    for word in text:
        encoded_word = []
        for char in word:
            # ignore letter 'z'
            if char != 'z':
                encoded_word.append(matrix.index(char))
            else:
                encoded_word.append('z')
        encoded_text.append(encoded_word)
    algo = input('Enter Algo to Use (N for NumPy, F for Fisher Yates): ').strip().lower()
    if algo == 'f':
        fisher_yates(matrix, encoded_text)
    if algo == 'n':
        shuffle_matrix(matrix, encoded_text)
    else:
        get_input()


def encrypted_square(shuffled, encoded_text):
    encrypted_text = []
    for word in encoded_text:
        encrypted_word = ''
        for i in word:
            # ignore letter 'z'
            if i != 'z':
                encrypted_word += shuffled[i]
            if i == 'z':
                encrypted_word += 'z'
        encrypted_text.append(encrypted_word)
    print('Square Encryption: ' + ' '.join(encrypted_text))
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
    for i in range(0, len(shuffled), 5):
        print('| ' + ' | '.join(shuffled[i:i+5]) + ' |')
        print('---------------------')
    print('')
    return


def get_input():
    choose = input('Enter Cipher Type (C or S or exit): ').lower()
    if choose == 'c':
        text = input('Enter Text to Encrypt: ').lower().split()
        val = int(input('Enter Number between 0-25: '))
        caesar(text, val)
    if choose == 's':
        text = input('Enter Text to Encrypt: ').lower().split()
        square(text)
    if choose == 'exit':
        print('Have a Good Day')
        sys.exit()
    else:
        get_input()


def main():
    get_input()


main()
