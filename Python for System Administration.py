import subprocess
from os import system


# #Class Activity for Linux System Administration
# def new_user():
#     confirm='N'
#     while confirm !='Y':
#         username=input('Enter a username: ')
#         print('Is this correct ' +username+ '? (Y/N):')
#         confirm=input().upper()
#     system('sudo useradd -m '+username)

# #class activity for windows system administration
# # def new_user():
# #     confirm='N'
# #     while confirm !='Y':
# #         username=input('Enter a username: ')
# #         print('Is this correct ' +username+ '? (Y/N):')
# #         confirm=input().upper()
# #     system('net user '+username)

# #Call the function
# new_user()

# #Class Activity for Linux System Administration
# def delete_user():
#     confirm='N'
#     while confirm !='Y':
#         username=input('Enter a username: ')
#         print('Is this correct ' +username+ '? (Y/N):')
#         confirm=input().upper()
#     system('sudo userdel -r '+username)

# #class activity for windows system administration
# # def delete_user():    
# #     confirm='N'
# #     while confirm !='Y':
# #         username=input('Enter a username: ')
# #         print('Is this correct ' +username+ '? (Y/N):')
# #         confirm=input().upper()
# #     system('net user '+username+' /delete')

# #Call the function
# delete_user()

#Class Activity Adding a user to a group for Linux System Administration
# def add_user_to_group():
#     confirm='N'
#     while confirm !='Y':
#         username = input("Enter the name of the user that you want to add to agroup: ")
#         output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
#         print("Enter a list of groups to add the user to")
#         print("The list should be separatedby spaces, for example:\r\n group1 group2 group3")
#         print("The available groups are:\r\n " + str(output))
#         chosenGroups = input("Groups: ")
#         #output = output.split(" ")
#         #chosenGroups = chosenGroups.split(" ")
#         print("Add To:")
#         found = True
#         groupString = ""
#         for grp in chosenGroups:
#             for existingGroup in output:
#                 if grp == existingGroup:
#                     found = True
#                     print("-Existing Group: " + grp)
#                     groupString= groupString + grp + ","
#                     if found == False:
#                         print("-New Group : " + grp)
#                         groupString = groupString + grp + ","
#                     else:
#                         found = False
#                     print("Is this correct? (Y/N)")
#                     confirm = input().upper()
#                     if confirm == "Y":
#                         system("sudo usermod -a -G " + groupString + " " + username)
#                         break
#                     else:
#                         continue

# #call the function
# add_user_to_group()


#Class Activity Adding a user to a group for linux system administration
def install_or_remove_packages():
    confirm='N'
    while confirm !='Y':
        print("Do you want to install or remove a package? (I/R)")
        action = input().upper()
        if action == "I":
            package = input("Enter the name of the package you want to install: ")
            system("sudo apt-get install " + package)
        elif action == "R":
            package = input("Enter the name of the package you want to remove: ")
            system("sudo apt-get remove " + package)
        else:
            print("Invalid option")
            continue
        print("Is this correct? (Y/N)")
        confirm = input().upper()
#call the function
install_or_remove_packages()
                 