# Author: <your name>
import random 
num1 = random.randrange(1, 10)
num2 = random.randrange(1, 10)
num3 = random.randrange(1, 10)

input("Press <enter> key to start") #to pause and wait for user input
print()

print("*****************")
print("**", num1, "**", num2, "**", num3, "**")
print("*****************")

if num1 == num2 == num3:
    print("**", "Jackpot!!", "**")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("**", "2 of a kind", "**")
else: 
    print("**", "Try again!", "**")
