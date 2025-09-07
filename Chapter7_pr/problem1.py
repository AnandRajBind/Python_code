# problem 1: Write a program to print multiplication table of a given number n.

num=int(input("Enter a number you want to read the table: "))
 
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")


#  proble 2 Attempt problem 1 using while loop

i=1
while(i<=10):
    print(num*i)
    i+=1

# problem3 : Write a program to greet all the person names stored in a list l1 and which starts with letter 'A'.

l =["Anand", "Ravi", "Vijay", "Ajay"]

for name in l:
    if(name.startswith("A")):
        print(f"Hello {name}")



# problem 4 : Write a program to find whether a given number is prime or not.

n=int(input("Enter the number you want check prime or not : "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number")


# problem 5 : Write a program to find the sum of first n natural numbers.

n=int(input("Enter the numbers: "))
i=1
sum=0
while(i<=n):
   sum+=i
   i+=1
    
print(sum)

