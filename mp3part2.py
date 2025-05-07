print("MENU")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
print("3. Exit")

def ctof(a):
    return (a*(1.8)+32)
    
def ftoc(a):
    return (a-32)*(5/9)

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        x = float(input("Enter temperature in Celsius: "))
        print(ctof(x))
    
    elif choice == 2:
        x = float(input("Enter temperature in Fahrenheit: "))
        print(ftoc(x))
    
    elif choice == 3:
        break

    else:
        print("Choice does not exist")