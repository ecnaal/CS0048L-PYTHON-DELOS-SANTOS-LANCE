import random

print("MENU")
print("1. Play Number Guessing Game")
print("2. Exit")

def rando():
    
    for i in range(1, 100000):
        
        
        rand = int(random.randint(0,100))
        a = int(input("Enter your guess: "))
        
        if a > rand:
            print("Your guess is too high!")
        
        elif a < rand:
            print("Your guess is too low!")
        
        elif a == rand:
            print("Congratulations! You guessed the number in ", i, " attempt(s).")
            break
        
        else:
            print("Out of Range!")
        
        
choice = int(input("Enter choice: "))

if choice == 1:
    rando()
    
if choice == 2:
    exit()
    
