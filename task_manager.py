"""
Capstone Project II

This Python program is to help a small business manage tasks assigned to each member of the team.
This program works with two text files, user.txt and tasks.txt.
tasks.txt stores a list of all the tasks that the team is working on.
user.txt stores the username and password for each user that has permission to use this program.
"""

#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
file_info = open('user.txt', 'r')
lines = file_info.readlines()

username_list = []
password_list = []

for line in lines:
    u_name, pswd = line.strip("\n").split(", ")
    username_list.append(u_name)
    password_list.append(pswd)

username = ""

username = input("\033[0;34;47m Username: ")

while not username in username_list:
    print("Invalid username. Try again!")
    username = input("Username: ")

position = username_list.index(username)
 
password = input("Password: ")

while password != password_list[position]:
    print("Invalid password. Try again!")
    print(f"Username: {username}")
    password = input("Password: ")

print(f"\n\033[0;34;47mWelcome {username}!\n")

file_info.close()


while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input(''' ************Main Menu************
Please select one of the following options:
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

    if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        

        # Compulsory Task 2 - admin menu
        
        username_reg = ""
        attempt_rule1 = True

        while attempt_rule1 == True:
            if username != "admin":
                is_admin = False
                print("\nOnly the admin is allowed to register users.\n")
                admin_choice = (input("Would you like the admin to login? (y/n)?: \n")).lower()
                
                if admin_choice == 'y':
                    print("****Admin login****")
                    username_reg = input("\033[0;34;47mUsername: ")

                    attempts_uname = 0
                    count = 3

                    while username_reg != "admin":
                        print("Invalid username!")
                        attempts_uname += 1
                        if attempts_uname == 3:
                            print("\nYou have had 3 attempts. Sorry, only the admin is allowed to register users.\n")
                            print("Returning to the main menu....\n")
                            attempt_rule1 = False
                            break
                        else:
                            print(f"\nYou have {count - attempts_uname} attempts to login the username as admin!")
                            username_reg = input("Username: ")
                        

                    if username_reg == "admin":
                        position = username_list.index(username_reg)
                        password = input("Password: ")
                
                        while password != password_list[position]:
                            print("\nInvalid password. Try again!\n")
                            print(f"Username: {username_reg}")
                            password = input("Password: ")

                        print(f"\n\033[0;34;47m Welcome {username_reg}!\n")
                        is_admin = True
                        break
                
                elif admin_choice == 'n':
                    break

                else:
                    print("Sorry, invalid input! Please try again!")
                
            elif username == "admin":
                is_admin = True
                break

            else:
                is_admin = False
                print("Only the admin is allowed to register users.")
                print("Returning to Main menu.....\n")
                break


        if is_admin == True:
            while True:
                menu_admin = input('''\t\t\t\t\t************Admin Menu************
                Please select one of the admin options:
                rn - Registering a new user
                t - View total number of tasks
                u - View total number of users
                x - Exit from the admin menu
                : ''').lower()

                if menu_admin == 'rn':
                    """ Only the admin is allowed to register users. 
                    In this block, the following steps are carried out:
                    - Request input of a new username
                    - Request input of a new password
                    - Request input of password confirmation.
                    - Check if the new password and confirmed password are the same.
                    - If they are the same, add them to the user.txt file,
                    - Otherwise you present a relevant message.'''
                    """
                    file_info = open('user.txt', 'r')
                    lines = file_info.readlines()
                    file_info.close()


                    username_list = []
                    password_list = []

                    for line in lines:
                        u_name, pswd = line.strip("\n").split(", ")
                        username_list.append(u_name)
                        password_list.append(pswd)
                    
                    new_user = input("New username: ")
                    while new_user in username_list:
                        print("\nUsers registered:")

                        for item in username_list:
                            print(item)
                
                        print("\nUser already exists! Try another username!\n")
                        new_user = input("New Username: ")
                    
                    new_pwd = input("Password: ")
                    confirm_pwd = input("Confirm the password: ")

                    while new_pwd != confirm_pwd:
                        confirm_pwd = input("Confirm the password: ")
                
                    print(f"\n{new_user} successfully registered!\n")
                    file_info = open('user.txt', 'a')
                    file_info.write("\n" + new_user + ", " + new_pwd)
                    file_info.close()
                            
                elif menu_admin == 't':
                    """
                    In this block the program will read the task from task.txt file and
                    print to the console the total number of tasks.
                    This is done in the following way:
                    - Read a line from the file.
                    - Split that line where there is comma and space.
                    - Then add all the tasks and print the results. 
                    """
                    count = 0

                    file_info = open('tasks.txt', 'r')
                    lines = file_info.readlines()

                    print("\nThe tasks are: \n")
                    print("\tNo.\tTask Assigned to\t\tTask Title")

                    for line in lines:
                        line_data = line.strip("\n").split(", ")
                        count += 1
                        print(f"\t{count} \t\t {line_data[0]} \t\t {line_data[1]}")

                    print(f"\nTotal number of tasks: {count}\n")

                    file_info.close()


                elif menu_admin == 'u':
                    """
                    In this block the program will read the task from user.txt file and
                    print to the console the total number of users.
                    This is done in the following way:
                    - Read a line from the file.
                    - Split that line where there is comma and space.
                    - Then add all the tasks and print the results. 
                    """
                    count_users = 0

                    file_info = open('user.txt', 'r')
                    lines = file_info.readlines()

                    print("\nThe users are: \n")
                    print("No.\tUsers \n")

                    for line in lines:
                        line_data = line.strip("\n").split(", ")
                        if line_data[0] != "admin":
                            print(f"{count_users + 1}\t{line_data[0]}")
                            count_users += 1
                    if count_users == 0:
                        print("There are no users.")
                    else:
                        print(f"{count_users + 1}\tadmin is a user")
                        print(f"\nTotal number of users (including admin): {count_users + 1}\n")

                    file_info.close()
                
                
                elif menu_admin == 'x':
                    print("Exiting admin menu....\n")
                    break

                else:
                    print("You have made a wrong choice, Please try again\n")

                    
    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        print("Adding a new task")
        username_task = input("Username whom the task is assigned to: ")
        title = input("Title of the task: ")
        descrip = input("Description of the task: ")
        due_date = input("Due date of the task (dd mon yyyy): ")
        current_date = date.today()
        complete_task = "No"

        file_info = open('tasks.txt', 'a')
        file_info.write("\n" + username_task + ", " + title + ", " + descrip + ", " + due_date + ", " + str(current_date) + ", " + complete_task)
        file_info.close()


    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        
        file_info = open('tasks.txt', 'r')
        lines = file_info.readlines()

        for pos, line in enumerate(lines):
            line_data = line.strip("\n").split(", ")
            output = f"\n———————————————————————————————————————————————Task {pos + 1} of {len(lines)} - {line_data[0]}———————————————————————————————————————————————\n"
            output += "\n"
            output += f"Task:\t\t\t {line_data[1]}\n"
            output += f"Assigned to:\t\t {line_data[0]}\n"
            output += f"Date assigned:\t\t {line_data[4]}\n"
            output += f"Due date:\t\t {line_data[3]}\n"
            output += f"Task Complete?\t\t {line_data[5]}\n"
            output += f"Task description:\n {line_data[2]}\n\n"
            output += "—————————————————————————————————————————————————————*****—————————————————————————————————————————————————————\n\n"
            print(output)
        file_info.close()


    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        val = False     # incase the user has no tasks assigned

        file_info = open('tasks.txt', 'r')
        lines = file_info.readlines()

        for line in lines:
            line_data = line.strip("\n").split(", ")
            if username == line_data[0]:
                val = True
                output = f"\n———————————————————————————————————————————————————{username} Task——————————————————————————————————————————————\n"
                output += "\n"
                output += f"Task:\t\t\t {line_data[1]}\n"
                output += f"Assigned to:\t\t {line_data[0]}\n"
                output += f"Date assigned:\t\t {line_data[4]}\n"
                output += f"Due date:\t\t {line_data[3]}\n"
                output += f"Task Complete?\t\t {line_data[5]}\n"
                output += f"Task description:\n {line_data[2]}\n\n"
                output += "—————————————————————————————————————————————————————*****—————————————————————————————————————————————————————\n\n"
                print(output)
        if val == False:
            print(f"\n{username}, you have no tasks assigned to you!\n")
        file_info.close()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")