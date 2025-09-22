print("Hello, World!")
 
data=12
data="anand"
 
print(data)

# list

list=[ "Anand" , "24MCA044", "Kafurpur Patahana Jaunpur Uttar Pradesh India 222001", "MCA" ]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])

# print list using  formatted string
print(f"Name: {list[0]}\n Roll No.: {list[1]} \n Address: {list[2]}\n Course: {list[3]}")

# print list using loop
for i in list:
    print(i)


# tuple
# immutable, duplicate values allowed, ordered
tuple=("Anand" , "24MCA044", "Jaunpur UP 222001", 8726271088)

print(tuple)

print(f"{tuple[0]} : {type(tuple[0])} \n {tuple[1]} : {type(tuple[1])} \n {tuple[2]} : {type(tuple[2])} \n {tuple[3]} : {type(tuple[3])}")

# set
# unordered, mutable, no duplicate values allowed
s={"Anand" , "24MCA044", "Jaunpur UP 222001", 8726271088, "Anand"}
s1={} # this is empty dictionary
s2=set() # this is empty set
print(type(s1))
# print(set)



# dictionary 
# ordered, mutable, no duplicate keys allowed

dict={"name":"Anand", "roll":"24MCA044", "address":"Jaunpur UP 222001", "phone":8726271088}
print(dict)
dict["email"]="anandrajbind35@gmail.com" # adding new key value pair
print(dict) # adding new key value pair


dict.pop("phone") # removing key value pair
print(dict)

