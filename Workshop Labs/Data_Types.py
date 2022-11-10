#DATA TYPES

#In python a string, is shortened to str and refers to anything inside quotes. 
#The quotes can be double or single. 
#The examples below are identical to python:
"The quick brown fox jumped over the lazy dog"
'The quick brown fox jumped over the lazy dog'

#For a direct quote in your sentence:
'The error message was "Incorrect DataType"'

#Strings, like all data types, can be assigned to a variable:
first_name = "Monty"
last_name = "Python"

#You can add strings together using variables. This concatenates (links) them:
print(first_name+last_name)

#To separate:
print(first_name + " " + last_name)

#If you want to use the value of a variable in the middle of a string, you can do this a few ways in python with the .format() method:
first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}".format(first_name, surname))

#Since python version 3.6 it has been possible to use a format called f-strings to include variables in your strings. 
#Some people find this format easier to read:
firstname = "Jane"
surname = "Doe"
print(f"My first name is {firstname}. My family name is {surname}")

#Choose whichever is the easiest for you.

#If you want your text to go over several lines you can use \n and \t. 
#The \ character is called an escape character.
#The n tells python to put the text on the next line.
#The t tells python to add a tab spacing.
string = "This is a string over\nthree lines\n\twith the third line indented"
print(string)

################################################################################

#An integer is a whole number such as 50. The data type integer is abbreviated to int.
#A floating point number is a number followed by a decimal point such as 50.5.

#You can't add an integer and a string together regularly, but you can turn the integer into a string to add them:
my_int = 50
sentence = "The total comes to: "
print(sentence + str(my_int))

#We have used the str() method to convert the variable from an integer to a string. 
#In most cases python will determine the type of data without having to declare it. 
#However, it can be useful to tell python exactly how you want to treat the data type. 
#Other examples are:
str() returns a string object
int() returns an integer object
float() returns a floating point object
bool() a boolean value of True or False

################################################################################

#A dictionary is a way of storing related information in key-value pairs. 
#It uses a key as an identifier and a value to store the information. 
#For example, the key could be first_name and the value could be Ada.
#Dictionaries can be created by assigning the key-values you want to store in the dictionary:
user = {"first_name":"Ada"}
print(user)
#If you are going to be adding the contents of the dictionary later, you can declare an empty dictionary. 
#You can create an empty dictionary in two ways:
account_details = {} or account_details = dict()

#To read the value associated with a key, you need to provide the name of the dictionary and the the value of the key inside square brackets:
user = {"first_name":"Ada"}
print(user["first_name"])

#Dictionaries are mutable, which means they can be changed after you create them. 
#You can add, update or delete the key-value pairs in a dictionary.
#To add:
user["family_name"] = "Byron"
print(user)
#Output = {'first_name': 'Ada', 'family_name': 'Byron'}

#To modify:
user["family_name"] = "Lovelace"
print(user)
#Output = {'first_name': 'Ada', 'family_name': 'Lovelace'}

#To delete:
del user["family_name"]
print(user)
#Output = {'first_name': 'Ada'}

################################################################################

#A list is an ordered sequence of values separated by spaces. 
#For example: [0,1,2,3,4] or ["apples","oranges","bananas"].
#A list can contain other objects, for example dictionaries, which we learned about in the last lesson. 
#For example:
#[{"fruit_type":"apples"},{"number":50}]

#To create an empty list:
fruit = [] or fruit = list()

#To read what is in the list, use indexing:
fruit = ["apples","oranges","bananas"]
print(fruit[1])                                 #Prints in the position starting from 0. Oranges is in position 1 in the list

#To get the length of the list:
print(len(fruit))

#To return the last value or work backwards in a list:
print(fruit[-1])
#Output = bananas
print(fruit[-2])
#Output = oranges

#You can use append() to add an element to the end of the list:
fruit.append("kiwi")
print(fruit)
#Output = ['apples', 'oranges', 'bananas', 'kiwi']

#If you want add an element at a specific point in the list you can use the index value with the insert() method:
fruit.insert(2, "passion fruit")
print(fruit)
#Output = ['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#To permanently sort a list:
fruit.sort()
print(fruit)
#Output = ['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

#To reverse the list:
fruit.reverse()
print(fruit)
#Output = ['passion fruit', 'oranges', 'kiwi', 'bananas', 'apples']
#To change it back, just use the reverse() method again.

#To remove elements from a list:
del fruit[1]
print(fruit)
#Output = ['passion fruit', 'kiwi', 'bananas', 'apples']

#If you want to use the value after removing it from a list you use the pop() method. 
#To use pop(), you need to store the value you have removed from the list inside another variable:
favorite_fruit = fruit.pop()
print(favorite_fruit)
#Output = apples

#In this example, pop() has returned the last element in the list, which is the default for pop(). 
#You can return any element with the pop() by using the index value:
fresh_fruit = fruit.pop(1)
print(fresh_fruit)
#Output = kiwi

#If you don't know the index position, or you don't want to remove the last item in the list, you can use the remove() method to specify the value of the element you want to remove:
fruit.remove('bananas')
print(fruit)
#Output = ['passion fruit']