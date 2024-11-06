#Dictionaries

#Structure - Key: Value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# How to retrieve a value from the Dictionary
#Provide the Key
print(programming_dictionary["Bug"])

#How to insert a new var in the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Creating an empty dictionary
empty_dictionary = {}

#Editing an item on a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#Looping through a dictionary
for key in programming_dictionary:
    print(key)  #This way will, doing similarly as used in lists, print the 'key', not the 'value'
    print(programming_dictionary[key])

#Wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary)