# Chapter 2 : QuickStart

- 

## Topics Covered :

1. **Variables & Types**
2. **Data Structures**
3. **Operators**
4. **Control Flow**
5. **Functions**
6. **Classes & Objects**
7. **About the Challenges**

**Note** : All codes regarding this files are given in the file named **CH2.py** in order to get the code file run by you, and find the reason behind running a particular set of code.

### Variables & Types

#### Storing/Defining a Variables

- In order to store any value, we first need to give a variable name and then **=** symbol, after this the value of the variable with a particular data type.

```bash
# storing a number into a variable
x = 4

print(x)

# for directling printing the value of x on the screen in IDLE we can use it as mentioned below
x           # this will direclty print the value of x on screen but in IDLE
```

#### Rules/Protocols for Variable Creation :

- Variable's name must starts with an *alphabet character*, no number or symbol at the beginning.
- On the place of using space in b/w variable's name using **_** symbol, **ex** - on the place of writing *my age*, write it a **my_age**. It will not create an error.
- Use camelCase on the place of bold structure in variable names. *Example* - Use **myAge**, not **MyAge**.
- Mostly recommeded, if you don't want to use the **camelCase**, you can use the lowercase at the beginning of any variable's name.

#### Data Types

- **Numbers** : The general numerical values that are used to denote a count or digital symbol are consider in  it.

```python
num = 23

print(num)          # will simply print 23 as it numerical data type.
```

- **String** : Strings are generally considered set of charaters that are used to store data in b/w **'** or **"** (Single or Double Quotes). Characters can be number, symbol or any alphabet.

```python
# creating a string with single quote
myName = 'Abhay'

print(myName)       # will print the set of characters stored inside myName

# in order to get the type or data type of any variable, we uses the type(variable_name) method here
dataType = type(myName)

# from above we have store a data type of myName into dataType named variable
print(dataType)

# we can also add 2 or more strings together in order to make a new string containing more data
# this addition is considered as Concatenation of Strings.
str1 = 'First String and '
str2 = 'Second String'

print(str1 + str2)
```

- **float** : These are the category of data types that are used to store the numerical values containing *Decimal* in it. Decimal can either be on *right* or *left* side of the number depending on the number or values on each side.

```python
# storing a float
myBMI = 23.4

print(myBMI)
print(type(myBMI))
```

- **Complex** : The Mathematical part where different complex statements are used including alphabet with numerical digits, are considered in this **Complex** data type category.

```python
# storing a complex variable
var1 = 23j * 44j

print(var1)             # will print the values after solving the complex equation

# you can also get the category of its data type by using the type() method
# Doing this will cause Type Error, it is an error which is caused, stopping the program to run after that particular point. 
```

**Note** : We can't add two different data types together in their initial formats.

- **Boolean** : These are the data types that are build on the concept of Machine Code, i.e. 1 or 0 or in simple words True or False, while using these remember to be Case-Sensitive.

```python
myConcept = True

# this will not store any particular value cause these are data type which have their fixed values
print(myConcept)

# example statement where it is used
print(1 == 1)                                   # here it will be used as returning whether the statement written inside the print is True or False
```

### Data Structures

- These are used to store a ray of values, unlike single values that we just stored in the Code above, unlike *Strings*, *Numbers*,..etc. So, here we have different categories assigned, to store different structures of data.

#### Different Categories of Data Structures

- **List** : It is used to store the data in b/w **Square Brackets** [] seperated by commas. And the values can be any single value or variable, or any other data type like a list inside another. As, it will be considered as Single element of the List inside which it is stored.

```python
# creating a list of number
numbers = [1,2,3,4,5]
print(numbers)                          # this will simply print the list

# creating a list of another data type, like a list of String (Names)
names = ['Abhay','Ram','Carry']
print(names)                            # similarly here also will print the list of different names

# creating a list of different data types
dataTypes = ['String',34,[4,5,5],45.6]          # list containing different data types in it.
print(dataTypes)

# let's count the number of elements present in this list, with the help of len() method
print(len(dataTypes))

# we can also store it
length_of_data = len(dataTypes)

# we can also add elements to list by simply using a method called as append() will add the element at the ending of the list
print(numbers)
numbers.append(7)

print(numbers)      # here you can check the updated value
```

- **Sets** : This data type is used to store values similar to list and are used similar to the sets that are used in Mathematices. It is independent of order, while storing any value.

```python
# storing a set
set1 = {3,4,5,5}
print(set1)

# getting its data types
print(type(set1))

print([1,2] == [2,1])               # will print False as shown the order is different

print({1,2} == {2,1})               # will print True as its independent of order while storing any value
```

- **tuples** : This data type is used to store the elements in the paranthesis, and once declared can't be modified similar to other data types. In coding term, we consider them as **Unmutable**, means can't be changed once it is declared.

```python
# declaring a tuple
tup1 = (1,2,3)
print(tup1)

# we can count the length
print(len(tup1))

# we can check the statement
print((1,2) == (2,1))               # will return False, as Tuples considers their order properly

# adding element will provide us error
tup1.append(4)
```

**Note** : Similar to adding element to the lists using *append()* method we can't do the same with the tuples, cause tuples can't be changed once these are declared. Tuples are memory efficient. Good for storing, x or y coordinates.