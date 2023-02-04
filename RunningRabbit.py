import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 400))

# Define the colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

# Draw the grass
screen.fill(GREEN)
pygame.draw.rect(screen, WHITE, (0, 300, 600, 100))

# Draw the rabbit
def draw_rabbit(x, y):
    # Draw the body
    pygame.draw.ellipse(screen, GREY, (x, y, 60, 80))

    # Draw the ears
    pygame.draw.polygon(screen, GREY, [(x-25, y-30), (x-5, y-50), (x+15, y-30)])

    # Draw the eyes
    pygame.draw.circle(screen, WHITE, (x-10, y-10), 5)
    pygame.draw.circle(screen, WHITE, (x+10, y-10), 5)

    # Draw the nose
    pygame.draw.circle(screen, GREY, (x, y), 5)

    # Draw the whiskers
    pygame.draw.line(screen, GREY, (x-15, y+5), (x-30, y+15), 2)
    pygame.draw.line(screen, GREY, (x-15, y+5), (x-30, y-5), 2)
    pygame.draw.line(screen, GREY, (x+15, y+5), (x+30, y+15), 2)
    pygame.draw.line(screen, GREY, (x+15, y+5), (x+30, y-5), 2)

# Set the starting position of the rabbit
x = 300 - 30
y = 125

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                y -= 5
            elif event.key == pygame.K_DOWN:
                y += 5

    # Clear the screen
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (0, 300, 600, 100))

    # Draw the rabbit
    draw_rabbit(x, y)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
