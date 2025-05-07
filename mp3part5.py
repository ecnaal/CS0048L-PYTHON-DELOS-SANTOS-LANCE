print("MENU")
print("1. Add Score")
print("2. Calculate Average")
print("3. Exit")

sub = []
sco = []

def average(a, b):
    sub.append(a)
    sco.append(b)
    scolen=len(sco)
    average = sum(sco)/scolen
    return average
    
while True:
    choice = int(input("Enter choice:"))
    if choice == 1:
        x = str(input("Enter subject: "))
        y = int(input("Enter grade: "))
        val = average(x, y)
        print("Score Added")
    elif choice == 2:
        print("Average grade: ",val)
        
    elif choice == 3:
        break
    
    else:
        print("Choice does not exist")