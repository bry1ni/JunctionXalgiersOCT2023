import numpy as np
import pygame

# Initialize Pygame
pygame.init()

# Set up the window
size = (512, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drawing Program")

# Set the background color to white
background_color = (255, 255, 255)
screen.fill(background_color)

# Set up drawing variables
drawing = False
last_pos = None
brush_size = 10
brush_color = (0, 0, 0)

# Set up color buttons
red_button = pygame.Rect(10, 10, 20, 20)
green_button = pygame.Rect(40, 10, 20, 20)
blue_button = pygame.Rect(70, 10, 20, 20)
black_button = pygame.Rect(130, 10, 20, 20)
reset_button = pygame.Rect(492, 10, 20, 20)

# Set up eraser button
eraser_button = pygame.Rect(100, 10, 20, 20, width=2, border_radius=2)
eraser_color = background_color  # Eraser color is set to background color initially

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if red_button.collidepoint(event.pos):
                brush_color = (255, 0, 0)  # Red
            elif green_button.collidepoint(event.pos):
                brush_color = (0, 255, 0)  # Green
            elif blue_button.collidepoint(event.pos):
                brush_color = (0, 0, 255)  # Blue
            elif black_button.collidepoint(event.pos):
                brush_color = (0, 0, 0)  # Black
            elif reset_button.collidepoint(event.pos):
                screen.fill(background_color) # Reset
            elif eraser_button.collidepoint(event.pos):
                brush_color = eraser_color  # Set brush color to eraser color
            else:
                drawing = True
                last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, brush_color, last_pos, pos, brush_size)
            last_pos = pos

    # Draw color buttons
    pygame.draw.rect(screen, (0, 0, 0), black_button)
    pygame.draw.rect(screen, (255, 0, 0), red_button)
    pygame.draw.rect(screen, (0, 255, 0), green_button)
    pygame.draw.rect(screen, (0, 0, 255), blue_button)
    pygame.draw.rect(screen, (255, 0, 0), reset_button)

    # Draw eraser button
    pygame.draw.rect(screen, background_color, eraser_button)

    # Update the screen
    pygame.display.flip()

    # Check for key press
    keys = pygame.key.get_pressed()
    cpt = 0
    if keys[pygame.K_y]:
        cpt += 1
        pygame.image.save(screen, f"drawDataset/Normal/Ydrawing{cpt}.png")
        print('Drawing saved.')
    if keys[pygame.K_n]:
        cpt += 1
        pygame.image.save(screen, f"drawDataset/Not Normal/Ndrawing{cpt}.png")
        print('Drawing saved.')

# Quit Pygame
pygame.quit()
