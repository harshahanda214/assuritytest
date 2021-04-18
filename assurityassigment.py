import requests
import jsonpath
import json

# Json file data
file = open('C:\\Users\\kgaur\\OneDrive\\Desktop\\datajson.json', 'r')
#reading data from the json file
data = file.read()
print(data)
# parsing json data
obj = json.loads(data)
print (str(obj['Name']))
assert obj['Name'] == 'Carbon credits', "Name is found"
AssertionError ('name is not found')
print (str(obj['CanRelist']))
assert obj['CanRelist'] == True, "CanRelist is found as True"
AssertionError ('CanRelist is not found')
print(str(obj['Promotions']))
list = obj['Promotions']
S = input("add the name are you looking?")
T = input("add the Description are you looking?")
for i in range(len(list)):
    if list[i].get('Name').count(S) > 0 and list[i].get('Description').count(T) > 0:
        print("Required " + (S) + " and " + (T) + " is found in ID " + str(list[i].get('Id')))
    else:
        print("Required \"" + list[i].get('Name') + "\" and \"" + list[i].get('Description') + "\" is not found in ID" + str(list[i].get('Id')))
