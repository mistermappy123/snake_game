import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [250, 150]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

reward_position = [random.randrange(1, (window_x // 10)) * 10,
                   random.randrange(1, (window_y // 10)) * 10]

reward_spawn = True

start_direction = 'LEFT'
change_to = start_direction

player_points = 0

def show_current_points(choice, color, font, size) :
    
    
    point_font = pygame.font.SysFont(font, size)
    
    point_surface = point_font.render('Points: ' + str(player_points), True, color)

    point_display_board = point_surface.get_rect()

    game_window.blit(point_surface, point_display_board)

def game_over():
    
    my_font = pygame.font.SysFont('Helvetica', 50)

    game_over_message = my_font.render('Points: ' + str(player_points), True, red)

    game_over_board = game_over_message.get_rect()

    game_over_board.midtop = (window_x / 2, window_y / 4)

    game_window.blit(game_over_message, game_over_board)
    pygame.display.flip()

    time.sleep(3)

    pygame.quit()

    quit()

#Moving the Snake 
while True: 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and start_direction != 'DOWN' :
        start_direction = 'UP'
    if change_to == 'DOWN' and start_direction != 'UP' :
        start_direction = 'DOWN'
    if change_to == 'LEFT' and start_direction != 'RIGHT' :
        start_direction = "LEFT"
    if change_to == 'RIGHT' and start_direction != 'LEFT' :
        start_direction = 'RIGHT'

    if start_direction == 'UP' :
        snake_position[1] -= 10
    if start_direction == 'DOWN' :
        snake_position[1] += 10
    if start_direction == 'LEFT' :
        snake_position[0] -= 10
    if start_direction == 'RIGHT' :
        snake_position[0] += 10

#Growing the Snake after every point earned
    snake_body.insert(0, list(snake_position))

    if snake_position[0] == reward_position[0] and snake_position[1] == reward_position[1] :
        player_points += 10
        reward_spawn = False 
    else:
        snake_body.pop()

    if not reward_spawn :
        reward_position = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]
    
    reward_spawn = True 
    game_window.fill(blue)

    for pos in snake_body :
        pygame.draw.rect(game_window, black, pygame.Rect(pos[0], pos[1], 10,10))
    pygame.draw.rect(game_window, white, pygame.Rect(reward_position[0], reward_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    #If snake collides with its own body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    show_current_points(1, white, 'sans serif', 20)

    pygame.display.update()

    fps.tick(snake_speed)