'''
Created on Dec 2, 2020
Last Updated on Dec 3, 2020

@author: Erick Orellana

Final Exam Problem 2

 Prompt: Define a class with at least two methods
 Method 1: getString: to get a string from console input; and,
 Method 2: printString: to print the string in upper case
'''

#Class to get a string from a user, convert the string to all upper case letters, and print the results
class StringConversion:
    #Initiating variables
    def __init__(self):
        self.user_input = ''
    
    #Get a string from the user
    def getString(self):
        self.user_input = input("Enter a string to convert to upper case letters: ")
    
    #Print the string in all upper case letters  
    def printString(self):
        print("\n" + "Here are your results -")
        print("You entered the string: " + self.user_input)
        print("In all upper case letters this string is: " + self.user_input.upper())

#Calling the class and methods to get a string from the user and show the string in all upper case letters           
user_input = StringConversion()
user_input.getString()
user_input.printString()

