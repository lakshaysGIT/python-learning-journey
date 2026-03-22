# ##Dictionaries works in key-value pair like sequence and keys should be unique
# #key:value
mydict = {
    "one" : 1,
    "two" : 2,
    3 : "three",
    4.5 : ["four","pointFive"]
}
print(mydict)
#dictionaires accessed by keys (Left side act as variable and right side as value)
print(mydict["one"])
print(mydict[4.5])

mydict["seven"]=7
print(mydict)

print("two" in mydict) #true or false
#Keys and Values functions in dictionaries 
print(mydict.keys())
print(mydict.values())

# for loop to iterate over all items in dictionary dictionary
for key, val in mydict.items(): #iterates one by one on all key:val 
    print(key, val) #prints key:val each in separate line