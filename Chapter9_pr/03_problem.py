# problem 3 : generate multiplication tables from 2 to 20 and save them in separate text files

def generateTable(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)



#  generate tables from 2 to 20
for i in range(2,21):
    generateTable(i) # function call