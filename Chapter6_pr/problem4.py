# problem 4: Write a program to check if the length of a username is less than 10 characters or not.  
username=input("Enter username: ")
 
if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")
    
