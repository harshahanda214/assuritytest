import requests
import jsonpath
import json

# Json file data
response = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false")
print(response.status_code)
assert response.status_code == 200
data = response.json()
print (data['Name'])
assert data['Name'] == 'Carbon credits', "Name is found"
AssertionError ('name is not found')
print (str(data['CanRelist']))
assert data['CanRelist'] == True, "CanRelist is found as True"
AssertionError ('CanRelist is not found')
print(str(data['Promotions']))
list = data['Promotions']
S = input("add the name are you looking?")
T = input("add the Description are you looking?")
for i in range(len(list)):
    if list[i].get('Name').count(S) > 0 and list[i].get('Description').count(T) > 0:
        print("Required " + (S) + " and " + (T) + " is found in ID " + str(list[i].get('Id')))
    else:
        print("Required \"" + list[i].get('Name') + "\" and \"" + list[i].get('Description') + "\" is not found in ID" + str(list[i].get('Id')))
