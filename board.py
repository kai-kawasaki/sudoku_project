import pygame
import pygame.freetype
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
from cell import Cell

WIDTH = 540
HEIGHT = 600
CELL_SIZE = 60
SQUARE_SIZE = 180
LINE_COLOR = (40, 40, 40)

class Board:
    cells = {} # Dictionary of cells

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.reset_rectangle = None
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
            pygame.draw.line(self.screen, "Orange", (0, SQUARE_SIZE * i), (self.width, SQUARE_SIZE * i), 6)
        for i in range(1, 9):
            pygame.draw.line(self.screen, "Orange", (0, CELL_SIZE * i), (self.width, CELL_SIZE * i), 2)

        # vertical lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, "Orange", (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, self.height), 6)
        for i in range(1, 9):
            pygame.draw.line(self.screen, "Orange", (CELL_SIZE * i, 0), (CELL_SIZE * i, self.height), 2)

        # Bottom border line
        pygame.draw.line(self.screen, (0, 125, 200), (0, SQUARE_SIZE + 56 * 8), (self.width, SQUARE_SIZE + 56 * 8), 6)

        # cells
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()
        

        BUTTON_FONT = pygame.freetype.Font("NexaRustSans-Black.ttf", 30)

        # Prepares button variable
        reset_text = BUTTON_FONT.render("Reset", True, (255, 255, 255))
        restart_text = BUTTON_FONT.render("Restart", True, (255, 255, 255))
        exit_text = BUTTON_FONT.render("Exit", True, (255, 255, 255))

        # Prepares button surface
        ###reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        ###reset_surface.fill(LINE_COLOR)
        ###reset_surface.blit(reset_text, (10, 10))

        ###restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        ###restart_surface.fill(LINE_COLOR)
        ###restart_surface.blit(restart_text, (10, 10))

        ###exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        ###exit_surface.fill(LINE_COLOR)
        ###exit_surface.blit(exit_text, (10, 10))

        # Positions buttons
        ###self.reset_rectangle = reset_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 338))
        ###self.restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 338))
        ###self.exit_rectangle = exit_surface.get_rect(center=((3 * WIDTH) // 4, HEIGHT // 2 + 338))

        # Buttons final
        ###self.screen.blit(reset_surface, self.reset_rectangle)
        ###self.screen.blit(restart_surface, self.restart_rectangle)
        ###self.screen.blit(exit_surface, self.exit_rectangle)

    
