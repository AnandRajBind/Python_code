import random

'''
1 for snake
-1 for water
0 for gun
'''

computer= random.choice([-1, 0, 1])
yourstr=input("Enter s for snake, w for water, g for gun: ")
youDict={'s':1, 'w':-1, 'g':0}
you=youDict[yourstr]
reverseDict={1:'Snake', -1:'Water', 0:'Gun'}

print(f" You chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(you==computer):
    print("Match Draw")
else:
    if(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You Lose")
    elif(computer == 1 and you == -1):
        print("You Lose")
    elif(computer == 1 and you == 0):
        print("You Win")
    elif(computer == 0 and you == -1):
        print("You Win")
    elif(computer == 0 and you == 1):
        print("You Lose")
    else:
        print("Something went wrong")

 
#  another way to do this problem

# if(you==computer):
#     print("Match Draw")
# else:
#     if((computer -you)== -1 or (computer -you)==2):
#         print("You lose")
#     else:
#         print("You Win")