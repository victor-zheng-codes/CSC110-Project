"""CSC110 Fall 2021 Final Project, Visual Class

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
    """This visualizes the product of our computation

    Instance Attributes:
        - dimension: the dimension of the screen in (width, length)
        - screen: the pygame screen to display our pygame visuals
        - clock: the pygame time to run code
        - virus_pic: a pygame image of our icon
        - virus_rect: the pygame size of our icon
        - font_name: the name of our pygame font
        - start: an interactive button to start an event
        - quit: an interactive button to end an event
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
        """Initiates the various variables, and start up program
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

        self.start = Button((500, 150), (w // 2 - 50, h // 2 + 50))
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
        self.virus_rect.topleft = (random.randint(0, w // 2), random.randint(0, h // 2))
        xvelocity = 10
        yvelocity = 6
        while True:
            self.screen.fill((255, 255, 255))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.start.mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.main()

            self.screen.blit(self.virus_pic, self.virus_rect)
            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment',
                           70, (w // 2, h // 4))
            self.draw_text(self.screen, 'How does  the  pandemic  impact  employment  in  Ontario?',
                           50, (w // 2, h // 3))
            self.draw_text(self.screen,
                           'Are  there  certain  industries  that  suffered or '
                           'benefited more than others?', 50, (w // 2, h // 3 + 50))
            self.start.draw(self.screen, "Individual Comparison", 50)

            self.virus_rect.x += xvelocity
            self.virus_rect.y += yvelocity

            if self.virus_rect.x + self.virus_rect.w > w:
                xvelocity = -xvelocity
            if self.virus_rect.x < 0:
                xvelocity = -xvelocity
            if self.virus_rect.y + self.virus_rect.h > h:
                yvelocity = -yvelocity
            if self.virus_rect.y < 0:
                yvelocity = -yvelocity

            pygame.display.update()
            self.clock.tick(50)

    def main(self) -> None:
        """The main page of the program
        """
        while True:
            self.screen.fill((0, 0, 0))  # covers up anything from the start menu
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if self.quit.mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_menu()

            self.quit.draw(self.screen, 'bye', 30)
            pygame.display.update()
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
