x=101
def changeVariable():
    #if we donnot decalare x as global we cannot access inside our function
    global x
    print(x)
    x="hello"
    print(x)
a=6
b=7
#we can print multiple variables
print(a,b)