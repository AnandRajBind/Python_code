# problem 1 write a program to take name as input and print a greeting message for that name.

name =input("Enter your name: ")
print(f"Good AfterNoon{name}") # 

# problem 2  Write a program to fill in a letter template given below with name and date.

letter= """
Dear <|NAME|>,
You are selected!
<|Date|>
"""
print(letter.replace("<|NAME|>", "Anand").replace("<|Date|>", "20/08/2023"))


# problem 3 Write a program to detect double spaces in a string.
st="This is a  string  with  double spaces."
print(st.find("  ")) # finding the first occurence index. otherwise -1  print.

# problem 4 Replace double spaces with single space in the string.
print(st.replace("  ", " ")) # replacing double space with single space

print(st) # string are immutable so orginal string will not change.

# problem 5 Write a program to format the following letter using escape sequence characters.


letter="Dear Anand,\n\t This python course is nice. \nThanks!"
print(letter)