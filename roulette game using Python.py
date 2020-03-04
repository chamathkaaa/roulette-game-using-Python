#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("Welcome")
print("You have $1000. Good Luck")
begin = 1000.00

while begin >= 0 and begin <= 1000:
    while begin != 0:
        print("---------------------------------------------")

        number = input("On which number you want to bet? ")
        number = int(number)

        while number < 0 or number >= 50:
            print("The Number should be between 0 - 49")
            number = input("On which number you want to bet? ")
            number = int(number)

        money = input("How much you want to bet on this number? ")
        money = float(money)

        while money > 1000 or money > begin:
            print("You dont have enough money")
            money = input("How much you want to bet on this number? ")
            money = float(money)

        while money < 0:
            print("Amount of money cannot be negative")
            money = input("How much you want to bet on this number? ")
            money = float(money)



        randomNo = random.randint(0, 49)

        print("The number output is ", randomNo)

        if number == randomNo:
            begin = begin + (number * 50)
            print("You have won " ,begin)
        elif number != randomNo:
            print("Sorry but you lost, try again")
            begin = begin - money
            print("You now have ",begin," amount of money")
            
            if begin == 0:
                print("You dont have enough money to continue")
                print("The game is now ending")


# In[ ]:




