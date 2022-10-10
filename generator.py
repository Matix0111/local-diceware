import secrets
import argparse
import string
import math

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--rolls', type=int, help='Amount of dice rolls, default is 5')
parser.add_argument('-t', '--title', action='store_true', help='Capitalize first letter of words')
parser.add_argument('-s', '--special', action='store_true', help='Append random symbols between words')
args = parser.parse_args()

SYMBOLS = string.punctuation

if args.rolls is None:
    rolls = 5
else:
    rolls = args.rolls

with open('eff_large_wordlist.txt', 'r') as f:
    lines = {k:v for k, v in [x.strip().split(' ') for x in f.readlines()]}

def roll_die():
    return ''.join([str(secrets.randbelow(6)+1) for _ in range(5)])

def get_pool_size():
    char_pool_size = 26
    if args.title:
        char_pool_size += 26
    if args.special:
        char_pool_size += len(SYMBOLS)

    return char_pool_size

def main():
    password = ""
    char_pool_size = get_pool_size()
    for i in range(rolls):
        chosen_word = lines[roll_die()]
        if args.title:
            chosen_word = chosen_word.title()
        if args.special:
            if i + 1 < rolls:
                chosen_word += ' ' + secrets.choice(SYMBOLS)
            else:
                chosen_word = chosen_word

        password += chosen_word + ' '

    real_password = password.replace(" ", "")

    print(f'Chosen: {password}')
    print(f'Password: {real_password}')
    print(f'Password length: {len(real_password)}')
    print(f'Entropy: {len(real_password) * math.log2(char_pool_size):.2f} bits')

if __name__ == "__main__":
    main()
