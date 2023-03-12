"""
Capstone Project III

This Python program is a modificaton of the Capstone II project.
This program is used to help a small business manage tasks assigned to each member of the team.
Functions are used to improve the modularity of the code. 

The funtions used are listed below:
reg_user - is called when the user selects 'r' to register a user.
add_task - is called when a user selects 'a' to add a new task.
view_all - is called when users type 'va' to view all the tasks listed in 'tasks.txt'.
view_mine - is called when users type 'vm' to view all the tasks that have been assigned to them.
generate_task_report is called when the user selects 'gr' and this generates a report of the tasks 
that is stored in the 'task_overview.txt' file.
generate_user_report generates a report of the tasks per user and 
this data is stored in 'user_overview.txt' file.
display_task_statistics - is called when users type 'ds' to display 
task statistics from the generated 'task_overview.txt' file.
display_user_statistics - is called to display task per user statistics from 
the generated 'user_overview.txt' file.
file_read_handling - is called when working with files.
mark_completed - is called when a tasks listed in 'tasks.txt' is to be marked as completed with a "Yes".
dict_total_users - is called to store all the users in user.txt in a dictionary.
edit_user - is called when the user assigned a task listed in 'tasks.txt' is to be edited 
to a new user from the users listed in 'user.txt'.
edit_due_date - is called when the user assigned a task due date listed in 'tasks.txt' 
that is not complete, is to be edited to a new due date entered.
task_edit - is called to allow the user to select what they want to edit for a selected task.
choice_task_function - is called when the correct function needs to be called based on the user's choice.
view_my_tasks - is called when the user would like to edit or mark a specified task as complete.
total_tasks - is called when a user selects 't' view all tasks.
total_users - is called when a user selects 'u' to view all the users in 'user.txt'.

The text files used are listed below:
This program works with four text files, user.txt, tasks.txt, task_overview.txt and user_overview.txt.
tasks.txt stores a list of all the tasks that the team is working on.
user.txt stores the username and password for each user that has permission to use this program.
task_overview.txt stores a list of the statistics regarding the tasks in tasks.txt.
user_overview.txt stoes a list of the statistics regarding tasks in tasks.txt
per user in user.txt.
"""



#=====importing libraries===========
'''This is the section to import libraries'''
from datetime import date
from datetime import datetime



#The function, file_info deals with working with files.
def file_read_handling(file_name, file_mode):
    """
    This block opens a specified file with the specified mode and reads 
    lines from the file and returns the list.
    """
    file_info = open(file_name, file_mode)
    lines_list = file_info.readlines()
    file_info.close()
    return lines_list



# The function, reg_user, is called when a user selects 'rn' to register a new user.
def reg_user():
    """ Only the admin is allowed to register users. 
    In this block, the following steps are carried out:
    - Check if the entered username already exists.
    - Check if the new password and confirmed password are the same.
    - If they are the same, add them to the user.txt file,
    - Otherwise the user is presented with a relevant message.
    """
    
    lines = file_read_handling('user.txt', 'r')

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



