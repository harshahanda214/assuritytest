# assuritytest


This is a short Python scripts I use to test the promotion json file.
To insert the script-level comments as descriptions below.

#Download the python
https://www.python.org/downloads/

# Install the Python package

https://docs.python.org/3/installing/index.html


# Using PyCharm community version
https://download-cf.jetbrains.com/python/pycharm-community-2021.1.exe

# Instructions to install PyCharm
Download the pycharm-community-2021.1.exe
Run the pycharm-community-2021.1.exe
Once the installation is done Pycharm is ready to create python project

#Create a pyhton project
Goto File menu and create a "New project".
The user will be asked to create the new project and choose a workspace for it, for example : C:\Users\xxxx\PycharmProjects\pythonProject1.
The user can also create a python file and start writing the code.
It is upto the user to create a project or just a python file in order to run the python script.
Once the file or project is created the next task is to import the important modules.
Three modules have been imported in order to work with API and JSON.


#How to import the modules in PyCharm
There are three modules imported to work with API and JSON.
These are requests,jsonpath,json.
To import a module goto File in the menu bar and select "Settings" inside it.
Goto "Python project" and specifically to the project the user have created.
Now goto "Python interpreter" inside the python project.
Click on the "Plus" icon to install a new package.
Write the name of the package in the search bar.
Click on the "Install Package" icon.


# Scripts
The subheadings link to the script contents on GitHub.


## [readme.md](https://github.com/harshahanda214/assuritytest/edit/main/README.md)
+ Authors: [Harsha Arora](https://github.com/harshahanda214)
+ Created: 2021.04.18


Generates the README for
[harsha/assurityassignment](https://github.com/harshahanda214/assuritytest)
so that the README and scripts contain synchronized documentation.


## [assurityassigment.py](https://github.com/harshahanda214/assuritytest/blob/main/assurityassigment.py)
+ Authors: [Harsha Arora](https://github.com/harshahanda214)
+ Created: 2021.04.18


This script [assurityassigment.py](https://github.com/harshahanda214/assuritytest/blob/main/assurityassigment.py) needs an input as a Name and Description which you want to search in the api.

Extracted the [api](https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false) and get the [json](https://github.com/harshahanda214/assuritytest/blob/main/datajson.json) file is having array of records,example below:

```
For example:
Id: 1 
Name: Basic 
Description: Lowest position in category 
Price: 0.0
MinimumPhotoCount: 0

```


# Acception Criteria of the test case
+ Authors: [Sam Hooper](https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false)
+ Shared: 2021.04.13

```
Name = "Carbon credits"
CanRelist = true
The Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

```


## [assurityassigment.py](https://github.com/harshahanda214/assuritytest/blob/main/assurityassigment.py)
+ Authors: [Harsha Arora](https://github.com/harshahanda214)
+ Created: 2021.04.18


This is a Python script output matches the element name and description with their ID.
This is helpful to find the ID according to name and description.

Tester needs to pass the name and description as input. 

### Usage
Ensure `name` and `description` are correctly set below.

Enter the input name is Gallery and Description is "Good position" which check in the api whether this conditions matches or not, if matches then answer the ID number.

```buildoutcfg
for example

add the name are you looking?Gallery
add the Description are you looking?Good position
Required "Basic" and "Lowest position in category" is not found in ID1
Required Gallery and Good position is found in ID 2
Required "Feature" and "Better position in category" is not found in ID3
```



