#type 1->Numbers
a=6
print(type(a))
str="hananiah"
print(type(str))
complex=1+5j
print(type(complex))
#type2->Sequence(String)
string="hananiah martin"
#slicing
print(string[0:len(string)-1])
temp=str*3
print(temp)
#Sequence(list)
#list are like arrays in C but in python we can have different data types
list=[1,2,3,"hananiah"]
list[1]="martin"
print(list*2)
#Sequence(tuple)
#tuples are like lists but we cannot manipulate them\
tuple=("hananiah",1,2)
print(tuple[1:])
#sequence(dictionary)
dictionary={1:"hritik",2:"shivakant"}
print(dictionary.values())
#set
set={"hananiah",1,"badminton"}
set.remove(1)
print(set)