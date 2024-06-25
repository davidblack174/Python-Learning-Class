 #while loop

counter=0

while counter < 3:
     print("Enter the number: ", counter)
     counter=counter+1

print("End of the program")

# #List Example
list=[1,2,3,4,5]
class_roster= ["Xiulan","Kwaku","Shirley"]
test_scores= [86,93,80]

print(class_roster)
print(test_scores)

# #For loop
for i in range(0,5):
     print("Enter the number: ", i)
     print("The number is: ", list[i])
for i in range(0,3):
     print("The student is: ", class_roster[i])
     print("The test score is: ", test_scores[i])
# #or
for student in class_roster:
     print("The student is: ", student)
for score in test_scores:
     print("The test score is: ", score)
# The use of the input function
name = input("What’s your name?")
print("Hello " + name)

