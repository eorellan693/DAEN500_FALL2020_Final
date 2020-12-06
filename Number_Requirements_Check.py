'''
Created on Dec 2, 2020
Last Updated on Dec 3, 2020

@author: Erick Orellana

Final Exam Problem 1

Prompt: Design and implement a Python program that is based on the following requirements: a) program will find all numbers which are divisible by 7 but are not a multiple of 5; and b) numbers between 2000 and 3200
'''
#Get input from user
user_number = int(input('Please enter a number: '))     #Number from user to check against requirements

#Constants used for calculations
divisible_by = 7 
multiple_of = 5
min_range = 2000
max_range = 3200

#Variables to hold results of tests of program requirements
divisible_by_constant = False
multiple_of_constant = False
is_in_range = False

#Confirm if user input is a divisible by the given constant (Requirement A)
if ((user_number % divisible_by) == 0):
    divisible_by_constant = True
else:
    divisible_by_constant = False

#Confirm if user input is a multiple of the given constant (Requirement A)
if ((user_number % multiple_of) == 0):
    multiple_of_constant = True
else:
    multiple_of_constant = False

#Confirm if user input is within the provided range, exclusive of boundaries (Requirement B)
if (user_number < max_range) and (user_number > min_range):
    is_in_range = True
else:
    is_in_range = False
    
#Print results based on the requirements
if (divisible_by_constant == True) and (multiple_of_constant == False) and (is_in_range == True):   #All requirements are met
    print("\n" + "The number {} meets all the requirements!".format(user_number))
else:   #Determine which requirements were not met
    print("\n" + "The number {} does not meet all the requirements!".format(user_number))
    print("\n" + "Here is an explanation of this result:")
    if(divisible_by_constant == False):
        print("- This number is not divisible by {}. (Does not meet requirement A)".format(divisible_by))
    if(multiple_of_constant == True):
        print("- This number is a multiple of {}. (Does not meet requirement A)".format(multiple_of))
    if(is_in_range == False):
        print("- This number does not fall between {} and {}. (Does not meet requirement B)".format(min_range,max_range))

