import pygame, sys
import pygame.freetype
from board import Board

# setup of constants
WIDTH = 540
HEIGHT = 600
CELL_SPACING = 60
GROUP_SIZE = 180
running = True



#color pallet
dark_moss = (81, 75, 35)
moss = (101, 104, 57)
sage = (203, 201, 173)
ash = (203, 208,185)
mist = (189, 219, 208)
white = (250, 250, 250)

def main_screen(screen):
    
    game_screen = 0

    # wipe the screen with the background
    screen.fill(dark_moss)

    if (game_screen == 0): # title
        pygame.draw.rect(screen, ash, pygame.Rect(0, 540, 599, 60))


        pygame.draw.rect(screen, moss, pygame.Rect(0, 540, 599, 60), width=6)
        pygame.draw.line(screen, moss, (179,540), (179, 599),width=4)
        pygame.draw.line(screen, moss, (359,540), (359, 599),width=4)
        pygame.draw.line(screen, moss, (537,540), (537, 599),width=4)

        # title text
        title_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 100)
        title_surface, rect = title_font.render("SUDOKU", ash)
        screen.blit(title_surface, (40, 200))
        
        title_font2 = pygame.freetype.Font("NexaRustSans-Black.ttf", 30)
        button_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 35)
        
        title_surface2, rect = title_font2.render("Select Game Mode", ash)
        center=(WIDTH // 2, HEIGHT // 2)
        screen.blit(title_surface2, (85, 450))

        # creating buttons
        easy_text = button_font.render("Easy", moss)
        medium_text = button_font.render("Medium", moss)
        hard_text = button_font.render("Hard", moss)

        easy_surface, easy_rect = easy_text
        screen.blit(easy_surface, (35, 556))

        medium_surface, medium_rect = medium_text
        screen.blit(medium_surface, (194, 556))

        hard_surface, hard_rect = hard_text
        screen.blit(hard_surface, (390, 556))

        easy_rectangle = easy_surface.get_rect(center=(35, 556))
        medium_rectangle = medium_surface.get_rect(center=(194, 556))
        hard_rectangle = hard_surface.get_rect(center=(390, 556))


        while running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        sys.exit()
                    case pygame.MOUSEBUTTONDOWN:
                        if easy_rectangle.collidepoint(event.pos):  # 30 cells
                            return 30
                        if medium_rectangle.collidepoint(event.pos):  # 40 cells
                            return 40
                        if hard_rectangle.collidepoint(event.pos):  # 50 cells
                            return 50
            pygame.display.update()


def win_screen(screen): # winning screen
    screen.fill(mist)
    win_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 100)
    win_surface, rect = win_font.render("WIN", ash)
    screen.blit(win_surface, (40, 200))


def lose_screen(screen): # losing screen
    screen.fill(dark_moss)
    lose_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 100)
    lose_surface, rect = lose_font.render("LOSE", ash)
    screen.blit(lose_surface, (40, 200))

def win_check(screen, main_board):
    win = True
    for row in range(9):
        for col in range(9):
            main_board.board[row][col] = 0
            if main_board.is_valid(row, col, main_board.cells[row][col].sketch_value) == False: # confirms if pplayer input
                win = False
            main_board.board[row][col] = main_board.cells[row][col].sketch_value
            if main_board.cells[row][col].value == "0" and main_board.cells[row][col].sketch_value == 0:
                win = False
    if win:
        win_screen(screen)
    else:
        lose_screen(screen)


def sudo_buttons(main_board, screen, event, difficulty):
    result = True
    if main_board.reset_rect.collidepoint(event.pos):  # resets the board
        screen.fill(moss)
        main_board = Board(WIDTH, HEIGHT, screen, difficulty)
        main_board.draw()
        pygame.display.update()
    elif main_board.restart_rect.collidepoint(event.pos):  # back to the start menu
        main()
    elif main_board.exit_rect.collidepoint(event.pos):  # Closes the program
        sys.exit()
    else:
        result = False
    return [result, main_board]  


