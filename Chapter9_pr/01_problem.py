f=open("poem.txt")

content = f.read()

if("twinkle" in content):
    print("twinkle is present in the file")
else: 
    print("twinkle is not present in the file")
f.close()