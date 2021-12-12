"""CSC110 Fall 2021 Final Project, Button Class

File Description
===============================
This file contains the Button Class for our final project in CSC110. It creates buttons, allowing
the user to interact and navigate (see visual.py) our pygame application to access data.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of students, TA, and professors
within the CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Daniel Xu, Nicole Leung, Kirsten Sutantyo, and Victor Zheng.
"""
import pygame


class Button:
    """The button class

    Instance Attributes:
        - colours: a list of rgb colour codes
        - colour: tuple[int, int, int]
        - dimension: the dimension of the screen in (width, length)
        - position: tuple[int, int]
        - font_name: pygame.font
    """
    colours: list[tuple[int, int, int]]
    colour: tuple[int, int, int]
    dimension: tuple[int, int]
    position: tuple[int, int]
    font_name: pygame.font

    def __init__(self, dimension: tuple[int, int], position: tuple[int, int]) -> None:
        """Initialize the variables
        """
        self.colours = [(240, 240, 240), (200, 200, 200)]
        self.colour = self.colours[0]
        self.dimension = dimension
        self.position = position
        self.font_name = pygame.font.match_font('dubai')

    def draw(self, surface: pygame.display, text: str, size: int) -> None:
        """Draw the button onto a display
        """
        x, y = self.position
        w, h = self.dimension

        rect = pygame.Rect(x - w // 2, y - h // 2, w, h)
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        pygame.draw.rect(surface, pygame.Colour(self.colour), rect)
        surface.blit(text_surface, text_rect)

    def get_x_pos(self) -> tuple[int, int]:
        """Return the button's left and right x positions"""
        x, _ = self.position
        w, _ = self.dimension
        return x - w // 2, x + w // 2

    def get_y_pos(self) -> tuple[int, int]:
        """Return the button's top and bottom y positions"""
        _, y = self.position
        _, h = self.dimension
        return y - h // 2, y + h // 2

    def mouse_hover(self, mouse: pygame.mouse) -> bool:
        """Return whether or not the mouse is on this button
        """
        if self.get_x_pos()[0] <= mouse[0] <= self.get_x_pos()[1] and \
                self.get_y_pos()[0] <= mouse[1] <= self.get_y_pos()[1]:
            self.colour = self.colours[1]
            return True
        else:
            self.colour = self.colours[0]
            return False


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': ['python_ta.contracts', 'pygame', 'button', 'sys'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200', 'R0902']
    })
