# PROJECT ON RANDOM PASSWORD GENERATOR

import random
import pyperclip

print("\nWelcome to the PASSWORD GENERATOR\n\n")

print('''CONDITIONS : 
1. There should be minimum 8 characters
2. There should be minimum 1 uppercase alphabet
3. There should be minimum 1 lowercase alphabet
4. There should be minimum 1 numerical value
5. There should be minimum 1 symbol\n''')

character = int(input("No. of characters (Length of password) : "))
uppercase = int(input("No. of uppercase alphabets : "))
numbers = int(input("No. of numerical values : "))
symbols = int(input("No. of symbols : "))

lowercase = character - (uppercase+symbols+numbers)

print(f"No. of lowercase alphabets : {lowercase}")

if(character < 8 or uppercase < 1 or numbers < 1 or symbols < 1 or lowercase < 1):
    print("\nINVALID INPUTS! Please Check Conditions\n")

else :
    password = []

    for i in range(0,uppercase):
        password += chr(random.randint(65,90))
        # password.append(chr(random.randint(65,90)))

    for i in range(0,lowercase):
        password += chr(random.randint(97,122))
        # password.append(chr(random.randint(97,122)))

    for i in range(0,numbers):
        password += chr(random.randint(48,57))
        # password.append(chr(random.randint(48,57)))

    # for i in range(0,numbers):
    #     password += str(random.randint(0,9))

    symbols_list = []

    for i in range(33,48):
        symbols_list += chr(i)
        
    # symbols_list = [chr(i) for i in range(33,48) ]

    for i in range(58,65):
        symbols_list += chr(i)
    for i in range(91,97):
        symbols_list += chr(i)
    for i in range(123,127):
        symbols_list += chr(i)

    for i in range(0,symbols):
        password +=  symbols_list[random.randint(0, len(symbols_list)-1)]

    random.shuffle(password)


    # for i in range(0,len(password)):
    #     password_generated += password[i]

    # for item in password:
    #     password_generated += item

    password_generated = "".join(password)


    pyperclip.copy(password_generated)
    print(f"\nPassword Generated : {password_generated}")
