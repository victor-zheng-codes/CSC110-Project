import pygame
from sys import exit

pygame.init()
w, h = 1600, 1000
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('CO(VISION)')
clock = pygame.time.Clock()

# http://resources.finalsite.net/images/v1603987533/ellensburg/ixbajjxlqntul6ymrofc/COVID.jpg
programIcon = pygame.image.load('COVID.jpg')
pygame.display.set_icon(programIcon)

virusPic = pygame.image.load('virus.png')
virusRect = virusPic.get_rect()

font_name = pygame.font.match_font('dubai')


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

    def draw(self, surface: pygame.display, text: str, size: int) -> None:
        """Draw the button onto a display
        """
        rect = pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        pygame.draw.rect(surface, pygame.Color(self.color), rect)
        surface.blit(text_surface, text_rect)

    def get_x_pos(self) -> tuple[int, int]:
        """Return the button's left and right x positions"""
        return self.x - self.w // 2, self.x + self.w // 2

    def get_y_pos(self) -> tuple[int, int]:
        """Return the button's top and bottom y positions"""
        return self.y - self.h // 2, self.y + self.h // 2

    def mouse_hover(self, mouse: pygame.mouse) -> bool:
        """Return whether or not the mouse is on this button
        """
        if self.get_x_pos()[0] <= mouse[0] <= self.get_x_pos()[1] and \
                self.get_y_pos()[0] <= mouse[1] <= self.get_y_pos()[1]:
            return True


def draw_text(surface: pygame.display, text: str, size: int, x, y) -> None:
    """Draw the button onto a display
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x, y))

    surface.blit(text_surface, text_rect)


start = Button(500, 150, w // 2 - 50, h // 2 + 50, (245, 245, 245))
quit = Button(200, 200, w // 2 - 50, h // 2, (145, 15, 245))
graph1 = Button(100, 100, 30, 30, (255, 255, 255))


def start_menu():
    virusRect.topleft = (0, 0)
    xvelocity = 100
    yvelocity = 60
    while True:
        screen.fill((255, 255, 255))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if start.mouse_hover(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main()
        screen.blit(virusPic, virusRect)
        draw_text(screen, 'CO(VISION): COVID-19’s Impact on employment', 70, w / 2, h / 4)
        draw_text(screen, 'How does  the  pandemic  impact  employment  in  Ontario?', 50, w / 2, h / 3)
        draw_text(screen, 'Are  there  certain  industries  that  suffered  orbenefited more than others?', 50, w / 2,
                  h / 3 + 50)
        start.draw(screen, "Individual Comparison", 50)

        virusRect.x += xvelocity
        virusRect.y += yvelocity

        if virusRect.x + virusRect.w > w:
            xvelocity = -xvelocity
        if virusRect.x < 0:
            xvelocity = -xvelocity
        if virusRect.y + virusRect.h > h:
            yvelocity = -yvelocity
        if virusRect.y < 0:
            yvelocity = -yvelocity

        pygame.display.update()
        clock.tick(50)


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

            if graph1.mouse_hover(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("hello")
        graph1.draw(screen, 'hi', 30)
        quit.draw(screen, 'bye', 30)
        pygame.display.update()
        clock.tick(30)


start_menu()
