import random
game_grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0]
]
#game_grid = [[0 for _ in range(4)] for _ in range(4)]             
def get_userinput():
    try:
        inpuT = input("Please use w,a,s,d to play the game")
        if inpuT == "w" or inpuT == "a" or inpuT == "s" or inpuT == "d":
            return inpuT
        else:
            print("input is not valid")
            get_userinput()
    except ValueError:
        print("input is not valid")
        get_userinput()



def print_game():
    for row in game_grid:
        print(row)

def random_spawn():
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if game_grid[x][y] == 0:
            game_grid[x][y] = 2
            break
        else:
            continue

def move_up():
    for row in range(len(game_grid) - 1, 0, -1):
        for col in range(len(game_grid[0])):
            if game_grid[(row)-1][col] == 0:
                brow = row

                while brow < len(game_grid):
                    if game_grid[brow][col] != 0:
                        game_grid[brow-1][col] = game_grid[brow][col]
                        game_grid[brow][col] = 0
                    brow += 1
                    

            elif game_grid[row][col] == game_grid[(row)-1][col]:
                game_grid[row-1][col] *= 2
                game_grid[row][col] = 0
                brow = row + 1
                while brow < len(game_grid):
                    if game_grid[brow][col] != 0:
                        game_grid[brow-1][col] = game_grid[brow][col]
                        game_grid[brow][col] = 0
                    brow += 1


"""
                for brow in range(row,len(game_grid)-1):
                    game_grid[brow-1][col] = game_grid[brow][col]
                    game_grid[brow][col] = 0
"""    
    
def main():
    while True:
        random_spawn()
        print_game()
        
        match (get_userinput()):
            case ("w"):
                move_up()
            #case (_):
                # comment:       


if __name__ == "__main__":
    main()

    
    
   
        
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
    start: len(array) - 1 (last index).
        stop: -1 (one less than the first index, because range is exclusive at the stop).
        step: -1 (to move backwards).
"""