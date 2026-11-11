## Written by: Evan Ridinger ##
## Game Board Code for the Tetris Engine ##

class GameBoard:

    ## Initialize the Game Board with a Given Width and Height ##
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    ## Check If a Cell is Empty (If a Cell is Empty, return true(0) else return false(1)) ##
    def is_empty(self, row, column):
        
        ## Checks if the Cell is Outside of the Game Board ##
        if row < 0 or row >= self.height or column < 0 or column >= self.width:
            return False

        return(self.grid[row][column] == 0)
        
    ## Check If a Row is Full (If a Row is Full, return true(1) else return false(0)) ##
    def is_full(self, row, column):

        ## Checks if the Cell is Outside of the Game Board ##
        if row < 0 or row >= self.height or column < 0 or column >= self.width:
            return False
                
        return(self.grid[row][column] == 1)
    
    ## Checks if row is full
    ## TODO: Shift pieces down
    def remove_full_rows(self):
        for row in range(self.height):
            # DEBUG: Correct syntax?
            if all(self.grid[row]) == 1:
                self.grid[row] = [0 for _ in range(self.width)]


class ScoreBoard:

    ## Initialize the Score Board with a Given Width and Height (This will be a 5x5 Grid) ##
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    ## Set the layout of the Score Board (We want to Display the Score) ##
    def score_Layout(self, score):

        ## Loop for Clearing and Replacing the Score ##
        ## The Score is as Follows:Single Line = 40*(n+1), Double Line = 100*(n+1), Triple Line = 300*(n+1), Tetris = 1200*(n+1) (where n is the level number)##
        for row in range(self.height):
            for column in range(self.width):
                ## Clear Score Board ##
                self.grid[row][column] = 0
                ## Replace Score Board with the New Score ##
                ## n is the level number, there are 50 levels, so n = 1,2,...,50 ##
                n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]