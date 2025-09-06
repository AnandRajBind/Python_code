# problem 33: Write a program to detect spam comments in a website. The program should ask the user to enter a comment and then check whether the comment contains any spam words such as "make a lot of money", "buy now", "click this", "subscribe this", or "limited time offer". If the comment contains any of these words, the program should print "This is a spam comment". Otherwise, it should print "This is not a spam comment".

p1="Make a lot off money"
p2="buy now"
p3="Limited time offer"
p4="Click this"
p5="subscribe this"

message=input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):
    print("This is a spam message")
else:
    print("This is not a spam message")
