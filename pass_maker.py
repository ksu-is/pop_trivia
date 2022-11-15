import random

print('Welcome to your Password Generator')

reg_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXXYZ'
spec_chars = '~`!@#$%^&*+=:;?'
num_chars = '0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

s_number = input('Amount of special characters: ')
s_number = int(s_number)

n_number = input('Amount of numbers: ')
n_number = int(n_number)

length = input('Input desired password length: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
