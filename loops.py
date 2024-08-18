#traversing in list
list=[5,6,7,8,9]
squares=[]
#like for each loop
for value in list:
    val=value*value
    squares.append(val)
#traversing through string
s="hananiah martin"
vowels=[]
for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        vowels.append(ch)

tuple=("hananiah","martin","melchi","jacob")
for i in range(0,len(tuple)):
    print(tuple[i])
for s in tuple:
    print(s)
#while looop
counter=0
while counter<10:
    print("counter is less than 10")
    counter=counter+2
# printing substrings
str="abc"
for i in range(0,len(str)):
    for j in range(i+1,len(str)+1):
        print(str[i:j])

        