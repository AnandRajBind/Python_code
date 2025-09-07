# problem 6
# Write a program to find the factorial of a given number n.

n=int(input("Enter the number you want to find factorial: "))
fact=1
for i in range(1,n+1):
    fact=fact*i

print(f"The factorial of {n} is {fact}")


# problem 7 write a program to print the following star pattern for n=5

'''
    *
   ***
  *****
 *******
*********
'''
# print statement bydefault adds a new line after it. To avoid that we use end=""
n =int(input("Enter the number of rows: "))
# i = row number Example n=5, i=1 to 5
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="") # 
    print("") # to add a new line after each row
    
    
# problem 8
# Write a program to print the following star pattern for n=5
'''
*
* *
* * *
* * * *
* * * * * 
'''

n =int(input("Enter the number : "))

for i in range(1,n+1):
    print("* "*i)

