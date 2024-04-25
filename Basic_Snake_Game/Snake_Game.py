import pygame
import random

pygame.init()

game_over = False
end = False
FPS = 10
pixel_size = 20
score = 0
end_screen_time = 1

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pink = (255,0,255)

food_coordinates = []

snake_segments = [(20, 20)]
snake_direction = 'right'

screen_height = 500
screen_width = 500
window = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Snake_Game_1.0") 

def draw_screen():

    if not end:
        window.fill(black)
        draw_food()
        draw_snake()
        draw_score()
        pygame.display.update()
    else :
        end_screen()

def draw_score():
    text = (pygame.font.Font(None, 36)).render("Score: " + str(score), True, pink)
    window.blit(text, (10, 10))

def draw_food():
    if not food_coordinates:
        food_x = random.randrange(0, screen_width - pixel_size, pixel_size)
        food_y = random.randrange(0, screen_height - pixel_size, pixel_size)
        food_coordinates.append((food_x, food_y))

    for food in food_coordinates:
        pygame.draw.rect(window, red, (food[0], food[1], pixel_size, pixel_size))

def draw_snake():
    for segment in snake_segments:
        pygame.draw.rect(window, white, (segment[0], segment[1], pixel_size, pixel_size))

def move_snake():
    global snake_direction

    head = snake_segments[0]
    x, y = head

    if snake_direction == 'right':
        x += pixel_size
    elif snake_direction == 'left':
        x -= pixel_size
    elif snake_direction == 'up':
        y -= pixel_size
    elif snake_direction == 'down':
        y += pixel_size

    new_head = (x, y)
    snake_segments.insert(0, new_head)

    if len(snake_segments) > score + 1:
        snake_segments.pop()

def check_collision():
    global score,end

    head_x, head_y = snake_segments[0]
    if head_x < 0 or head_x >= screen_width or head_y < 0 or head_y >= screen_height:
        end = True

    if snake_segments[0] in snake_segments[1:]:
        end = True
    for food in food_coordinates:
        if snake_segments[0] == food:
            score += 1
            food_coordinates.clear()

def end_screen():
    global game_over

    window.fill(black)
    text = (pygame.font.Font(None, 55)).render("Final Score: " + str(score), True, pink)
    window.blit(text, (screen_width//4, screen_height//3))
    pygame.display.update()
    pygame.time.delay(end_screen_time*1000)
    game_over = True

def main():
    global game_over, snake_direction

    clock = pygame.time.Clock()
    while not game_over:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT] and snake_direction != 'left':
            snake_direction = 'right'
        elif key_pressed[pygame.K_LEFT] and snake_direction != 'right':
            snake_direction = 'left'
        elif key_pressed[pygame.K_UP] and snake_direction != 'down':
            snake_direction = 'up'
        elif key_pressed[pygame.K_DOWN] and snake_direction != 'up':
            snake_direction = 'down'

        move_snake()
        check_collision()
        draw_screen()

    pygame.quit()

if __name__ == '__main__':
    main()
