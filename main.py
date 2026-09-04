import pygame

# Initialize Pygame
pygame.init()

# Set up the display
my_screen = pygame.display.set_mode((800, 600))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    my_screen.fill((230, 220, 240))  # Light gray background

    # Update the display
    pygame.display.update()
    
# Quit Pygame
pygame.quit()