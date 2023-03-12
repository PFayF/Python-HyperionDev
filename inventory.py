'''
This Python program will read from the text file inventory.txt and
perform the following on the data, to prepare for presentation to the
managers:
There is a class named Shoe with the following attributes:
country, code, product, cost and quantity.
Inside this class, the following methods are defined:
get_cost - Returns the cost of the shoes.
get_quantity - Returns the quantity of the shoes.
__str__ - This method returns a string representation of a class.
Outside this class there is a variable with an empty list. This variable
will be used to store a list of shoes objects.
The following functions are defined outside the class:
read_shoes_data - Reads the shoe data from the the text file, "inventory.txt"
capture_shoes - Accepts shoe data from the user and saves it to the list of shoes
view_all - Displays shoe data using Python's tabulate module
update_file - Updates the shoe data in the file
re_stock - Finds the shoe object with the lowest quantity and accepts the quantity 
            to be increased from the user and updates this data to the file
search_shoe - Searches for a shoe using it's code
value_per_item - Calculates the total value for each item
highest_qty - Find the shoe with the highest quantity and print this shoe as being on sale.
'''

from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"Country: {self.country}\n"\
                f"Code: {self.code}\n"\
                f"Product: {self.product}\n"\
                f"Cost: {self.cost}\n"\
                f"Quantity: {self.quantity}"\
                f""



    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost



    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    

    def prod_list(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]

    
    
    def to_file(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as file_info:
            lines = file_info.readlines()
            for i, line in enumerate(lines):
                if i > 0:
                    country_1, code_1, product_1, cost_1, quantity_1  = line.strip("\n").split(",")
                    shoe_object = Shoe(country_1, code_1, product_1, float(cost_1), int(quantity_1))
                    shoe_list.append(shoe_object)
    except FileNotFoundError as error:
        print(f"The file that you are trying to open does not exist!\n")
        print(error)
    

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    error1_found = True
    error2_found = True
    print("\nPlease enter shoe data!")
    country = input("\nPlease enter the country: ")
    code = input("\nPlease enter the code: ")
    product = input("\nPlease enter the product: ")
    while error1_found:
        try:
            cost = float(input("\nPlease enter the cost: "))
            error1_found = False
        except:
            print("This is not a number. Please try again!")
            error1_found = True
    while error2_found:
        try:
            quantity = int(input("\nPlease enter the quantity: "))
            error2_found = False
        except:
            print("This is not a number. Please try again!")
            error2_found = True
           
    shoe_obj = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_obj)
    update_file()



def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''
    data_list = []
    for item in shoe_list:
        data_list.append(item.prod_list())
    print(tabulate(data_list, headers = ["Country", "Code", "Product", "Cost", "Quantity"], tablefmt = "fancy_grid"))


def update_file():
    file_update = open('inventory.txt', 'w')
    file_update.write("Country,Code,Product,Cost,Quantity")
    for shoe in shoe_list:
        
        file_update.write(f"\n{shoe.to_file()}")
    print("File updated!\n")
    file_update.close()



def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest_qty = []
    min_qty = 10000
    min_code = ""
    increase_val = 0

    for index, item in enumerate(shoe_list):
        list1 = item.prod_list()
        if list1[4]<= min_qty:
            min_qty = list1[4]
            min_code = list1[1]
            min_index = index
            lowest_qty = list1
    
    print("The shoe with the lowest quantity is:")
    print(lowest_qty)
    user_ans = input(("\nWould you like to increase the quantity? [y/n]")).lower()
    error3_found = True
    if user_ans == "y":
        while error3_found:
            try:
                increase_val = int(input("\nEnter the quantity to increase by: "))
                error3_found = False
            except:
                print("This is not a number. Please try again!")
                error3_found = True
        for index, item in enumerate(shoe_list):
            if min_code == shoe_list[index].code:
                shoe_list[index].quantity += increase_val
                list1 = item.prod_list()
                lowest_qty = list1

        print(f"Quantity changed to...\n")
        print(f"{list1}\n")
        update_file()
        
    elif user_ans == "n":
        print("Not increasing the lowest quantity at this time!\n")
    else:
        print("Invalid input!\n")


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    val_found = []
    print("List of shoes\n")
    for item in shoe_list:
        list1 = item.prod_list()
        print(f"{list1[1]}\n")
    code_shoe = input("Enter shoe code: ")
    code_shoe = code_shoe.upper()
    for item in shoe_list:
        list1 = item.prod_list()
        to_check = list1[1]
        if to_check == code_shoe:
            val_found = list1
            
    return val_found


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    total_value_list2 = []
    for index, item in enumerate(shoe_list):
        total_value_list = []
        total_value = item.get_cost() * item.get_quantity()
        #total_value = shoe_list[index].cost * shoe_list[index].quantity
        total_value_list.append(shoe_list[index].country)
        total_value_list.append(shoe_list[index].code)
        total_value_list.append(shoe_list[index].product)
        total_value_list.append(shoe_list[index].cost)
        total_value_list.append(shoe_list[index].quantity)
        total_value_list.append(total_value)
        total_value_list2.append(total_value_list)
    print(tabulate(total_value_list2, headers = ["Country", "Code", "Product", "Cost", "Quantity", "Total Value"], tablefmt = "fancy_grid"))


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    sale_info = []
    max_qty = 0
    max_code = ""
    for index, item in enumerate(shoe_list):
        list1 = item.prod_list()
        if list1[4]> max_qty:
            max_qty = list1[4]
            max_code = list1[1]
            sale_info = list1
    print(f"\n{sale_info} has the highest quantity!\n")
    print(f"****{sale_info[2]} is on SALE!***")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()

while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''\n***************Main Menu***************\n
    Please select one of the following options:
    a - Add shoe data
    v - View shoe data
    r - Restock lowest quantity
    s - Search for a shoe using it's code
    t - Display total value per item
    h - Display shoe on sale
    e - Exit
    : ''').lower()

    if menu == 'a':
        capture_shoes()
        print("Shoe added!\n")
    
    elif menu == 'v':
        view_all()

    elif menu == 'r':
        re_stock()

    elif menu == 's':
        val = []
        val = search_shoe()
        if val:
            print("The information found is:\n")
            print(val)
        else:
            print("\nItem not found!")

    elif menu == 't':
        value_per_item()

    elif menu == 'h':
        highest_qty()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")