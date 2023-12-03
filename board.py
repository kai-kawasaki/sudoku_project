import sudoku_generator, cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # Difficulty: easy-0, medium-1, hard-2

    def draw(self):
        # starting point (horrizontal lines)
            # (self.row + i) * boxsize, self.col * boxsize
            # i = 1,2
            # color: bold black
        # ending point
            # (self.row + i) * boxsize, (self.col + 1) * boxsize
            # i = 1,2
            # color: bold black

        # starting point (vertical lines)
            # self.row * cellsize, (self.col + i) * cellsize
            # i = 1,2
            # color: bold black
        # ending point
            # (self.row + 1) * cellsize, (self.col + i) * cellsize
            # i = 1,2
            # color: bold black

        board = sudoku_generator.SudokuGenerator.generate_sudoku(9, 30 + (self.difficulty * 10))
        board.fill_values

        # i_rows = 0
        # i_cols = 0
        # for rows in board.board:
            # for cols in rows:
                # board.board[rows][cols] = cell.Cell(cols, i_rows, i_cols, screen)
                # i_cols += 1
            # i_cols = 0
            # i_rows = 0

    def select(self, row, col):
        pass
        # ???

    def click(self, x, y):
        pass
        # if x-coord < screen size and y-coord < screensize:
            # t1 = x-coord // cellsize
            # t2 = y-coord // cellsize
            # retrurn (t1, t2)
        # else:
            # return None

    def clear(self):
        pass

    def sketch(self, value):
        pass
        # value = input

    def place_number(selfz, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass
        # for rows in board.board:
            # for cols in rows:
                # if board.board[rows][cols] == 0
                    # return False
        # return True

    def update_board(self):
        pass

    def find_empty(self):
        pass
        # for rows in board.board:
            # for cols in rows:
                # if board.board[rows][cols] == 0
                    # t1 = cols
                    # t2 = rows
                    # return (t1, t2)
        # return None

    def check_board(self):
        pass
        # for rows in board.board:
            # for cols in rows:
                # if board.board[rows][cols] == ?solution board?
                    # return False
        # return True