def set_value(main_board, row, col, key):  # updates the board wit the new value
    print(key)
    main_board.update_value(row, col, f"{key}")
    main_board.board[row][col] = key
    print(main_board.board[row][col])

def main():
    pygame.init()  # Initializes pygame.
    screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Creates the window.
    removed = main_screen(screen)  # Shows the start screen and gets the number of removed cells.
    screen.fill((81, 75, 35))  # Makes the background.

    # Draws the board with random values.
    main_board = Board(WIDTH, HEIGHT, screen, removed)
    main_board.draw()
    pygame.display.update()

    #user input
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    sys.exit()
                case pygame.KEYDOWN:  # If enter is pressed then win condition is checked
                    if event.key == pygame.K_RETURN:
                        win_check(screen, main_board)
                        break
                case pygame.MOUSEBUTTONDOWN:  # If the user clicks.
                    buttons = sudo_buttons(main_board, screen, event, removed)
                    main_board = buttons[1]
                    if not buttons[0]:  # If the user didn't click on one of the buttons
                        # Checks which cell they clicked on.
                        for row in main_board.cells:
                            for col in main_board.cells[row]:
                                if main_board.cells[row][col].value_rect.collidepoint(event.pos) and main_board.cells[row][col].value == "0":  # Only allows change if cell is empty.
                                    go = True
                                    while go:  # Checks for user input.
                                        main_board.cells[row][col].enable_selection()  # Highlights the current cell.
                                        for event2 in pygame.event.get():
                                            if event2.type == pygame.KEYDOWN:  # If keyboard button pressed.
                                                match event2.key:
                                                    # Moves the highlighted cell in inputted direction if possible.
                                                    case pygame.K_DOWN:
                                                        main_board.cells[row][col].disable_selection()
                                                        col += 1 if col != 8 else 0
                                                    case pygame.K_UP:
                                                        main_board.cells[row][col].disable_selection()
                                                        col -= 1 if col != 0 else 0
                                                    case pygame.K_RIGHT:
                                                        main_board.cells[row][col].disable_selection()
                                                        row += 1 if row != 8 else 0
                                                    case pygame.K_LEFT:
                                                        main_board.cells[row][col].disable_selection()
                                                        row -= 1 if row != 0 else 0

                                                    # Checks for digit input for cell.
                                                    case pygame.K_1:
                                                        set_value(main_board, row, col, 1)
                                                        go = False
                                                        break
                                                    case pygame.K_2:
                                                        set_value(main_board, row, col, 2)
                                                        go = False
                                                        break
                                                    case pygame.K_3:
                                                        set_value(main_board, row, col, 3)
                                                        go = False
                                                        break
                                                    case pygame.K_4:
                                                        set_value(main_board, row, col, 4)
                                                        go = False
                                                        break
                                                    case pygame.K_5:
                                                        set_value(main_board, row, col, 5)
                                                        go = False
                                                        break
                                                    case pygame.K_6:
                                                        set_value(main_board, row, col, 6)
                                                        go = False
                                                        break
                                                    case pygame.K_7:
                                                        set_value(main_board, row, col, 7)
                                                        go = False
                                                        break
                                                    case pygame.K_8:
                                                        set_value(main_board, row, col, 8)
                                                        go = False
                                                        break
                                                    case pygame.K_9:
                                                        set_value(main_board, row, col, 9)
                                                        go = False
                                                        break
                                            if event2.type == pygame.QUIT:
                                                sys.exit()
                                            if event2.type == pygame.MOUSEBUTTONDOWN:  # Checks if button was pressed.
                                                main_board = sudo_buttons(main_board, screen, event2, removed)[1]
                                    main_board.cells[row][col].disable_selection()  # Removes selection when cleared




if __name__ == "__main__":  # Runs the main method.
    main()
