# problem 6: Write a Python program to convert inches to centimeters.

def inch_to_cm(inch):
    return inch*2.54

n=int(input("Enter value in inches: "))
print(f"{n} inch = {round(inch_to_cm(n),2)} cm")


# problem 7  Write a Python program to remove a name from a list if it is present in the list.

l=["Anand", "Bharat", "Chandan", "Dinesh"]

def remove_name(name):
    if(name in l):
        l.remove(name)
        return f"{name} name removed successfully"
    else:
        return f"{name} name not found in the list"

name=input("Enter name to be removed: ")
print(remove_name(name))