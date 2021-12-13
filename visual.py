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
import sys
import random
import pygame

from visualizations import Visualization
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
    font_name: str

    buttons: dict[str, Button]

    def __init__(self) -> None:
        """Initializes the visual class and its variables, and starts up the program.
        Uses the class Buttons.
        """
        pygame.init()
        self.font_name = "M1PRegular-R3wv.ttf"  # Sets up the font
        self.dimension = (1600, 1000)  # Sets the dimension for the screen (width, height)
        w, h = self.dimension
        self.screen = pygame.display.set_mode((w, h))

        pygame.display.set_caption('CO(VISION)')
        self.clock = pygame.time.Clock()
        # http://resources.finalsite.net/images/v1603987533/ellensburg/ixbajjxlqntul6ymrofc/COVID.jpg
        pygame.display.set_icon(pygame.image.load('COVID.jpg'))
        self.virus_pic = pygame.image.load('virus.png')
        self.virus_rect = self.virus_pic.get_rect()

        small_button_width = 400
        c1_x = w // 4 - 50  # column_1's x position
        c2_x = w // 2  # column_2's x position
        c3_x = w // 2 + w // 4 + 50  # column_3's x position

        # Position of buttons on the screen
        self.buttons = {'back': Button((100, 50), (50, 25)),
                        'individual': Button((500, 150), (w // 2 - 50, h // 2 + 50)),
                        'all': Button((500, 150), (w // 2 - 50, h // 2 + 200)),

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
                        'Top Strong': Button((500, 150), (w - w // 3 + 50, h // 2 + 50)),
                        'Top Weak': Button((500, 150), (w - w // 3 + 50, h // 2 + 250))
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
                    sys.exit()
                if self.buttons['individual'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    self.individual()
                if self.buttons['all'].mouse_hover(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.all()

            self.screen.blit(self.virus_pic, self.virus_rect)
            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment',
                           50, (w // 2, h // 4))
            self.draw_text(self.screen, 'How does  the  pandemic  impact  employment  in  Ontario?',
                           40, (w // 2, h // 3))
            self.draw_text(self.screen,
                           'Are  there  certain  industries  that  suffered or '
                           'benefited more than others?', 40, (w // 2, h // 3 + 50))
            self.buttons['individual'].draw(self.screen, "Individual Comparisons", 35)
            self.buttons['all'].draw(self.screen, "All Comparisons", 35)

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
        w, h = self.dimension
        while True:  # Infinite while loop
            self.screen.fill((255, 255, 255))  # Background colour of the screen
            mouse = pygame.mouse.get_pos()  # Tracks the mouse and its interactions with events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.buttons['back'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_menu()

                industries = ['Total', 'Goods-producing', 'Agriculture', 'Forestry', 'Utilities',
                              'Construction', 'Manufacturing', 'Services-producing', 'Wholesale',
                              'Transportation', 'Finance', 'Professional', 'Business',
                              'Educational', 'Health', 'Information', 'Accommodation',
                              'Other']
                for industry in industries:
                    if self.buttons[industry].mouse_hover(
                            mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                        # print("Begin Run")
                        v = Visualization()
                        v.display_individual_graphs(industry)
                        v.industry_covid_visualization(industry)
                        # plt.plot([1, 2, 3, 4])
                        # plt.ylabel('some numbers')
                        # plt.show()
                        # print("Ran Successfully")
            self.draw_text(self.screen,
                           'CO(VISION): COVID-19’s Impact on employment Impact on Individual '
                           'Industries', 30, (w // 2, h // 12))

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
            pygame.display.update()
            self.clock.tick(50)

    def all(self) -> None:
        """The all menu of the program
        """
        w, h = self.dimension

        while True:
            self.screen.fill((255, 255, 255))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.buttons['back'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_menu()

                if self.buttons['Top Benefit'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    v = Visualization()
                    association = v.get_benefited_industries()
                    v.display_multiple_associations(association, criteria="Benefited")
                    # association = v.get_best_association()
                    # v.display_multiple_associations(association, criteria="Best Association")

                if self.buttons['Top Suffer'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    v = Visualization()
                    # association = v.get_worst_association()
                    # v.display_multiple_associations(association, criteria="Worst Association")
                    association = v.get_struggling_industries()
                    v.display_multiple_associations(association, criteria="Suffered")

                if self.buttons['Top Strong'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                if self.buttons['Top Weak'].mouse_hover(mouse) and \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.draw_text(self.screen, 'CO(VISION): COVID-19’s Impact on employment ',
                           60, (w // 2, h // 4))
            self.draw_text(self.screen, 'Impact on all industries',
                           60, (w // 2, h // 4 + 70))

            self.buttons['Top Benefit'].draw(self.screen, "Top 5 Industries that benefited from "
                                                          "COVID", 20)
            self.buttons['Top Suffer'].draw(self.screen, "Top 5 Industries that suffered from"
                                                         " COVID", 20)
            self.buttons['Top Strong'].draw(self.screen, "Top 5 industries with strong "
                                                         "correlations", 20)
            self.buttons['Top Weak'].draw(self.screen, "Top 5 industries with weak "
                                                       "correlations", 20)
            self.buttons['back'].draw(self.screen, "Back", 20)

            pygame.display.update()  # Refreshes the display
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
        'disable': ['R1705', 'C0200'],
        'generated-members': ['pygame.*']
    })
