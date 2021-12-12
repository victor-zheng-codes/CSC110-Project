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
import random
import pygame

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
        - buttons: a list holding all the button

    Representation Invariants:
        - all(num >= 0 for num in self.dimensions)
    """
    dimension: tuple[int, int]
    screen: pygame.display
    clock: pygame.time
    virus_pic: pygame.image
    virus_rect: pygame.Rect
    font_name: pygame.font

    buttons: dict[str, Button]

    def __init__(self) -> None:
        """Initializes the visual class and its variables, and starts up the program.
        """
        pygame.init()
        self.font_name = pygame.font.match_font('dubai')
        self.dimension = (1600, 1000)
        w, h = self.dimension
        self.screen = pygame.display.set_mode((w, h))

        pygame.display.set_caption('CO(VISION)')
        self.clock = pygame.time.Clock()
        # http://resources.finalsite.net/images/v1603987533/ellensburg/ixbajjxlqntul6ymrofc/COVID.jpg
        pygame.display.set_icon(pygame.image.load('COVID.jpg'))
        self.virus_pic = pygame.image.load('virus.png')
        self.virus_rect = self.virus_pic.get_rect()

        small_button_width = 300

        self.buttons = {'individual': Button((500, 150), (w // 2 - 50, h // 2 + 50)),
                        'all': Button((500, 150), (w // 2 - 50, h // 2 + 200)),
                        'Total employed, all industries': Button((small_button_width, 100),
                                                                 (w // 4, h // 5)),
                        'Goods-producing sector': Button((small_button_width, 100),
                                                         (w // 4, h // 5 + 125)),
                        'Agriculture': Button((small_button_width, 100), (w // 4, h // 5 + 250)),
                        'Forestry':
                            Button((small_button_width, 100), (w // 4, h // 5 + 375)),
                        'Utilities':
                            Button((small_button_width, 100), (w // 4, h // 5 + 500)),
                        'Construction': Button((small_button_width, 100), (w // 4, h // 5 + 250))
                        }

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
        self.virus_rect.topleft = (random.randint(0, w // 2), random.randint(0, h // 2))
        x_velocity = random.choice([-10, 10])  # The speed of the image
        y_velocity = random.choice([-6, 6])
        while True:
            self.screen.fill((255, 255, 255))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.buttons['individual'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    self.individual()
                if self.buttons['all'].mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.individual()

            self.screen.blit(self.virus_pic, self.virus_rect)
            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment',
                           70, (w // 2, h // 4))
            self.draw_text(self.screen, 'How does  the  pandemic  impact  employment  in  Ontario?',
                           50, (w // 2, h // 3))
            self.draw_text(self.screen,
                           'Are  there  certain  industries  that  suffered or '
                           'benefited more than others?', 50, (w // 2, h // 3 + 50))
            self.buttons['individual'].draw(self.screen, "Individual Comparisons", 50)
            self.buttons['all'].draw(self.screen, "All Comparisons", 50)

            self.virus_rect.x += x_velocity
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

    def individual(self) -> None:
        """The main page of the program
        """
        while True:  # Infinite while loop
            self.screen.fill((255, 255, 255))  # Background colour of the screen
            mouse = pygame.mouse.get_pos()  # Tracks the mouse and its interactions with events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start_menu()
                if self.buttons['Total employed, all industries'].mouse_hover(
                        mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO
                    pass
                if self.buttons['Goods-producing sector'].mouse_hover(
                        mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO
                    pass
                if self.buttons['Agriculture'].mouse_hover(
                        mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO
                    pass
                if self.buttons['Forestry'].mouse_hover(
                        mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO
                    pass
                if self.buttons['Utilities'].mouse_hover(
                        mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO
                    pass
                if self.buttons['Construction'].mouse_hover(
                        mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO
                    pass

            # Display the buttons
            self.buttons['Total employed, all industries'].draw(self.screen, 'Total employed, '
                                                                             'all industries', 15)
            self.buttons['Goods-producing sector'].draw(self.screen, 'Goods-producing sector', 15)
            self.buttons['Agriculture'].draw(self.screen, 'Agriculture', 15)
            self.buttons['Forestry'].draw(
                self.screen, 'Forestry, fishing, mining, quarrying, oil and gas', 15)
            self.buttons['Utilities'].draw(self.screen, 'Utilities', 15)
            self.buttons['Construction'].draw(self.screen, 'Construction', 15)
            pygame.display.update()
            self.clock.tick(50)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': ['python_ta.contracts', 'pygame', 'button', 'sys', 'random'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
