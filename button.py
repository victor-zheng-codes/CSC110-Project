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
        - all(0 <= value[0] <= 255 for value in self.colours)
        - all(0 <= value[1] <= 255 for value in self.colours)
        - all(0 <= value[2] <= 255 for value in self.colours)
        - all(0 <= value <= 255 for value in self.colour)
        - all(num >= 0 for num in self.dimensions)
    """
    colours: list[tuple[int, int, int]]
    colour: tuple[int, int, int]
    dimension: tuple[int, int]
    position: tuple[int, int]
    font_name: str

    def __init__(self, dimension: tuple[int, int], position: tuple[int, int]) -> None:
        """Initializes the Button class its following variables.

        Preconditions:
            - position != ()
            - dimension != ()
        """
        # Initialize the colours for the button
        self.colours = [(240, 240, 240), (200, 200, 200)]
        # Takes the first tuple from self.colours
        self.colour = self.colours[0]
        # Initialize the dimension for the screen as (width, height)
        self.dimension = dimension
        # Initialize the position of the button as (x, y)
        self.position = position
        # Initialize the font name
        self.font_name = "M1PRegular-R3wv.ttf"

    def draw(self, surface: pygame.display, text: str, size: int) -> None:
        """Draws the button onto a display.

        Preconditions:
            - size > 0
            - len(text) > 0
        """
        # Assign the variables x, y, w, h
        x, y = self.position
        w, h = self.dimension

        # Assign a rectangular shape
        rect = pygame.Rect(x - w // 2, y - h // 2, w, h)
        # Assign the font
        font = pygame.font.Font(self.font_name, size)
        # Draw text on the display
        text_surface = font.render(text, True, (0, 0, 0))
        # Gets the rectangular area of the text
        text_rect = text_surface.get_rect(center=(x, y))
        # Draws the rectangular shape on the display
        pygame.draw.rect(surface, pygame.Color(self.colour), rect)
        # Draws the objects onto the screen
        surface.blit(text_surface, text_rect)

    def get_x_pos(self) -> tuple[int, int]:
        """Return the button's left and right x positions.
        """
        # Takes the x position
        x, _ = self.position
        # Takes the width of the dimension
        w, _ = self.dimension
        # Calculates and returns the buttons x position
        return x - w // 2, x + w // 2

    def get_y_pos(self) -> tuple[int, int]:
        """Return the button's top and bottom y positions.
        """
        # Takes the y position
        _, y = self.position
        # Takes the height of the dimension
        _, h = self.dimension
        # Calculates and returns the buttons y position
        return y - h // 2, y + h // 2

    def mouse_hover(self, mouse: pygame.mouse) -> bool:
        """Return whether or not the mouse is on the button.
        If the mouse is on the button, this will change the buttons colour.
        """
        # Checks if the mouse is on the button
        if self.get_x_pos()[0] <= mouse[0] <= self.get_x_pos()[1] and \
                self.get_y_pos()[0] <= mouse[1] <= self.get_y_pos()[1]:
            # Changes the colour of the button to (240, 240, 240)
            self.colour = self.colours[1]
            # Confirms that the change has been made
            return True
        # The following is executed if the if-statement is rejected
        else:
            # Changes the colour of the button to (200, 200, 200)
            self.colour = self.colours[0]
            # Confirms that the change has not been made
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
