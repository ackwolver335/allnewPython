# creating a variable
x = 4

print(x)            # getting the output

# the above mentioned value is also a number stored in a variable
# let's store a variable with a logical name and provide its value

number = 32             # so we have a number stored in variable called number with value 32

# Strings : Created in Single or Double Quotes
# creating a single quote string
myName = 'My Name is Abhay'

# Double quotes
myAge = "My Age is 21"

# type(variable_name) : method used to get the type of any variable/data
print(type(myAge))          # this will provide a string class indicating that the data type stored in myAge is of String Data Category

# String Concatenation : Adding two or more string together to make a new one.
str1 = 'Things will get'
str2 = ' better soon!'

print(str1 + str2)          # this will print the combination of both of these strings

# float : The decimal part of numerical digits or numbers are considered as floats.

myBMI = 23.55

print(myBMI)
print(type(myBMI))      # this will provide you the float class

# complex : All mathematical calculations, that including the calculations regarding equations are considered in this Data type category
comp1 = 23j + 45j
print(comp1)                # will print the result after calculating and solving the equation

# You can also get the data type of it using type() method.
# Note : Don't try adding two or more different data types together, it will cause Type Error

# Boolean : Data type storing 2 values only either True or False, and are case-sensitive while using.
myConcept = False

print(myConcept)
print(type(myConcept))

# example use-case with statement
print(1 == 2)                           # will return False, as 1 is not equal to 2

# Data Structures
# List : Used for storing different values inside square brackets, seperated by commas

numbers = [1,2,3,4]         # simple list containing numerical data types

names = ['Navy','Army']     # list of storing string as its data types

# storing different category of data types inside one variable
dataTypes = [34.55,[3,4,4],44,'String']
print(dataTypes)                                # this will look similar to the one we represented above

# len() : Method to get the length of any variable, used with the lists mostly or other data structures in order to get the number of elements present in it.
print(len(dataTypes))

# append() : We can also append the element in the list by using this method, but it will add the element to the ending of the list not at specific place
numbers.append(5)
print(numbers)          # you can check the updated values in the output

# sets : Another data type that is used to store the values similar to a list but in Curly Brackets {}, as in case of set we can't do the duplicacy one value needs to be stored once at a time. These are similar to the sets that are used in Mathematices
set1 = {2,3,3}
print(set1)

print(len(set1))            # you must be thinking it will print 3, but it will print 2 considering unique elements only

print({1,2} == {2,2,1})       # here it will return True cause, sets are independent of orders.

# tuple : It is used to store data values in parenthesis, and can't be changed once it is declared.
tup1 = (1,2,3)
print(tup1)

print(len(tup1))

# tup1.append(5)            # writing this in comment not in order to get more errors.

# Note : We can't add the elements to tuples similar to lists, once it is declared try doing this will generate an error.

# left at 5:51