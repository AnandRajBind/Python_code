

a= int(input("Enter Your age:   "))

# if elif else ladder
if(a>=18):
    print("You can drive")
    print("You are an adult")
elif(a<0):
    print("You have entered invalid age")
elif(a==0):
    print("You have entering 0 age which is not a valid age")
else:
    print("You cannot drive")    
    

print("Thank you")