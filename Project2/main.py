import random

computerInput=random.randint(1,100)

userInput=-1

guesses=1


while(userInput != computerInput):
    userInput=int(input("Guess the Number: "))
    if(userInput > computerInput):
        print("Lower Number Please")
        guesses+=1
    elif(userInput<computerInput):
        print("Higher Number Please")
        guesses+=1


print(f"You have guess the number {computerInput} correctly in {guesses} attampts ")