import random
import string

characters = string.ascii_letters + string.digits + '@$!?*&%'

password = ''
for i in range(10):
    rand = random.choice(characters)
    password += rand

print('password: ', password)
