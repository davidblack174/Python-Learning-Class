#Logging and Testing
import logging
from logging import basicConfig

# Python program with 2 errors
# var = "Double Value"
# sumvalue = var + "4"
# print(sumvalue)

# Debugging the program
# def dosomething(valuetocheck):
    # if valuetocheck > 4:
    #     print("Bad indent")
# #calling the function
# dosomething(5)

# def loguserage(age):
#     assert age <= 0, "Invalid age was supplied" 
#     print("User age is: ", age)
# #calling the function
# loguserage(5) # This will raise an error

# Logging
basicConfig(filename="app.log", level=logging.DEBUG)

# Ask the user for a value and confirm the supplied value is greater than 0
def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int), "Value entered must be an integer"
    assert (valuetocheck > 0), "Value entered must be greater than 0"
    if valuetocheck > 4:
        print("Value is greater than 4")


#calling the function
var=input("Enter a value: ")
checkvalue(var) # This will raise an error
