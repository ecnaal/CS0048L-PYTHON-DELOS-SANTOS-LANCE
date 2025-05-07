print("MENU")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
print("5. Exit")

def add(a,b):
    return a+b
    
def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    return a/b

while True:
    choice = int(input("Enter your choice: "))
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == 1:
        print(add(x,y))
    
    elif choice == 2:
        print(subtract(x,y))
    
    elif choice == 3:
        print(divide(x,y))
    
    elif choice == 4:
        print(multiply(x,y))

    elif choice == 5:
        break

    else:
        print("Choice does not exist")