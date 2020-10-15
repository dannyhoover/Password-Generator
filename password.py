'''
Class 6/19/2020
Danny
password.py
'''

import random
import string




# getting the random characters 
choice1 = random.choice(string.printable)
choice2 = random.choice(string.printable)
choice3 = random.choice(string.printable)
choice4 = random.choice(string.printable)
choice5 = random.choice(string.printable)
choice6 = random.choice(string.printable)
choice7 = random.choice(string.printable)
choice8 = random.choice(string.printable)
choice9 = random.choice(string.printable)
choice10 = random.choice(string.printable)


# creating the list
figures = [choice1]



# adding the items to the list

for figure in figures:
    figures.insert(1, choice2)
    figures.insert(2, choice3)
    figures.insert(3, choice4)
    figures.insert(4, choice5)
    figures.insert(5, choice6)
    figures.insert(6, choice7)
    figures.insert(7, choice8)
    figures.insert(8, choice9)
    figures.insert(9, choice10) 
    break 



# printing the randomly selected characters
print(f'''
The chosen characters are: {figures} 
''')

# showing the user their new password
print(f'''
This means your password is: 
{figures[0]}{figures[1]}{figures[2]}{figures[3]}{figures[4]}{figures[5]}{figures[6]}{figures[7]}{figures[8]}{figures[9]}
''')