# The function, add_task, is called when a user selects 'a' to add a new task.
def add_task():
    '''In this block, a user is allowed to add a new task to task.txt file
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
    


#The function, view_all is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’.
def view_all():
    '''In this block you the program will read the task from task.txt file and
        print to the console in the format of Output 2 in the task PDF
        (i.e. include spacing and labelling)
        The following steps are carried out:        
        - Read a line from the file.
        - Split that line where there is comma and space.
        - Then print the results in the format shown in the Output 2 
        - It is much easier to read a file using a for loop.'''
    
   
    lines = file_read_handling('tasks.txt', 'r')


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



#The function, mark_completed is called when a task listed in ‘tasks.txt’ is to be marked 
# as completed with a "Yes".
def mark_completed(task_number):
    """
    In this block, for the task selected, if the task is not completed, the task will be assigned "Yes"
    to mark as completed.
    """   
    lines = file_read_handling('tasks.txt', 'r')

    temp_file_info = open('tasks.txt', 'w') 

    for pos, line in enumerate(lines):
        line_data = line.strip("\n").split(", ")
        if username == line_data[0] and task_number - 1 == pos:
            if line_data[5] == "No":
                line_data[5] = "Yes"    #Successfully changed {line_data[5]}
                print(f"Successfully marked task as completed!")
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
                temp_file_info.write(line_data[0] + ", " + line_data[1] + ", " + line_data[2] + ", " + line_data[3] + ", " + line_data[4] + ", " + line_data[5] + "\n")
            else:
                print("Task already completed!")
        else:
            temp_file_info.write(line_data[0] + ", " + line_data[1] + ", " + line_data[2] + ", " + line_data[3] + ", " + line_data[4] + ", " + line_data[5] + "\n")

    temp_file_info.close()



# The function, dict_total_users is used to store all the users in user.txt in a dictionary.
def dict_total_users():
    """
    In this block the program will read the task from user.txt file and
    store the users in a dictionary.
    This is done in the following way:
    - Read a line from the file.
    - Split that line where there is comma and space.
    - Then add a number for a key and the username for the value. 
    """
    count_users = 1
    dict_users = {}
    line_data = []
   
    lines = file_read_handling('user.txt', 'r')

    print("\nThe users are: \n")
    print("\tNo.\tUsers \n")

    for line in lines:
        line_data = line.strip("\n").split(", ")
        dict_users.update({count_users: line_data[0]})
        count_users += 1
    

    return dict_users



#The function, edit_user is called when the user assigned a task listed in ‘tasks.txt’ 
# is to be edited to a new user from the users listed in 'user.txt'.
def edit_user(task_number):
    """
    In this block, the user assigned a task in 'tasks.txt' can be edited to a different user.
    This user is chosen from the 'user.txt' file.
    """

    new_user_num = 0

    error_input = True

    lines = file_read_handling('tasks.txt', 'r')

    changed_username = False
    print("\n****Editing user****\n")    
    print(f"\nCurrent user: {username}")
    dict_users = dict_total_users()
    for item in dict_users:
        print(f"\t{item}:\t{dict_users[item]}\n")
    
    while error_input:
        while not new_user_num in range(1, len(dict_users) + 1):
            try:
                new_user_num = int(input("\nPlease enter the number to select the respective user: "))
                print("Invalid choice. Please try again!")

            except:
                print("This is not a number. Please try again!")
                error_input = True
        error_input = False

    popped = dict_users.get(new_user_num)
    
    temp_file_info = open('tasks.txt', 'w')

    for index_no, line in enumerate(lines):
        line_data = line.strip("\n").split(", ")
        
        if line_data[5] == "No" and index_no + 1 == task_number:
            if line_data[0] == popped:
                changed_username = False
                print(f"Trying to change {line_data[0]} to {popped}!")
            else:
                line_data[0] = popped
                changed_username = True
                temp_file_info.write(line_data[0] + ", " + line_data[1] + ", " + line_data[2] + ", " + line_data[3] + ", " + line_data[4] + ", " + line_data[5] + "\n")
        else:
            temp_file_info.write(line_data[0] + ", " + line_data[1] + ", " + line_data[2] + ", " + line_data[3] + ", " + line_data[4] + ", " + line_data[5] + "\n")
            
    temp_file_info.close()
    
    if changed_username == True:
        print(f"\nSuccesfully changed the user for task assigned from {username} to {popped}!")
    else:
        print("No changes made!")



#The function, edit_due_date is called when the user assigned a task due date listed in ‘tasks.txt’ 
#that is not complete, is to be edited to a new due date entered.
def edit_due_date(task_number):
    """
    In this block, if the task is not completed, the due date assigned to a task 
    can be edited to a new date entered.
    """
    print("\n****Editing due date****\n")    
    lines = file_read_handling('tasks.txt', 'r')
    changed_due_date = False
    date_correct = True
    date_format = "%Y-%m-%d"
    day_error = True
    month1_error = True
    month2_error = True
    year1_error = True
    year2_error = True

    while date_correct:
        new_due_date = print("\nPlease enter the new due date!")
        while day_error:
            try:
                due_day = int(input("Please enter the day it's due: "))
                while not (due_day >= 1 and due_day <= 31):
                    print("There are upto 31 days in a month!")
                    due_day = int(input("Please re-enter the day it's due: "))
                day_error = False
            except:
                print("This is not a number. Please try again!")
                day_error = True

        while month1_error:
            try:
                due_month = int(input("Please enter the new month it's due: "))
                month1_error = False
            except:
                print("This is not a number. Please try again!")
                month1_error = True

        while month2_error:
            try:
                while not (due_month <= 12 and due_month >= 1):
                    print("There are upto 12 months in a year!")
                    due_month = int(input("Please re-enter the month it's due: "))
                month2_error = False
            except:
                print("This is not a number. Please try again!")
                month2_error = True

        while year1_error:
            try:
                due_year = int(input("Please enter the year it's due (example: 2023): "))
                year1_error = False
            except:
                print("This is not a number. Please try again!")
                year1_error = True

        year = date.today().strftime("%Y")
        while year2_error:
            try:
                while not (due_year >= int(year)):
                    print("The due date should be this year or in the future!")
                    due_year = int(input("Please re-enter the year it's due (example: 2023): "))
                year2_error = False
            except:
                print("This is not a number. Please try again!")
                year2_error = True


        new_date_temp = datetime(due_year, due_month, due_day)
        
        new_due_date = datetime.strftime(new_date_temp, date_format)
        
        check_date = datetime.strptime(new_due_date, "%Y-%m-%d")
        
        if check_date < datetime.now():
            print("\nInvalid date! Date in the past! Please try again!")
            date_correct = True
        else:
            date_correct = False

    

    temp_file_info = open('tasks.txt', 'w')

    for index_no, line in enumerate(lines):
        line_data = line.strip("\n").split(", ")
    
        popped = line_data[3]
        if line_data[5] == "No" and index_no + 1 == task_number:
            if line_data[3] == new_due_date:
                changed_due_date = False
                print(f"Trying to change {line_data[3]} to {new_due_date}!")
            else:
                line_data[3] = new_due_date
                changed_due_date = True
                temp_file_info.write(line_data[0] + ", " + line_data[1] + ", " + line_data[2] + ", " + line_data[3] + ", " + line_data[4] + ", " + line_data[5] + "\n")
        else:
            temp_file_info.write(line_data[0] + ", " + line_data[1] + ", " + line_data[2] + ", " + line_data[3] + ", " + line_data[4] + ", " + line_data[5] + "\n")
            
    temp_file_info.close()
    if changed_due_date == True:
        print(f"\nSuccesfully changed the due date for task assigned for {username} from {popped} to {new_due_date}!\n\n")
    else:
        print("No changes made!")



#The function, task_edit allows the user to select what they want to do with the selected task.
def task_edit(task_number):
    """
    In this block, the user selects if they would like to edit the username, the due date of a task 
    or both in the 'tasks.txt' file.
    """
    test_val = True
       
    while test_val:
        print("Would you like to edit the username or the due date or both?")
        user_or_date = input("Please select u - username, d - due date or b - both: ").lower()
        if user_or_date == "u":
            edit_user(task_number)
            generate_task_report()  #updating task report after changes
            generate_user_report()  #updating user report after changes
            test_val = False
        
        elif user_or_date == "d":
            edit_due_date(task_number)
            generate_task_report()  #updating task report after changes
            generate_user_report()  #updating user report after changes
            test_val = False

        elif user_or_date == "b":
            edit_user(task_number)
            edit_due_date(task_number)
            generate_task_report()  #updating task report after changes
            generate_user_report()  #updating user report after changes
            test_val = False

        else:
            print("Invalid choice. Please try again!")
            test_val = True



#The function, choice_task_function calls the correct function based on the user's choice.
def choice_task_funct(choice_task, task_number):
    """
    In this block, the correct function is called based on whether the user would like to
    mark the task specified in task number as completed or whether they would like to edit 
    something in the specified task number.
    """
    if choice_task == "m":
        mark_completed(task_number)
        generate_task_report()  #updating task report after changes
        generate_user_report()  #updating user report after changes
    elif choice_task == "e":
        task_edit(task_number)
    else:
        print("Invalid choice!")



#The function, view_my_tasks works on the tasks that the user to edit or mark as complete.
def view_my_tasks(task_number):    
    """
    In this block, the chosen task is displayed and also the user is asked to choose if they would 
    like to mark the selected task as completed with a "Yes" in 'tasks.txt' or if they 
    would like to edit the specified task.
    """

    lines = file_read_handling('tasks.txt', 'r')

    for pos, line in enumerate(lines):
        line_data = line.strip("\n").split(", ")
        if username == line_data[0]:
            if task_number == pos + 1:
                output = f"\n———————————————————————————————————————————————————{username} Task——————————————————————————————————————————————\n"
                output += "\n"
                output += f"Task{pos + 1}:\t\t\t{line_data[1]}\n"
                output += f"Assigned to:\t\t {line_data[0]}\n"
                output += f"Date assigned:\t\t {line_data[4]}\n"
                output += f"Due date:\t\t {line_data[3]}\n"
                output += f"Task Complete?\t\t {line_data[5]}\n"
                output += f"Task description:\n {line_data[2]}\n\n"
                output += "—————————————————————————————————————————————————————*****—————————————————————————————————————————————————————\n\n"
                print(output)
                print("Please select what you would like to do with the task!")
                choice_task = input("m - Mark as complete or e - Edit: ").lower()
                return(choice_task, task_number)
                


#The function, view_mine is called when users type ‘vm’ to view all the tasks that have been assigned to them
def view_mine():
    '''In this block the code reads the task from task.txt file and
        prints to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
        The following steps are carried out:
        - Read a line from the file
        - Split the line where there is comma and space.
        - Check if the username of the person logged in is the same as the username read from the file.
        - If they are the same print it in the format of Output 2 in the task PDF'''

    val = False     # incase the user has no tasks assigned
    error1_found = True

    task_num = -1
    tasks_nums_list = []
    yes_list = []

    
    lines = file_read_handling('tasks.txt', 'r')

    print(f"\n———————————————————————————————————————————————{username} Task——————————————————————————————————————————")

    for pos, line in enumerate(lines):
        line_data = line.strip("\n").split(", ")
        if username == line_data[0]:
            val = True
            output = "\n"
            output += f"Task number: {pos + 1}:\t{line_data[1]} assigned to {line_data[0]}. Task completed?: {line_data[5]}"
            print(output)
            tasks_nums_list.append(pos + 1)
            if line_data[5] == "Yes":
                yes_list.append(pos + 1)
        
    if val == False:
        print(f"\n{username}, you have no tasks assigned to you!\n")
    
    print(f"Task numbers for {username}: {tasks_nums_list}")
    print(f"Task numbers completed: {yes_list}")
    
    lists_subtracted = [item for item in tasks_nums_list if item not in yes_list]
    if task_num in yes_list:
        print("This task is already completed!")
    elif len(tasks_nums_list) == 0 or len(lists_subtracted) == 0:
        print("There are no tasks assigned to you!")
    else:
        while error1_found:
            try:
                task_num = int(input(f"Please enter the task number from {lists_subtracted} you would like to edit or mark as complete: "))
                error1_found = False
                if not task_num in lists_subtracted:
                    print(f"{task_num} not in {lists_subtracted}. Please try again!")
                    error1_found = True
                
            except ValueError:
                print("That is not a number. Please try again!")
                error1_found = True


    return task_num
    


# The function, total_tasks is called when a user selects 't' view all tasks.
def total_tasks():
    """
    In this block the program will read the task from task.txt file and
    print to the console the total number of tasks.
    This is done in the following way:
    - Read a line from the file.
    - Split that line where there is comma and space.
    - Then add all the tasks and print the results. 
    """
    count = 0
 
    lines = file_read_handling('tasks.txt', 'r')
    
    print("\nThe tasks are: \n")
    print("\tNo.\tTask Assigned to\t\tTask Title")

    for line in lines:
        line_data = line.strip("\n").split(", ")
        count += 1
        print(f"\t{count} \t\t {line_data[0]} \t\t {line_data[1]}")

    print(f"\nTotal number of tasks: {count}\n")



# The function, total_users is called when a user selects 'u' to view all the users in user.txt.
def total_users():
    """
    In this block the program will read the task from user.txt file and
    print to the console the total number of users.
    This is done in the following way:
    - Read a line from the file.
    - Split that line where there is comma and space.
    - Then add all the tasks and print the results. 
    """
    count_users = 0

    lines = file_read_handling('user.txt', 'r')
    
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



#The function, generate_task_report generates a report of the tasks 
#and this data is stored in 'task_overview.txt' file.
def generate_task_report():
    """
    When the user chooses to generate reports, a text file, called
    task_overview.txt should be generated. The text file
    should be able to output data in a user-friendly, easy to read manner.
    task_overview.txt should contain:
    The total number of tasks that have been generated and
    tracked using the task_manager.py.
    The total number of completed tasks.
    The total number of uncompleted tasks.
    The total number of tasks that have not been completed and
    that are overdue.
    The percentage of tasks that are incomplete.
    The percentage of tasks that are overdue.
    This data is stored in task_overview.txt separated by a comma and space.
    """
    count_completed_tasks = 0
    count_incomplete_tasks = 0
    overdue_tasks = 0
    no_overdue_tasks = 0
    
    todays_date = datetime.strftime(datetime.now(), "%Y-%m-%d")

    file_info = open('task_overview.txt', 'w+')

    lines = file_read_handling('tasks.txt', 'r')
    num_tasks = len(lines)
 
    for line in lines:
        line_data = line.strip("\n").split(", ")

        if line_data[5] == "Yes":
            count_completed_tasks += 1
        else:
            count_incomplete_tasks += 1
            check_date = line_data[3]
            
            if todays_date > check_date:
                overdue_tasks += 1
            else:
                no_overdue_tasks += 1
    
    try:
        percent_incomplete_tasks = round(count_incomplete_tasks/num_tasks * 100, 2)
        percent_overdue_tasks = round(overdue_tasks/num_tasks * 100, 2)
    except:
        percent_incomplete_tasks = 0
        percent_overdue_tasks = 0

    file_info.write(str(num_tasks) + ", " + str(count_completed_tasks) + ", " + str(count_incomplete_tasks) + ", " + str(overdue_tasks) + ", " + str(no_overdue_tasks) + ", " + str(percent_incomplete_tasks) + ", " + str(percent_overdue_tasks))
    
    file_info.close()



#The function, generate_user_report generates a report of the tasks per user
#and this data is stored in 'user_overview.txt' file.
def generate_user_report():
    """
    When the user chooses to generate reports, a text file, called
    user_overview.txt should be generated. The text file
    should be able to output data in a user-friendly, easy to read manner.
    user_overview.txt should contain:
    The total number of users registered with task_manager.py.
    The total number of tasks that have been generated and
    tracked using task_manager.py.
    For each user also describe:
    The total number of tasks assigned to that user.
    The percentage of the total number of tasks that have
    been assigned to that user.
    The percentage of the tasks assigned to that user that
    have been completed.
    The percentage of the tasks assigned to that user that
    must still be completed.
    The percentage of the tasks assigned to that user that
    have not yet been completed and are overdue.
    """
    dict_users_tasks = {}
    todays_date = datetime.strftime(datetime.now(), "%Y-%m-%d")
    
    file_info = open('user_overview.txt', 'w+')

    lines1 = file_read_handling('tasks.txt', 'r')
    lines2 = file_read_handling('user.txt', 'r')

    num_tasks = len(lines1)
    num_users = len(lines2)

    for line2 in lines2:
        count_tasks_per_user = 0
        count_completed_user = 0
        count_incomplete_user = 0
        overdue_tasks_user = 0

        line_data2 = line2.strip("\n").split(", ")
        for line1 in lines1:
            line_data1 = line1.strip("\n").split(", ")

            if line_data2[0] == line_data1[0]:
                count_tasks_per_user += 1
                if line_data1[5] == "Yes":
                    count_completed_user += 1
                else:
                    count_incomplete_user += 1
                check_date = line_data1[3]
                
                if todays_date > check_date:
                    overdue_tasks_user += 1
            
          
        percent_tasks_per_user = round(count_tasks_per_user/num_tasks * 100, 2)
        try:
            percent_tasks_completed_user = round(count_completed_user/count_tasks_per_user * 100, 2)
            percent_tasks_incomplete_user = round(count_incomplete_user/count_tasks_per_user * 100, 2)
            percent_tasks_incomplete_overdue_user = round(overdue_tasks_user/count_tasks_per_user * 100, 2)
        except:
            percent_tasks_completed_user = 0
            percent_tasks_incomplete_user = 0
            percent_tasks_incomplete_overdue_user = 0

        
        dict_users_tasks.update({"user": line_data2[0]})
        dict_users_tasks["tasks_per_user"] = count_tasks_per_user
        dict_users_tasks["percent_tasks_per_user"] = percent_tasks_per_user
        dict_users_tasks["percent_tasks_completed_user"] = percent_tasks_completed_user
        dict_users_tasks["percent_tasks_incomplete_user"] = percent_tasks_incomplete_user
        dict_users_tasks["percent_tasks_incomplete_overdue_user"] = percent_tasks_incomplete_overdue_user

        file_info.write(str(num_users) + ", " + str(num_tasks) + ", " + line_data2[0] + ", " + str(count_tasks_per_user) + ", " + str(percent_tasks_per_user) + ", " + str(percent_tasks_completed_user) + ", " + str(percent_tasks_incomplete_user) + ", " + str(percent_tasks_incomplete_overdue_user) + "\n")
    
    print("\nSuccessfully generated reports to two files, namely 'task_overview.txt' and 'user_overview.txt'.\n")

    file_info.close()
    
   

#The function, display_task_statistics displays task statistics from the generated 'task_overview.txt' file.
def display_task_statistics():
    """
    In this block, the statistics are displayed so that
    the reports generated are read from task_overview.txt 
    and displayed on the screen in a user-friendly manner.
    If the text file does not exist (because the user hasn't selected to generate
    them yet), first call the code to generate the text files.
    """
    file_error = True
    while file_error:
        try: # incase file was not generated before getting called
            file_info = open('task_overview.txt', 'r')
            lines = file_info.readlines()
            file_error = False

        except FileNotFoundError:
            generate_task_report()
            generate_user_report()
            file_error = True
    
    
    for line in lines:
        line_data = line.strip("\n").split(", ")

        output = f"\n———————————————————————————————————————————————————Task Report——————————————————————————————————————————————\n"
        output += "\n"
        output += f"Total tasks generated and tracked: {line_data[0]}\n"
        output += f"Total tasks completed by: {line_data[1]}\n"
        output += f"Total uncompleted tasks: {line_data[2]}\n"
        output += f"Total incomplete tasks that are overdue: {line_data[3]}\n"
        output += f"Total incomplete tasks that are not overdue: {line_data[4]}\n"
        output += f"Percentage of tasks that are incomplete: {line_data[5]}%\n"
        output += f"Percentage of tasks that are overdue: {line_data[6]}%\n\n"
        output += "—————————————————————————————————————————————————————*****—————————————————————————————————————————————————————\n\n"
        print(output)
    


#The function, display_user_statistics displays task per user statistics from the generated 'user_overview.txt' file.
def display_user_statistics():
    """
    In this block, the statistics are displayed so that
    the reports generated are read from user_overview.txt and 
    displayed on the screen in a user-friendly manner.
    If the text file does not exist (because the user hasn't selected to generate
    them yet), first call the code to generate the text files.
    """
    file_error = True
    while file_error:
        try: # incase file was not generated before getting called
            file_info = open('user_overview.txt', 'r')
            lines = file_info.readlines()
            file_error = False

        except FileNotFoundError:
            generate_task_report()  #updating task report after changes
            generate_user_report()  #updating user report after changes
            file_error = True


    for line in lines:
        line_data = line.strip("\n").split(", ")

        output = f"\n———————————————————————————————————————————————————{line_data[2]} Report——————————————————————————————————————————————\n"
        output += "\n"
        output += f"Total number of users: {line_data[0]}\n"
        output += f"Total tasks generated and tracked: {line_data[1]}\n"
        output += f"Name of the user: {line_data[2]}\n"
        output += f"Total tasks for {line_data[2]}: {line_data[3]}\n"
        output += f"Percentage of tasks for {line_data[2]}: {line_data[4]}%\n"
        output += f"Percentage of completed tasks for {line_data[2]}: {line_data[5]}%\n"
        output += f"Percentage of incomplete tasks for {line_data[2]}: {line_data[6]}%\n"
        output += f"Percentage of incomplete overdue tasks for {line_data[2]}: {line_data[7]}%\n\n"
        output += "—————————————————————————————————————————————————————*****—————————————————————————————————————————————————————\n\n"
        print(output)




#====Login Section====
'''This code allows a user to login.
    - Firstly, usernames and password are read from the user.txt file.
    - Lists are used to store a list of usernames and passwords from the file.
    - A while loop is used to validate the username and password.
