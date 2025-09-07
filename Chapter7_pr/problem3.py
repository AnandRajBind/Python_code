
# problem 9

# Write a program to print the following star pattern for n=5
'''
* * * * *
*       *
* * * * *
'''

n =int(input("Enter the number : "))

for i in range(1,n+1):
    if(i==1 or i==n):
      print("*"*n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*")
    print("")


# problem 10 
# Write a program to print multiplication table of a given number n in reverse order.
n =int(input("Enter the number : "))

for i in range(1,11):
    print(f"{n} X {11-i} = {5*(11-i)}")