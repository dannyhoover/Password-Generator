import random
import string


figures = []


while True:
    choice = random.choice(string.printable)
    figures.append(choice)
    while True:
        choice = random.choice(string.printable)
        figures.append(choice)
        while True:
            choice = random.choice(string.printable)
            figures.append(choice)
            while True:
                choice = random.choice(string.printable)
                figures.append(choice)
                while True:
                    choice = random.choice(string.printable)
                    figures.append(choice)
                    while True:
                        choice = random.choice(string.printable)
                        figures.append(choice)
                        while True:
                            choice = random.choice(string.printable)
                            figures.append(choice)
                            while True:
                                choice = random.choice(string.printable)
                                figures.append(choice)
                                while True:
                                    choice = random.choice(string.printable)
                                    figures.append(choice)
                                    while True:
                                        choice = random.choice(string.printable)
                                        figures.append(choice)
                                        break
                                    break
                                break
                            break
                        break
                    break
                break  
            break
        break
    break  

print(f"Your password is: {figures}")
