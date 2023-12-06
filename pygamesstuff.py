import pygame, sys

# pygame setup
dim = (540, 600)
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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("steelblue1")
    
    game_screen = 0

    if (game_screen == 0):
        pygame.draw.rect(screen, "tomato", pygame.Rect(0, 540, 599, 60))


        pygame.draw.rect(screen, "tomato4", pygame.Rect(0, 540, 599, 60), width=3)
        pygame.draw.line(screen, "tomato4", (179,540), (179, 599),width=3)
        pygame.draw.line(screen, "tomato4", (359,540), (359, 599),width=3)
        pygame.draw.line(screen, "tomato4", (539,540), (539, 599),width=3)
        
        pass

    elif (game_screen == 1):
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