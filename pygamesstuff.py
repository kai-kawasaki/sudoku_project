import pygame, sys
import pygame.freetype

# pygame setup
WIDTH = 540
HEIGHT = 600
dim = (WIDTH, HEIGHT)
pygame.init()
screen = pygame.display.set_mode(dim)
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Sudoku Game 23")


# textReset = pygame.image.load("textReset.png")



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game_screen = 0

    #colors
    dark_moss = (81, 75, 35)
    moss = (101, 104, 57)
    sage = (203, 201, 173)
    ash = (203, 208,185)
    mist = (189, 219, 208)
    white = (250, 250, 250)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(dark_moss)

    if (game_screen == 0): # title
        pygame.draw.rect(screen, ash, pygame.Rect(0, 540, 599, 60))


        pygame.draw.rect(screen, moss, pygame.Rect(0, 540, 599, 60), width=3)
        pygame.draw.line(screen, moss, (179,540), (179, 599),width=3)
        pygame.draw.line(screen, moss, (359,540), (359, 599),width=3)
        pygame.draw.line(screen, moss, (539,540), (539, 599),width=3)

        # text
        title_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 100)
        title_surface, rect = title_font.render("SUDOKU", white)
        screen.blit(title_surface, (40, 200))
        
        title_font2 = pygame.freetype.Font("NexaRustSans-Black.ttf", 30)
        button_font = pygame.freetype.Font("NexaRustSans-Black.ttf", 20)
        
        title_surface2, rect = title_font2.render("Select Game Mode", white)
        center=(WIDTH // 2, HEIGHT // 2)
        screen.blit(title_surface2, (85, 450))

        # Initialize buttons.
        easy_text = button_font.render("Easy", (255, 255, 255))
        medium_text = button_font.render("Medium", (255, 255, 255))
        hard_text = button_font.render("Hard", (255, 255, 255))

        easy_surface, rect = easy_text
        screen.blit(easy_surface, (10, 10))


        pass

    elif (game_screen == 1): # main
        pygame.draw.rect(screen, "tomato", pygame.Rect(0, 540, 599, 60))
        pygame.draw.rect(screen, "tomato4", pygame.Rect(0, 540, 599, 60), width=3)
        pygame.draw.line(screen, "tomato4", (179,540), (179, 599),width=3)
        pygame.draw.line(screen, "tomato4", (359,540), (359, 599),width=3)
        pygame.draw.line(screen, "tomato4", (539,540), (539, 599),width=3)
        pass

    elif (game_screen == 2):
        pass

    elif (game_screen == 3):
        pass

    else:
        pass


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(2)  # limits FPS to 60

pygame.quit()