import pygame
from sys import exit

pygame.init()
w, h = 1600, 1000
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Unititled')
clock = pygame.time.Clock()


class Button:
    """The button class
    """
    color = tuple[int, int, int]
    w: int
    h: int
    x: int
    y: int

    def __init__(self, w: int, h: int, x: int, y: int, color: tuple[int, int, int]):
        """Initialize the variables
        """
        self.color = color
        self.w = w
        self.h = h
        self.x, self.y = x, y

    def draw(self, surface: pygame.display) -> None:
        """Draw the button onto a display
        """
        pygame.draw.rect(surface, pygame.Color(self.color), (self.x, self.y, self.w, self.h))

    def get_x_pos(self) -> tuple[int, int]:
        """Return the button's left and right x positions"""
        return self.x, self.x + self.w

    def get_y_pos(self) -> tuple[int, int]:
        """Return the button's top and bottom y positions"""
        return self.y, self.y + self.h

    def mouse_hover(self, mouse: pygame.mouse) -> bool:
        """Return whether or not the mouse is on this button
        """
        if self.get_x_pos()[0] <= mouse[0] <= self.get_x_pos()[1] and \
                self.get_y_pos()[0] <= mouse[1] <= self.get_y_pos()[1]:
            return True


start = Button(100, 100, w // 2 - 50, h // 2, (245, 245, 245))
quit = Button(200, 200, w // 2 - 50, h // 2, (145, 15, 245))


def start_menu():
    while True:
        screen.fill((0, 0, 0))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if start.mouse_hover(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
        start.draw(screen)
        pygame.display.update()
        clock.tick(30)


def main():
    while True:
        screen.fill((0, 0, 0))  # covers up anything from the start menu
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_menu()
            if quit.mouse_hover(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start_menu()

        quit.draw(screen)
        pygame.display.update()
        clock.tick(30)


start_menu()
