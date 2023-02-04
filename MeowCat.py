import pygame
import random

clock = pygame.time.Clock()
update_interval = 5000 # 5 seconds
current_time = pygame.time.get_ticks()

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 500)
screen = pygame.display.set_mode(window_size)

# Load the cat image
cat_image = pygame.Surface((300, 400))
cat_image.fill((255, 255, 255))

# Define the cat's body
body_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
body_rect = pygame.Rect(50, 200, 200, 200)
pygame.draw.rect(cat_image, body_color, body_rect)

# Define the cat's head
head_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
head_width = 150
head_height = 150
head_rect = pygame.Rect(100, 100, head_width, head_height)
pygame.draw.ellipse(cat_image, head_color, head_rect)

# Define the cat's eyes
eye_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
eye_width = 30
eye_height = 30
eye_spacing = 70
left_eye_rect = pygame.Rect(125, 150, eye_width, eye_height)
right_eye_rect = pygame.Rect(155, 150, eye_width, eye_height)
pygame.draw.rect(cat_image, eye_color, left_eye_rect)
pygame.draw.rect(cat_image, eye_color, right_eye_rect)

# Define the cat's ears
ear_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
ear_width = 30
ear_height = 50
left_ear_rect = pygame.Rect(75, 100, ear_width, ear_height)
right_ear_rect = pygame.Rect(195, 100, ear_width, ear_height)
pygame.draw.rect(cat_image, ear_color, left_ear_rect)
pygame.draw.rect(cat_image, ear_color, right_ear_rect)

# Define the cat's nose
nose_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
nose_width = 20
nose_height = 20
nose_rect = pygame.Rect(165, 180, nose_width, nose_height)
pygame.draw.rect(cat_image, nose_color, nose_rect)

# Define the cat's whiskers
whisker_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
whisker_width = 5
whisker_height = 40
left_whisker_rect = pygame.Rect(140, 145, whisker_width, whisker_height)
right_whisker_rect = pygame.Rect(180, 145, whisker_width, whisker_height)
pygame.draw.rect(cat_image, whisker_color, left_whisker_rect)
pygame.draw.rect(cat_image, whisker_color, right_whisker_rect)

# Set the position of the cat on the screen
cat_pos = (50, 50)

# Set the font and color for the text
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)

# Set a flag to indicate if the "Meow!" text should be displayed
display_text = False

# Pre-render the "meow" text
text = font.render("Meow!", True, text_color)

# Create a clock object to limit the frame rate
clock = pygame.time.Clock()

# Start the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check if the mouse is within the bounds of the cat
            if cat_image.get_rect(topleft=cat_pos).collidepoint(mouse_pos):
                # Toggle the display_text flag
                display_text = not display_text

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the cat on the screen
    screen.blit(cat_image, cat_pos)

    # Display the "meow" text if the display_text flag is set
    if display_text:
        screen.blit(text, (200, 200))

    # Update the screen
    pygame.display.update()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
