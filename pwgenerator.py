import argparse
import random

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w", "--words", type = int, default = 4, help="include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps", type = int, default = 0, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", type = int, default = 0, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", type = int, default = 0, help="insert SYMBOLS random symbols in the password (default=0)")

args = parser.parse_args()

words_num = int(args.words)
caps_num = int(args.caps)
num_num = int(args.numbers)
sym_num = int(args.symbols)

dictionary = open("words.txt", "r")
dictionary_content = dictionary.read()
words = dictionary_content.split()
dictionary.close()

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

password = []

for i in range(words_num):
    random_word = random.choice(words)
    password.append(random_word)

for i in range(caps_num):
    random_word = random.choice(words)
    random_cap = random_word.title()
    password.append(random_cap)

for i in range(num_num):
    random_num = random.choice(numbers)
    password.append(random_num)

for i in range(sym_num):
    random_sym = random.choice(symbols)
    password.append(random_sym)

random.shuffle(password)

final = ''.join(password)
print(final)
    
