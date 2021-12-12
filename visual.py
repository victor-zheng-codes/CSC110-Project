"""CSC110 Fall 2021 Final Project Visuals

File Description
===============================
This file contains the Visual Class for our final project in CSC110. It visualizes our computations
and uses pygame to create an interactive pygame application to access information on our data.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of students, TA, and professors
within the CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Daniel Xu, Nicole Leung, Kirsten Sutantyo, and Victor Zheng.
"""
from sys import exit
import pygame
import random

from button import Button


class Visual:
    """This visualizes the product of our computation.

    Instance Attributes:
        - dimension: the dimension of the screen in (width, height)
        - screen: the pygame screen to display our pygame visuals
        - clock: the pygame time to run code
        - virus_pic: a pygame image of our icon
        - virus_rect: the pygame size of our icon
        - font_name: the name of our pygame font
        - start: an interactive button to start an event
        - quit: an interactive button to end an event

    Representation Invariants:
        - all(num >= 0 for num in self.dimensions)
    """
    dimension: tuple[int, int]
    screen: pygame.display
    clock: pygame.time
    virus_pic: pygame.image
    virus_rect: pygame.Rect
    font_name: pygame.font

    start: Button
    quit: Button

    def __init__(self) -> None:
        """Initializes the visual class and its variables, and starts up the program.
        """
        pygame.init()
        self.font_name = pygame.font.match_font('dubai')  # Sets up the font
        self.dimension = (1600, 1000)  # Sets the dimension for the screen (width, height)
        w, h = self.dimension
        self.screen = pygame.display.set_mode((w, h))  # Sets the screens (width, height)

        pygame.display.set_caption('CO(VISION)')  # The title of our program
        self.clock = pygame.time.Clock()
        # http://resources.finalsite.net/images/v1603987533/ellensburg/ixbajjxlqntul6ymrofc/COVID.jpg
        pygame.display.set_icon(pygame.image.load('COVID.jpg'))  # Displays an image of chosen icon
        self.virus_pic = pygame.image.load('virus.png')
        self.virus_rect = self.virus_pic.get_rect()

        self.start = Button((500, 150), (w // 2 - 50, h // 2 + 50))  # (width, height) and (x, y)
        self.quit = Button((200, 200), (w // 2 - 50, h // 2))

    def draw_text(self, surface: pygame.display, text: str, size: int,
                  dimension: tuple[int, int]) -> None:
        """Draw the button onto a display
        """
        x, y = dimension
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)

    def start_menu(self) -> None:
        """The main menu of the program
        """
        w, h = self.dimension
        # Image spawns at a random position on the screen
        self.virus_rect.top_left = (random.randint(0, w // 2), random.randint(0, h // 2))
        x_velocity = 10  # The speed of the image
        y_velocity = 6
        while True:  # Infinite while loop
            self.screen.fill((255, 255, 255))  # Background colour of the screen
            mouse = pygame.mouse.get_pos()  # Tracks the mouse and its interactions with events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.start.mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.main()

            self.screen.blit(self.virus_pic, self.virus_rect)  # Drawing the screen with text
            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment',
                           70, (w // 2, h // 4))
            self.draw_text(self.screen, 'How does  the  pandemic  impact  employment  in  Ontario?',
                           50, (w // 2, h // 3))
            self.draw_text(self.screen,
                           'Are  there  certain  industries  that  suffered or '
                           'benefited more than others?', 50, (w // 2, h // 3 + 50))
            self.start.draw(self.screen, "Individual Comparison", 50)

            self.virus_rect.x += x_velocity  # Moving the image across the screen
            self.virus_rect.y += y_velocity

            # Changes image direction if the image bumps into the border of the screen
            if self.virus_rect.x + self.virus_rect.w > w:
                x_velocity = -x_velocity
            if self.virus_rect.x < 0:
                x_velocity = -x_velocity
            if self.virus_rect.y + self.virus_rect.h > h:
                y_velocity = -y_velocity
            if self.virus_rect.y < 0:
                y_velocity = -y_velocity

            pygame.display.update()  # Refreshes the display
            self.clock.tick(50)

    def main(self) -> None:
        """The main page of the program
        """
        while True:
            self.screen.fill((0, 0, 0))  # Covers up anything from the start menu
            mouse = pygame.mouse.get_pos()  # Tracks the mouse and its interactions with events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.quit.mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_menu()

            self.quit.draw(self.screen, 'bye', 30)
            pygame.display.update()  # Refreshes the display
            self.clock.tick(50)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': ['python_ta.contracts', 'pygame', 'button', 'sys'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
