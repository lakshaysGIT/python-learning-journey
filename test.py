# print("lakshay is now coding!")
# print("VSCode linked to GitHub")
# print("lakshay is now coding! and VSCode linked to GitHub")

# #taking input from user

# print("Hello World")
# name=input("What's your name,Buddy?")
# print ("Nice to see you",name)
# print (name,"Batra",name,"Batra",name,"Batra")

##-------------------------

## Lets start with Vairables and operators
# myint=10
# myfloat=1.123
# mybool=True
# mystr="LakshayBatra"
# print(mybool)
# print(mystr)

# #operations on variables

# print(myint*myfloat)
# print(myint%myfloat)
# print(myint-myfloat)
# print(myint+myfloat)

# anotherstr="@yahoo.com"
# print(mystr+anotherstr)
# print("L"*3)

# #Logical and comparison operators
# print(myint==10)
# print(myfloat!=20)
# print(myint>1000000)
# print(mybool==True)
# print(mystr=="LakshayBatra")

# print(myint>5 and myfloat<2000)
# print(myint>100 or mybool==True)
# print(myint!=10 or myfloat>100)

# #we can re-declare the previously used variable and override
# myint="STRING"
# print("Now it will print STRING:",myint)

##Sequence: Lists and Tuples
##can contain multiple values separated by comas any datatype

# mylist=[0,1,2,3,True]
# print(len(mylist)) #check length of list
# print(mylist[0])
# print(mylist[-1]) #minus means starts from reverse
# print(mylist[4])
# mylist[4]=False #assigning new value
# print(mylist)

# anotherlist=[False,7,8]
# print(anotherlist)
# anotherlist[0]=True
# print(anotherlist)
# new_my=mylist+anotherlist # adding both lists
# print(new_my)

# mystr=str("LAKSHAY")#defined datatype str here is optional
# print(mystr[::-1]) #string can be reversed like this as slicing works in string
# print(mystr[-1]) #will print only last alphabet
# #string index cannot be changed like list

# ##SLICING IN LIST
# lakshaylist=[10,20,30,"Lakshay",40,"Batra"]
# print(lakshaylist)
# print(lakshaylist[0:6:1])#1st index start point, 2nd is end point which is not inclusive,3rd is step amount value
# print(lakshaylist[::-1])#will reverse and print full, left blank means 0 to last
# print(lakshaylist[3::2])#start from lakshay skip next then batra as step value is 2 means skip every other
# print(lakshaylist[-2])#print second last as minus is added with 2

# #tuples datatype sequence
# #tuples are like lists but values cannot be changed later like str unlike list
# mytuple=tuple((1,5,50,500))
# print(mytuple[1])
# ##mytuple[0]=0     # value change not allowed in tuple
# print(mytuple)
#core diff between list and tuple is tuple cannot be changed rest all same, often used to store data that will never be changed which makes it more memory efficient
#also used to return multiple values from a function

#SET sequence datatype,Only unique values , if multiple - returns only 1 instance
#set indexing not allowed
#sets print is not ordered and changes everytime because indexing not there
myset={1,2,3,3,3,3,7," ","space"} #curly braces used means set
setalternativeway=set ((1,2,3,3,3,3,"    ","a")) #if set defined specifically then paranthesis
print(myset)
print(setalternativeway)
print(sorted(myset,key=str)) # sorted function used for fixed order
print(sorted(setalternativeway,key=str))

#test if value is in sequence 
print("" in myset)
print(3 in setalternativeway)
print(" " in myset)