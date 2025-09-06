# problem 2: Write a program to check whether a student has passed or failed.
# A student is considered to have passed if he/she has scored at least 33% in each subject and at least 40% overall.

marks1=int(input("Enter marks of subject 1: "))
marks2=int(input("Enter marks of subject 2: "))
marks3=int(input("Enter marks of subject 3: "))

# check for total percentage

total_percentage=(marks1+marks2+marks3)/300*100

if(total_percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print(f"You have passed the exam with {totoal_percentage} percentage")
else:
    print(f"You have failed the exam with {total_percentage} percentage")


