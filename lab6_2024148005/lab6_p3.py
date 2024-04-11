# Password Encryption/Decryption Program
import numbers
import sys

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a','m'), ('b','h'), ('c','t'), ('d','f'), ('e','g'),
                  ('f','k'), ('g','b'), ('h','p'), ('i','j'), ('j','w'), ('k','e'),('l','r'),
                  ('m','q'), ('n','s'), ('o','l'), ('p','n'), ('q','i'), ('r','u'), ('s','o'),
                  ('t','x'), ('u','z'), ('v','y'), ('w','v'), ('x','d'), ('y','c'), ('z','a'))

# Variable that store lower case of alphabet
lowercase = []
# Create lowercase list using encryption_key variable and for loop
for letter in encryption_key:
    lowercase.append(letter[0])

# Variable that store upper case of alphabet
uppercase = []
# Create uppercase list using encryption_key variable and for loop
for letter in encryption_key:
    uppercase.append(letter[0].capitalize())

encrypting = True

# get password
password_in = input('Enter password: ')

# Check password is valid
has_lowercase = False
has_uppercase = False
has_digit = False
has_special = False

# Check password contains lower case letter, capital letter, non-alphabetic character, and digit
for letter in password_in:
    if letter in lowercase:  # Check password has lower case letter
        has_lowercase = True
    elif letter in uppercase:  # Check password has capital letter
        has_uppercase = True
    elif letter.isnumeric():  # Check password has digit
        has_digit = True
    elif letter in ("#", "@", "%"):  # Check password has non-alphabetic character
        has_special = True

# If password is not valid, exit program
if not (has_lowercase and has_uppercase and has_digit and has_special):
    print('Invalid password!')
    sys.exit()

# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1
    to_index = 0

case_changer = ord('a') - ord('A')

for ch in password_in:
    letter_found = False

    for t in encryption_key:
        if ('a' <= ch and ch <= 'z') and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif ('A' <= ch and ch <= 'Z') and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True

    # Encrypt non-alphabetic characters
    if ch == "#":
        password_out = password_out + "!"
        letter_found = True
    elif ch == "@":
        password_out = password_out + "("
        letter_found = True
    elif ch == "%":
        password_out = password_out + ")"
        letter_found = True

    if not letter_found:
        password_out = password_out + ch

# output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)

