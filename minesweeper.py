'''
This Python program takes a grid of # and -, where each hash (#) represents a
mine and each dash (-) represents a mine-free spot.
The program returns a grid, where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. (horizontally, vertically, and
diagonally)

'''

# The NW_position function returns the row and column position at the NW position in the grid.
def NW_position(current_row, current_col):
    return current_row - 1, current_col - 1


# The N_position function returns the row and column position at the N position in the grid.
def N_position(current_row, current_col):
    return current_row - 1, current_col


# The NE_position function returns the row and column position at the North East position in the grid.
def NE_position(current_row, current_col):
    return current_row - 1, current_col + 1


# The E_position function returns the row and column position at the East position in the grid.
def E_position(current_row, current_col):
    return current_row, current_col + 1


# The SE_position function returns the row and column position at the South East position in the grid.
def SE_position(current_row, current_col):
    return current_row + 1, current_col + 1


# The S_position function returns the row and column position at the South position in the grid.
def S_position(current_row, current_col):
    return current_row + 1, current_col


# The SW_position function returns the row and column position at the South West position in the grid.
def SW_position(current_row, current_col):
    return current_row + 1, current_col - 1


# The W_position function returns the row and column position at the West position in the grid.
def W_position(current_row, current_col):
    return current_row, current_col - 1


# The check_for_a_mine function checks that the rows and columns are within the length of the grid 
# and checks for a mine and if a mine is found, it returns the count
def check_for_a_mine(check_row, check_col):
    count = 0
    if check_row >= row_start and check_row <= row_end and check_col >= col_start and check_col <= col_end:         
        if grid[check_row][check_col] == "#":
            count += 1
    return count


grid = [["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"]]

completed_grid = []

row_size = len(grid)
col_size = len(grid[0])

row_start = 0
col_start = 0

row_end = row_size - 1
col_end = col_size - 1


print("\nWelcome to Minesweeper!\n")
print("Input Grid\n")
print(grid)


for i, row in enumerate(grid):  # for each row
    completed_row = []
    for j, col in enumerate(row):   # for each column
        mine_counter = 0
        
        if grid[i][j] == "-":
            if i >= row_start and i <= row_end and j >= col_start and j <= col_end: #checks that the row and column are within the grid length
                
                #check NW position
                counter = 0
                try:
                    row_to_check, col_to_check = NW_position(i, j)
                except:
                    print("Index out of bounds!")
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1

                #check N position
                try:
                    row_to_check, col_to_check = N_position(i, j)
                except:
                    print("Index out of bounds!")
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1

                #check NE position
                try:
                    row_to_check, col_to_check = NE_position(i, j)
                except:
                    print("Index out of bounds!")    
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1

                #check E position
                try:
                    row_to_check, col_to_check = E_position(i, j)
                except:
                    print("Index out of bounds!")
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1
                
                #check SE position
                try:
                    row_to_check, col_to_check = SE_position(i, j)
                except:
                    print("Index out of bounds!")
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1
                
                #check S position
                row_to_check, col_to_check = S_position(i, j)
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1

                #check SW position
                try:
                    row_to_check, col_to_check = SW_position(i, j)
                except:
                    print("Index out of bounds!")
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1

                #check W position
                try:
                    row_to_check, col_to_check = W_position(i, j)
                except:
                    print("Index out of bounds!")
                counter = check_for_a_mine(row_to_check, col_to_check)
                if counter:
                    mine_counter += 1
            
        else:
            mine_counter = "#"

        completed_row.append(mine_counter)
        
    completed_grid.append(completed_row)
print("\n\nOutput Grid\n")
print(completed_grid)