'''

lines = file_read_handling('user.txt', 'r')


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


while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input(''' ************Main Menu************
Please select one of the following options:
r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Only the admin is allowed to register users. 
            In this block the code adds a new user to the user.txt file
            - The following steps are carried out:
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
                rn - Register a new user
                t - View total number of tasks
                u - View total number of users
                x - Exit from the admin menu
                : ''').lower()

                if menu_admin == 'rn':
                    # The function, reg_user is called when a user selects 'rn' to register a new user
                    reg_user()
                    generate_user_report()  #updating user report after changes
                            
                elif menu_admin == 't':
                    # The function, total_tasks is called when a user selects 't' to view all the tasks in task.txt
                    total_tasks()
                            
                elif menu_admin == 'u':
                    # The function, total_users is called when a user selects 'u' to view all the users in user.txt
                    total_users()
               
                elif menu_admin == 'x':
                    print("Exiting admin menu....\n")
                    break

                else:
                    print("You have made a wrong choice, Please try again\n")

                    
    elif menu == 'a':
        # The function, add_task, is called when a user selects 'a' to add a new task
        add_task()
        generate_task_report()  #updating task report after changes
        generate_user_report()  #updating user report after changes
        
    elif menu == 'va':
        #The function, view_all is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’
        view_all()

    elif menu == 'vm':
        #The function, view_mine is called when users type 'vm' to view all the tasks that have been assigned to them.
        task_no = view_mine()
        choice_task, task_number = view_my_tasks(task_no)
        choice_task_funct(choice_task, task_number)

    elif menu == 'gr':
        #The functions, generate_task_report and generate_user_report are called when users type ‘gr’ to generate a report on all the tasks listed in ‘tasks.txt’
        generate_task_report()  #updating task report after changes
        generate_user_report()  #updating user report after changes

    elif menu == 'ds':
        #The functions, display_task_statistics and display_user_statistics are called when users type ‘ds’ to display a report on all the tasks listed in ‘tasks.txt’
        display_task_statistics()
        display_user_statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")