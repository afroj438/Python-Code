# import pygame
# import sys

# # Initialize pygame
# pygame.init()

# # Set up display
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Simple Ball Game")

# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# # Ball settings
# ball_radius = 20
# ball_x, ball_y = WIDTH // 2, HEIGHT // 2
# ball_speed_x, ball_speed_y = 5, 5

# # Main game loop
# running = True
# while running:
#     pygame.time.delay(30)  # Control game speed
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     # Move the ball
#     ball_x += ball_speed_x
#     ball_y += ball_speed_y
    
#     # Bounce off walls
#     if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
#         ball_speed_x *= -1
#     if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
#         ball_speed_y *= -1
    
#     # Drawing
#     screen.fill(WHITE)
#     pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
#     pygame.display.update()

# # Quit pygame
# pygame.quit()
# sys.exit()
