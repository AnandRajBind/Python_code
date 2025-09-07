def far_to_cel(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in Fahrenheit: "))
c=far_to_cel(f)    

print(f"{round(c,2)}℃")