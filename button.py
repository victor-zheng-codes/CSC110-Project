"""CSC110 Fall 2021 Final Project Buttons

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
    """Defines objects which a user can interactive to perform a particular action.

    Instance Attributes:
        - colours: a list of rgb colour codes
        - colour: an rgb colour code (e.g., (63, 30, 43))
        - dimension: the dimension of the screen in (width, height)
        - position: the position of an object on the screen (x, y)
        - font_name: the name of our pygame font

    Representation Invariants:
        - all(0 <= value[0] <= 255 for value in colours)
        - all(0 <= value[1] <= 255 for value in colours)
        - all(0 <= value[2] <= 255 for value in colours)
        - all(0 <= value <= 255 for value in colour)
        - all(num >= 0 for num in self.dimensions)
    """
    colours: list[tuple[int, int, int]]
    colour: tuple[int, int, int]
    dimension: tuple[int, int]
    position: tuple[int, int]
    font_name: str

    def __init__(self, dimension: tuple[int, int], position: tuple[int, int]) -> None:
        """Initialize the variables for class Button.
        """
        self.colours = [(240, 240, 240), (200, 200, 200)]
        self.colour = self.colours[0]  # Takes the first tuple from self.colours
        self.dimension = dimension  # Sets the dimension for the screen (width, height)
        self.position = position  # Sets the position of the button in (x, y)
        self.font_name = "M1PRegular-R3wv.ttf"  # Sets up the font

    def draw(self, surface: pygame.display, text: str, size: int) -> None:
        """Draw the button onto a display.
        """
        x, y = self.position
        w, h = self.dimension

        rect = pygame.Rect(x - w // 2, y - h // 2, w, h)  # Draws the shape of the button
        font = pygame.font.Font(self.font_name, size)  # Draws the text of the button
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        pygame.draw.rect(surface, pygame.Color(self.colour), rect)
        surface.blit(text_surface, text_rect)  # Draws the objects onto the screen

    def get_x_pos(self) -> tuple[int, int]:
        """Return the button's left and right x positions.
        """
        x, _ = self.position
        w, _ = self.dimension
        return x - w // 2, x + w // 2

    def get_y_pos(self) -> tuple[int, int]:
        """Return the button's top and bottom y positions.
        """
        _, y = self.position
        _, h = self.dimension
        return y - h // 2, y + h // 2

    def mouse_hover(self, mouse: pygame.mouse) -> bool:
        """Return whether or not the mouse is on this button.
        If the mouse is on the button, this will change the buttons colour.
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
        'disable': ['R1705', 'C0200']
    })
