print("MENU")
print("1. Add Task")
print("2. Remove Task")
print("3. View Task(s)")
print("4. Exit")

a=[]

def add():
    while True:
        val = str(input("Enter a task (Hit Enter when done adding task(s)): "))
        if val == "":
            break
        a.append(val)
        
def remove():
    val = str(input("Enter a task to remove: "))
    a.remove(val)
    
def view():
    print("Here is/are your task(s):")
    print(a)

    
    
while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        add()
    
    elif choice == 2:
        remove()
    
    elif choice == 3:
        view()
        
    elif choice == 4:
        break
    
    else:
        print("Choice does not exist")
    