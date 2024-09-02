import random
from getLength import getInput

print('This is a strong password generator')

pwordchars = '!"#$%&*+-0123456789:;()?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

length = input('Please enter the desired password length (minimum recommended length is 12)')
length = getInput(length)
    

print('Here is your password:')

password=''
for i in range(length):
    password+=random.choice(pwordchars)
print(password)

