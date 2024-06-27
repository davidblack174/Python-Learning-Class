import math     #Maths Library Defined as math
from math import sqrt    #Maths Library Defined as sqrt
import math as m    #Maths Library Defined as m
import os, sys    #Operating System Library Defined as os, sys

# #Maths Library
# y=math.sqrt(16)
# z=m.sqrt(16)
# #print the square root of 16
# print(y)
# print(z)
# print(sqrt(16))

# #Exercise 2
# absolute = -5.999
# floor_test = 198.42
# #Absolute value of a number
# result1 = math.fabs(absolute)
# result2 = math.floor(floor_test)
# #Print the absolute value of a number
# print(result1, " is the absolute value of ", absolute)
# print(result2, " is the flow of ", floor_test) 

#File handlers
#Open a file
file=open("./sampleFile.txt","w")
#Write to a file
file.write("Hello World I am writing into the file")
#read from a file
file=open("./sampleFile.txt","r")
#Print the content of the file
print(file.read())
#close a file
file.close()


# #Try and Except
try:
    file=open("./sampleFile.txt","r")
    print(file.read())
except:
    print("File does not exist")

finally:
    print("End of the program")

#Using OS Library
# print(os.getcwd())
# os.rename("./sampleFile.txt","newFile.txt")

#Using Sys Library
print(sys.path)
sys.copyright
sys.version
sys.version_info
sys.platform