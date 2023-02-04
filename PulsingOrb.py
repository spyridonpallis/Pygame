import pygame
import random
import math

WIDTH = 800
HEIGHT = 600

def create_glass_orb(screen, x, y, size, color):
    # Create the gradient effect by drawing multiple circles with different colors and alpha values
    for i in range(size, 0, -5):
        alpha = i / size * 255
        color_with_alpha = color + (alpha,)
        pygame.draw.circle(screen, color_with_alpha, (x, y), i)

    # Draw a white circle in the center to create the light source
    pygame.draw.circle(screen, (255, 255, 255), (x, y), size // 4)

def random_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    return (r, g, b)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
size = 50
color = random_color()

dragging = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if math.sqrt((event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2) <= size:
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            x, y = event.pos

    screen.fill((0, 0, 0))
    size = 50 + 25 * math.sin(pygame.time.get_ticks() / 500)
    color = random_color()
    create_glass_orb(screen, x, y, int(size), color)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
