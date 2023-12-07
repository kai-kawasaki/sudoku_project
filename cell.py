import pygame

# Constants
CELL_SPACING = 60
GROUP_SIZE = 180
FULL_WIDTH = 540


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketch_value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.value_rect = None

    # Cell re-seter
    def set_cell_value(self, value):
        self.value = value

    # Creates a highlight of the currently selected cell
    def enable_selection(self):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         ((self.col * 60), (self.row * 60), CELL_SPACING+2, CELL_SPACING+2), 2)
        pygame.display.update()

    # Removes the just created cell highlight
    def disable_selection(self):
        pygame.draw.rect(self.screen, "orange",
                         ((self.col * 60), (self.row * 60), CELL_SPACING + 2, CELL_SPACING + 2), 2)
        pygame.draw.line(self.screen, "orange", (0, GROUP_SIZE + 56 * 8),
                         (FULL_WIDTH, GROUP_SIZE + 56 * 8), 6)  # Redraws the line at the bottom for looks.
        pygame.display.update()

    # Setter function for the number graphic of a cell
    def set_sketched_value(self, sketched_value):
        if self.value == 0:
            
            # Draws a rectangle to cover a preexisting sketched number
            pygame.draw.rect(self.screen, "Cyan", pygame.Rect((self.col * 60)+5, (self.row * 60)+5, CELL_SPACING-10, CELL_SPACING-10))
            print("WORKING")

            # Adds a new sketched number
            self.sketched_value = sketched_value
            value_font = pygame.font.Font(None, 60)                                            
            value_surf = value_font.render(f'{self.sketched_value if ord("1") <= ord(self.sketched_value) <= ord("9") else "      "}', True, (30, 30, 30))#line color
            self.value_rect = value_surf.get_rect(center = (CELL_SPACING // 2 + CELL_SPACING * self.col, CELL_SPACING // 2 + CELL_SPACING * self.row))
            self.screen.blit(value_surf, self.value_rect)
            pygame.display.update()

    # Draws the graphic of a cell
    def draw(self):
        value_font = pygame.font.Font(None, 60)
        value_surf = value_font.render(f'{self.value if ord("1")<=ord(self.value)<=ord("9") else "      "}', True, (255, 255, 255))
        self.value_rect = value_surf.get_rect(center=(CELL_SPACING // 2 + CELL_SPACING * self.col, CELL_SPACING // 2 + CELL_SPACING * self.row))
        pygame.draw.rect(self.screen, "Orange", ((self.col * 60), (self.row * 60), CELL_SPACING + 2, CELL_SPACING + 2), 2)
        pygame.draw.line(self.screen, (0, 125, 200), (0, GROUP_SIZE + 56 * 8),(FULL_WIDTH, GROUP_SIZE + 56 * 8), 6)
        
        self.screen.blit(value_surf, self.value_rect)

    # For representing the cell objects as a non-object
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return int(self.value)

    def __int__(self):
        return int(self.value)
