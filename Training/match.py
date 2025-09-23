# day 22
# It is alternative of switch case in other programming language

day=input("Enter Yor days: ")

match day :
    case "Sunday" | "sunday":
        print("Sunday")
    case "Monday" | "monday":
        print("Monday")
    case "Tuesday" | "tuesday":
        print("Tuesday")
    case "Wednesday" | "wednesday":
        print("Wednesday")
    case "Thursday" | "thursday":
        print("Thursday")
    case "Friday" | "friday":
        print("Friday")
    case "Saturday " | "saturday":
        print("Saturday")
    case _:
        print("Invalid Days")    



     