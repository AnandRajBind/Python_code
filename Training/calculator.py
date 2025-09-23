# Day 2 
# calculator using match case

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

# operation=int(input("Enter 1 for Addition , 2 for Subtraction , 3 for Multiplication , 4 for Division "))
operation=input("Enter your operations (+, -, *, / ) ")

match operation:
    case "+":
        print(f"Addition of {num1} and {num2} is: {num1+num2}")
    case "-":
        print(f"Substraction of {num1} and {num2} is: {num1-num2}")
    case "*":
        print(f"Multiplication of {num1} and {num2} is: {num1*num2}")
    case "/":
        print(f"Division of {num1} and {num2} is: {num1/num2}")
    case _: 
        print("Invalid Operation")

