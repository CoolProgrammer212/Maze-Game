import pygame

# Initialize Pygame
pygame.init()

# Define colors
gold = (212, 175, 55)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Set up the window
window_width, window_height = 750, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

# Define obstacles. Format- ( x coord, y coord, x size, y size )
obstacles = [
    pygame.Rect(0, 0, 750, 50),
    pygame.Rect(60, 105, 50, 200),
    pygame.Rect(75, 50, 25, 5),
    pygame.Rect(200, 150, 400, 50),
    pygame.Rect(60, 290, 150, 50),
    pygame.Rect(180, 350, 200, 50),
    pygame.Rect(450, 420, 30, 200),
    pygame.Rect(200, 0, 25, 85),
    pygame.Rect(400, 0, 25, 85),
    pygame.Rect(500, 115, 25, 80),
    pygame.Rect(600, 0, 25, 85),
    pygame.Rect(300, 115, 25, 80),
    pygame.Rect(150, 260, 25, 40),
    pygame.Rect(660, 150, 100, 50),
    pygame.Rect(550, 250, 25, 250),
    pygame.Rect(550, 275, 125, 25),
    pygame.Rect(400, 200, 25, 75),
    pygame.Rect(300, 275, 25, 75),
    pygame.Rect(640, 375, 125, 25),
    pygame.Rect(0, 0, 5, 500),
    pygame.Rect(0, 0, 750, 5),
    pygame.Rect(745, 0, 5, 500),
    pygame.Rect(0, 495, 750, 5)
]

# Initialize player position and speed
player_x, player_y = 5, 445
player_speed = 1

# Initialize font
pygame.font.init()
font = pygame.font.SysFont("Constantia", 30)

# Initialize clock
clock = pygame.time.Clock()
FPS = 300  # Set desired frames per second

# Main loop
running = True
while running:
    clock.tick(FPS)  # Limit frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Draw everything
    window.fill((14, 14, 16))
    player = pygame.draw.rect(window, gold, (player_x, player_y, 50, 50))
    win = pygame.draw.rect(window, green, (675, 425, 70, 70))
    for obstacle in obstacles:
        pygame.draw.rect(window, red, obstacle)


    # Check for collisions
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            game_over_text = font.render('Game Over. Better Luck Next Time!', True, (150, 0, 0))
            window.blit(game_over_text, (150, 250))
            pygame.display.update()
            pygame.time.delay(2000)
            running = False

    if player.colliderect(win):
        you_win_text = font.render('Well Done! You Win!', True, (0, 255, 0))
        window.blit(you_win_text, (250, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    window.blit(font.render('Welcome to The Ultimate Maze Game!', True, gold), (150, 250))

    pygame.display.update()

# Quit Pygame properly
pygame.quit()
