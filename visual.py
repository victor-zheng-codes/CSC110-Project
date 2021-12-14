"""CSC110 Fall 2021 Final Project Visuals

File Description
===============================
This file contains the Visual Class for our final project in CSC110. It uses pygame to create an
graphical user interface that the user can interact with to display our computations.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of students, TA, and professors
within the CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Daniel Xu, Nicole Leung, Kirsten Sutantyo, and Victor Zheng.
"""

import sys
import random
import pygame

from visualizations import Visualization
from button import Button


class Visual:
    """A class for the graphical user interface.

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
        - self.font_name[-4:] == ".ttf"
    """
    dimension: tuple[int, int]
    screen: pygame.display
    clock: pygame.time
    virus_pic: pygame.image
    virus_rect: pygame.Rect
    font_name: str

    buttons: dict[str, Button]

    def __init__(self) -> None:
        """Initializes the Visual class and its variables, and starts up the program.
        """
        # Initialize pygame
        pygame.init()
        # Set the font
        self.font_name = "project_font.ttf"
        # Initialize the dimension for the screen as (width, height)
        self.dimension = (1600, 1000)
        # Assigns the variables w, h to the elements in dimension
        w, h = self.dimension
        # Initialize a screen for display
        self.screen = pygame.display.set_mode((w, h))

        # Set the sound effect
        # https://www.fiftysounds.com
        sound_effect = 'sfx-pop.mp3'
        # Load sound
        pygame.mixer.music.load(sound_effect)
        # Set the sound volume
        pygame.mixer.music.set_volume(0.1)

        # Set the display window caption as 'CO(VISION)'
        pygame.display.set_caption('CO(VISION)')
        # Initializes an object to track time
        self.clock = pygame.time.Clock()
        # https://www.statnews.com/wp-content/uploads/2020/02/Coronavirus-CDC.jpg
        # Set the caption image for the display window
        pygame.display.set_icon(pygame.image.load('COVID.jpg'))
        # Loads the image of our virus.png
        self.virus_pic = pygame.image.load('COVID.jpg')
        # Gets the rectangular area of the image
        self.virus_rect = self.virus_pic.get_rect()

        # Initializes a variable for the width of a button
        small_button_width = 400
        # Initialize column_1's x position
        c1_x = w // 4 - 50
        # Initialize column_2's x position
        c2_x = w // 2
        # Initialize column_3's x position
        c3_x = w // 2 + w // 4 + 50

        # A dictionary mapping button names to their dimension and position
        self.buttons = {'back': Button((100, 50), (50, 25)),
                        'individual': Button((500, 150), (w // 2 - 50, h // 2 + 50)),
                        'all': Button((500, 150), (w // 2 - 50, h // 2 + 210)),

                        'Total': Button((small_button_width, 100), (c1_x, h // 5)),
                        'Goods-producing': Button((small_button_width, 100), (c1_x, h // 5 + 125)),
                        'Agriculture': Button((small_button_width, 100), (c1_x, h // 5 + 250)),
                        'Forestry': Button((small_button_width, 100), (c1_x, h // 5 + 375)),
                        'Utilities': Button((small_button_width, 100), (c1_x, h // 5 + 500)),
                        'Construction': Button((small_button_width, 100), (c1_x, h // 5 + 625)),

                        'Manufacturing': Button((small_button_width, 100), (c2_x, h // 5)),
                        'Services-producing':
                            Button((small_button_width, 100), (c2_x, h // 5 + 125)),
                        'Wholesale': Button((small_button_width, 100), (c2_x, h // 5 + 250)),
                        'Transportation': Button((small_button_width, 100), (c2_x, h // 5 + 375)),
                        'Finance': Button((small_button_width, 100), (c2_x, h // 5 + 500)),
                        'Professional': Button((small_button_width, 100), (c2_x, h // 5 + 625)),

                        'Business': Button((small_button_width, 100), (c3_x, h // 5)),
                        'Educational': Button((small_button_width, 100), (c3_x, h // 5 + 125)),
                        'Health': Button((small_button_width, 100), (c3_x, h // 5 + 250)),
                        'Information': Button((small_button_width, 100), (c3_x, h // 5 + 375)),
                        'Accommodation': Button((small_button_width, 100), (c3_x, h // 5 + 500)),
                        'Other': Button((small_button_width, 100), (c3_x, h // 5 + 625)),

                        'Top Benefit': Button((500, 150), (w // 3 - 50, h // 2 + 50)),
                        'Top Suffer': Button((500, 150), (w // 3 - 50, h // 2 + 250)),
                        'Top Positive': Button((500, 150), (w - w // 3 + 50, h // 2 + 50)),
                        'Top Negative': Button((500, 150), (w - w // 3 + 50, h // 2 + 250))
                        }

    def draw_text(self, surface: pygame.display, text: str, size: int,
                  dimension: tuple[int, int]) -> None:
        """Draw the text onto the screen

        Preconditions:
            - size > 0
            - len(text) > 0
        """
        # Assigns x, y to elements of the dimension
        x, y = dimension
        # Assign the font
        font = pygame.font.Font(self.font_name, size)
        # Draw text on the display
        text_surface = font.render(text, True, (0, 0, 0))
        # Gets the rectangular area of the text
        text_rect = text_surface.get_rect(center=(x, y))
        # Draws the objects onto the screen
        surface.blit(text_surface, text_rect)

    def start_menu(self) -> None:
        """The start menu of the program. Front page of the user interface. Displays all of the
        necessary graphics onto the screen and handles user actions.
        """
        # Assigns width, height to elements of the dimension
        w, h = self.dimension
        # Image spawns at a random position on the top left of the screen
        self.virus_rect.topleft = (random.randint(0, w // 2), random.randint(0, h // 2))
        # Select a random x velocity
        x_velocity = random.choice([-10, 10])
        # Select a random y velocity
        y_velocity = random.choice([-6, 6])
        # Creates an infinite while loop
        while True:
            # Fills the screen with a white background
            self.screen.fill((255, 255, 255))
            # Get the mouse position
            mouse = pygame.mouse.get_pos()
            # Get events
            for event in pygame.event.get():
                # Terminate the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Tracks if the mouse clicks on the Individual Comparisons button
                if self.buttons['individual'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    self.individual()
                # Tracks if the mouse clicks on the All Comparisons button
                if self.buttons['all'].mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    self.all()

            # Draws the virus.png onto the screen
            self.screen.blit(self.virus_pic, self.virus_rect)
            # Draws text using the draw_text function
            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment',
                           50, (w // 2, h // 4))
            self.draw_text(self.screen, 'How does  the  pandemic  impact  employment  in  Ontario?',
                           40, (w // 2, h // 3))
            self.draw_text(self.screen,
                           'Are  there  certain  industries  that  suffered or '
                           'benefited more than others?', 40, (w // 2, h // 3 + 50))
            # Draws buttons
            self.buttons['individual'].draw(self.screen, "Individual Comparisons", 35)
            self.buttons['all'].draw(self.screen, "All Comparisons", 35)

            # Sets the speed of the virus.png
            self.virus_rect.x += x_velocity
            self.virus_rect.y += y_velocity

            # Changes image direction if the image bumps into the border of the screen
            if self.virus_rect.x + self.virus_rect.w > w:
                x_velocity = -x_velocity
                pygame.mixer.music.play()
            if self.virus_rect.x < 0:
                x_velocity = -x_velocity
                pygame.mixer.music.play()
            if self.virus_rect.y + self.virus_rect.h > h:
                y_velocity = -y_velocity
                pygame.mixer.music.play()
            if self.virus_rect.y < 0:
                y_velocity = -y_velocity
                pygame.mixer.music.play()

            # Refreshes the display
            pygame.display.update()
            # Updates the clock by 50 frames per second
            self.clock.tick(50)

    def individual(self) -> None:
        """The page for Impact on Individual Industries. Display the 18 interactive buttons that
        opens up graphs that shows our computation on each of the individual industries.
        """
        # Assigns width, height to elements of the dimension
        w, h = self.dimension
        # Creates an infinite while loop
        while True:
            # Background colour of the screen
            self.screen.fill((255, 255, 255))
            # Get the mouse cursor position
            mouse = pygame.mouse.get_pos()
            # Get events
            for event in pygame.event.get():
                # Terminate the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Tracks if the mouse clicks on the Back button
                if self.buttons['back'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    # Brings the user to the start_menu function
                    pygame.mixer.music.play()
                    self.start_menu()

                # Assign industries to a list of button names
                industries = ['Total', 'Goods-producing', 'Agriculture', 'Forestry', 'Utilities',
                              'Construction', 'Manufacturing', 'Services-producing', 'Wholesale',
                              'Transportation', 'Finance', 'Professional', 'Business',
                              'Educational', 'Health', 'Information', 'Accommodation',
                              'Other']
                for industry in industries:
                    # Tracks if the mouse clicks on a specific industry button
                    if self.buttons[industry].mouse_hover(
                            mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.music.play()
                        # Assign the Visualization class to v
                        v = Visualization()
                        # Display the corresponding individual industry graph
                        v.display_individual_graphs(industry)
                        # Display the corresponding covid visualization graph
                        v.display_industry_covid(industry)

            # Draws text using the draw_text function
            self.draw_text(self.screen,
                           'CO(VISION): COVID-19’s Impact on employment', 30,
                           (w // 2, h // 12 - 45))
            self.draw_text(self.screen,
                           'Impact on Individual Industries', 25, (w // 2, h // 12 + 20))

            # Display the buttons

            # Column 1
            self.buttons['Total'].draw(self.screen, 'Total employed, '
                                                    'all industries', 15)
            self.buttons['Goods-producing'].draw(self.screen, 'Goods-producing sector', 15)
            self.buttons['Agriculture'].draw(self.screen, 'Agriculture', 15)
            self.buttons['Forestry'].draw(
                self.screen, 'Forestry, fishing, mining, quarrying, oil and gas', 15)
            self.buttons['Utilities'].draw(self.screen, 'Utilities', 15)
            self.buttons['Construction'].draw(self.screen, 'Construction', 15)

            # column 2

            self.buttons['Manufacturing'].draw(self.screen, 'Manufacturing', 15)
            self.buttons['Services-producing'].draw(self.screen, 'Services-producing sector', 15)
            self.buttons['Wholesale'].draw(self.screen, 'Wholesale and retail trade', 15)
            self.buttons['Transportation'].draw(self.screen, 'Transportation and warehousing', 15)
            self.buttons['Finance'].draw(self.screen, 'Finance, insurance, real estate, rental and '
                                                      'leasing', 15)
            self.buttons['Professional'].draw(self.screen, 'Professional, scientific and technical '
                                                           'services', 15)

            # column 3

            self.buttons['Business'].draw(self.screen, 'Business, building and other support '
                                                       'services', 15)
            self.buttons['Educational'].draw(self.screen, 'Educational services', 15)
            self.buttons['Health'].draw(self.screen, 'Health care and social assistance', 15)
            self.buttons['Information'].draw(self.screen, 'Information, culture and recreation', 15)
            self.buttons['Accommodation'].draw(self.screen, 'Accommodation and food services', 15)
            self.buttons['Other'].draw(self.screen, 'Other services (except public administration)',
                                       15)

            self.buttons['back'].draw(self.screen, "Back", 20)

            # Refreshes the display
            pygame.display.update()
            # Updates the clock by 50 frames per second
            self.clock.tick(50)

    def all(self) -> None:
        """The page for Impact on All Industries. Displays the 4 interactive buttons for
        different graphs, related to 5 industries that have the highest, weakest, worst, or best
        correlation to employment rates and COVID.
        """
        # Assigns width, height to elements of the dimension
        w, h = self.dimension

        # Creates an infinite while loop
        while True:
            # Background colour of the screen
            self.screen.fill((255, 255, 255))
            # Get the mouse cursor position
            mouse = pygame.mouse.get_pos()
            # Assign the Visualization class to v
            v = Visualization()
            # Get events
            for event in pygame.event.get():
                # Terminate the program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Tracks if the mouse clicks on the Back button
                if self.buttons['back'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    # Brings the user to the start_menu function
                    self.start_menu()

                # Tracks if the mouse clicks on the Top Benefit button
                if self.buttons['Top Benefit'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    # Assign association to get_benefited_industries function in the
                    # visualization class
                    association = v.get_benefited_industries()
                    # Displays the graph of 5 industries with the steepest positive
                    # linear regression
                    v.display_multiple_associations(association, criteria="Benefited")

                # Tracks if the mouse clicks on the Top Suffer button
                if self.buttons['Top Suffer'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    # Assign association to get_struggling_industries function in the
                    # visualization class
                    association = v.get_struggling_industries()
                    # Displays the graph of 5 industries with the steepest negative
                    # linear regression
                    v.display_multiple_associations(association, criteria="Suffered")

                # Tracks if the mouse clicks on the Top Strong button
                if self.buttons['Top Positive'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    # Assign association to get_best_association function in the
                    # visualization class
                    association = v.get_best_association()
                    # Displays the graph of 5 industries with the highest correlations
                    v.display_multiple_associations(association, criteria="Positive correlations")

                # Tracks if the mouse clicks on the Top Weak button
                if self.buttons['Top Negative'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.play()
                    # Assign association to get_worst_association function in the
                    # visualization class
                    association = v.get_worst_association()
                    # Displays the graph of 5 industries with the smallest correlations
                    v.display_multiple_associations(association, criteria="Negative correlations")

            # Draws text using the draw_text function
            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment ',
                           55, (w // 2, h // 4))
            self.draw_text(self.screen, 'Impact on all industries',
                           45, (w // 2, h // 4 + 100))

            # Display the buttons
            self.buttons['Top Benefit'].draw(self.screen, "Top 5 Industries that benefited from "
                                                          "COVID", 20)
            self.buttons['Top Suffer'].draw(self.screen, "Top 5 Industries that suffered from"
                                                         " COVID", 20)
            self.buttons['Top Positive'].draw(self.screen, "Top 5 industries with positive "
                                                           "correlations", 20)
            self.buttons['Top Negative'].draw(self.screen, "Top 5 industries with negative "
                                                           "correlations", 20)
            self.buttons['back'].draw(self.screen, "Back", 20)

            # Refreshes the display
            pygame.display.update()
            # Updates the clock by 50 frames per second
            self.clock.tick(50)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': ['python_ta.contracts', 'pygame', 'button', 'sys', 'random',
                          'visualizations'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200', 'R1702'],
        'generated-members': ['pygame.*']
    })
