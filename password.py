
import random
import array

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

COMPLETE_LIST = DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upcase_char = random.choice(UPCASE_CHARACTERS)
rand_locase_char = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

TEMP_PASSWORD = rand_digit+rand_locase_char+rand_upcase_char+rand_symbol

for p in range(8):
    TEMP_PASSWORD = TEMP_PASSWORD+random.choice(COMPLETE_LIST)

    temp_pass_list = array.array('u', TEMP_PASSWORD)
    random.shuffle(temp_pass_list)

password = ""
for p in temp_pass_list:
    password = password+p

print(password)
