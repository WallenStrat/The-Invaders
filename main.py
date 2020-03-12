import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Invaders"


def update():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Hello Allan & Peter")


def draw():
    pygame.display.update()


def init():
    pygame.init()
    icon = pygame.image.load("assets/comet_32x32px.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255, 255, 255))
    # TODO Draw a rectangle


def main():
    init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update()
        draw()

    pygame.quit()


if __name__ == '__main__':
    main()
