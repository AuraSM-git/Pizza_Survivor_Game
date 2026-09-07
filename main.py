import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
my_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Survivor")
icon = pygame.image.load("assets/pizza.png")
pygame.display.set_icon(icon)

# Load and scale the background image
background_image = pygame.image.load("assets/fondo.png")
background_image = pygame.transform.scale(background_image, (800, 600))

# Delivery man
delivery_man_image = pygame.image.load("assets/repartidor.png")
delivery_man_image = pygame.transform.scale(delivery_man_image, (64, 100))
delivery_man_x = 368
delivery_man_y = 440
delivery_man_x_change = 0
delivery_man_y_change = 0
delivery_man_speed = 1

def draw_delivery_man(x, y):
    my_screen.blit(delivery_man_image, (x, y))
    
# Enemy - dog

dog_image = pygame.image.load("assets/perro.png")
dog_image = pygame.transform.scale(dog_image, (54, 64))
dog_x = random.randint(0, 746)
dog_y = 0
dog_speed = 0.5

def draw_dog(x, y):
    my_screen.blit(dog_image, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delivery_man_x_change = -delivery_man_speed
            if event.key == pygame.K_RIGHT:
                delivery_man_x_change = delivery_man_speed
            if event.key == pygame.K_UP:
                delivery_man_y_change = -delivery_man_speed
            if event.key == pygame.K_DOWN:
                delivery_man_y_change = delivery_man_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                delivery_man_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                delivery_man_y_change = 0

    # Update the delivery man's position
    delivery_man_x += delivery_man_x_change
    delivery_man_y += delivery_man_y_change
    
    # Keep the delivery man within the screen boundaries
    if delivery_man_x < 0:
        delivery_man_x = 0
    if delivery_man_x > 736:
        delivery_man_x = 736
    if delivery_man_y < 0:
        delivery_man_y = 0
    if delivery_man_y > 500:
        delivery_man_y = 500
        
    # Update the dog's position
    dx = delivery_man_x - dog_x
    dy = delivery_man_y - dog_y
    distance = (dx**2 + dy**2) ** 0.5
    if distance > 0:
        dog_x += (dx / distance) * dog_speed
        dog_y += (dy / distance) * dog_speed

    # Fill the screen with the background image
    my_screen.blit(background_image, (0, 0))

    # Draw the delivery man
    draw_delivery_man(delivery_man_x, delivery_man_y)
    
    # Draw the dog
    draw_dog(dog_x, dog_y)

    # Update the display
    pygame.display.update()
    
# Quit Pygame
pygame.quit()