# assuritytest


This is a short Python scripts I use to test the promotion json file.
To insert the script-level comments as descriptions below.

# Download the python
https://www.python.org/downloads/

# Install the Python package

https://docs.python.org/3/installing/index.html

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




