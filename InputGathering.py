from Model import Cell, Board, Environment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

# Light-up base url for board gathering
BASE_URL = 'https://www.puzzle-light-up.com/'

# Light-up end url according to each level and difficulties
LEVEL_7_EASY = ''
LEVEL_7_NORMAL = '?size=1'
LEVEL_7_HARD = '?size=2'
LEVEL_10_EASY = '?size=3'
LEVEL_10_NORMAL = '?size=4'
LEVEL_10_HARD = '?size=5'
LEVEL_14_EASY = '?size=6'
LEVEL_14_NORMAL = '?size=7'
LEVEL_14_HARD = '?size=8'
LEVEL_25_EASY = '?size=9'
LEVEL_25_NORMAL = '?size=10'
LEVEL_25_HARD = '?size=11'
LEVEL_DAILY = '?size=13'
LEVEL_WEEKLY = '?size=12'
LEVEL_MONTHLY = '?size=14'

# Cell component identification for web scraping
WHITE_EMPTY = 'cell selectable cell-off'
BLACK_NUMBER = 'light-up-task-cell'
BLACK_WALL = 'light-up-task-cell wall'

# Open selenium using Chrome Profile
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={Environment.USER_DATA}")
options.add_argument(f"--profile-directory={Environment.PROFILE_DIRECTORY}")

# Assign chrome web driver and profile, because we will use Chrome Browser for web scraping
# driver = webdriver.Chrome(Environment.CHROME_DRIVER_PATH, chrome_options=options)
driver = webdriver.Chrome(Environment.CHROME_DRIVER_PATH)

def gatherBoard (level, size):
    # URL for web scraping target
    url = '{}{}'.format(BASE_URL, level)

    # Let selenium open the target URL for scraping
    driver.get(url)

    # Get all tiles from the board on web
    tiles = driver.find_element(By.CLASS_NAME, value = 'board-back').find_elements(By.TAG_NAME, value = 'div')

    # Get every board cell information
    board = getCellsFromBoard(tiles, size)

    # Debugging purposes
    printBoard(board)

    # Try writing the board to txt files
    writeBoard(size, board)


def getCellsFromBoard (tiles, colSize):
    # Variable initialization
    tileClass = ''  # used for temporary class information
    tileText = ''   # used for temporary child text information
    board = []      # returned 2d list
    row = []        # used for temporary row list
    i = 0

    # Iterate trough every tile on the tiles
    for tile in tiles:
        tileClass = tile.get_attribute('class')
        tileText = tile.text

        # Assigning correct cell value, and add it to the temp board
        if tileClass == WHITE_EMPTY:
            row.append(Cell.WHITE_EMPTY)
        if tileClass == BLACK_WALL:
            row.append(Cell.BLACK_ANY)
        if tileClass == BLACK_NUMBER:
            if tileText == '0':
                row.append(Cell.BLACK_ZERO)
            if tileText == '1':
                row.append(Cell.BLACK_ONE)
            if tileText == '2':
                row.append(Cell.BLACK_TWO)
            if tileText == '3':
                row.append(Cell.BLACK_THREE)
            if tileText == '4':
                row.append(Cell.BLACK_FOUR)

        # Move to the next row on the board
        if i == colSize:
            i = 0
            board.append(row)
            row = []
        
        i += 1

    # Return the temporary board
    return board

def printBoard (board):
    # Print the board in matrix 2d display
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
    print('\n')

def makeEmptyInputFiles ():
    nums = [7, 10, 14, 25, 'DAILY', 'WEEKLY', 'MONTHLY']
    for num in nums:
        open (f"Dataset/{num}.txt", 'w').close()

def writeBoard (size, board):
    # Input file name format
    filename = f"Dataset/{size}.txt"

    # Appending the file
    originalSTD = sys.stdout
    with open (filename, 'a') as f:
        sys.stdout = f
        printBoard(board)
        sys.stdout = originalSTD

# Main
if __name__ == "__main__":
    makeEmptyInputFiles()
    for i in range (5):
        gatherBoard(LEVEL_10_EASY, Board.SIZE_LEVEL_10)