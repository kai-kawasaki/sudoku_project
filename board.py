import pygame
import pygame.freetype
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
from cell import Cell

# Constants
WIDTH = 540
HEIGHT = 600
CELL_SPACING = 60
GROUP_SIZE = 180
LINE = (40, 40, 40)

#colors
dark_moss = (81, 75, 35)
moss = (101, 104, 57)
sage = (203, 201, 173)
ash = (203, 208,185)
mist = (189, 219, 208)
white = (250, 250, 250)

class Board:
    cells = {} # Dictionary of 'Cell' objects

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.reset_rect = None
        self.restart_rect = None
        self.exit_rect = None
        # Difficulty: easy-30, medium-40, hard-50
        self.difficulty = difficulty
        
        # Gets a randomly gnerated board from 'sudoku_generator'
        self.board = generate_sudoku(9, self.difficulty)

        # Creates and add 'Cell' objects into the "cells" dictionary
        for col in range(9):
            self.cells[col] = {}
            for row in range(9):
                self.cells[col][row] = Cell(f"{self.board[col][row]}", row, col, screen)

    def draw(self):
        # horizontal lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, "Orange", (0, GROUP_SIZE * i), (self.width, GROUP_SIZE * i), 6)
        for i in range(1, 9):
            pygame.draw.line(self.screen, "Orange", (0, CELL_SPACING * i), (self.width, CELL_SPACING * i), 2)

        # vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, "Orange", (GROUP_SIZE * i, 0), (GROUP_SIZE * i, self.height), 6)
        for i in range(1, 9):
            pygame.draw.line(self.screen, "Orange", (CELL_SPACING * i, 0), (CELL_SPACING * i, self.height), 2)

        # Bottom border line
        pygame.draw.line(self.screen, (0, 125, 200), (0, GROUP_SIZE + 56 * 8), (self.width, GROUP_SIZE + 56 * 8), 6)

        # cells
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()
        

        button_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 30)

        # Prepares button variable
        reset_text = button_font.render("Reset", "black")
        restart_text = button_font.render("Restart", "black")
        exit_text = button_font.render("Exit", "black")

        reset_surface, rect = reset_text
        self.screen.blit(reset_surface, (35, 556))
        self.reset_rect = reset_surface.get_rect(center=(35, 556))

        restart_surface, rect = restart_text
        self.screen.blit(restart_surface, (194, 556))
        self.restart_rect = restart_surface.get_rect(center=(194, 556))

        exit_surface, rect = exit_text
        self.screen.blit(exit_surface, (390, 556))
        self.exit_rect = exit_surface.get_rect(center=(390, 556))

    def update_value(self, row, col, num):
        print("test")
        Board.cells[col][row].set_sketched_value(num)

    def valid_in_row(self, row, num):
        for i in range(9):
            if num == self.board[row][i]:
                return False
        return True


    def valid_in_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True


    def valid_in_box(self, row_start, col_start, num):  # checks if 3 by 3 is valid
        row = 3
        col = 3
        for x in range(3):
            for y in range(3):
                if self.board[row*3+x][col*3+y] == num:
                    return False
        return True


    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        if not self.valid_in_col(col, num):
            return False
        #if not self.valid_in_box(row, col, num):
            #return False
        return True
