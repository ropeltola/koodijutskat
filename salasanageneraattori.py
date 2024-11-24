import random

print("your password:")
characters = "abcdefghijklmnopqrstuvwxyz1234567890!@£{}[]"

password = ""
for x in range(16):
    password += random.choice(characters)

print(password)
