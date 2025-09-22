gender=input("Enter Your gender: ")
age=int(input("Enter Your age: "))

if(age>=18 and gender == "Male" or gender == "male"):
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")
    