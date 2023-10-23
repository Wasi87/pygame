import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

initial_rect_height = 210
initial_circle_radius = 40
left_score = 0
right_score = 0


ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_vel = pygame.Vector2(10, 10)
rect = pygame.Rect(50, screen.get_height() / 2 - initial_rect_height / 2, 10, initial_rect_height)
rect2 = pygame.Rect(screen.get_width()-50,  screen.get_height() / 2 - initial_rect_height / 2, 10, initial_rect_height)

circle_radius = initial_circle_radius
rect_height = float(initial_rect_height)

def random_color():
    return random.choice(list(pygame.colordict.THECOLORS.keys()))

rect_color = random_color()
rect2_color = random_color()
ball_color = random_color()
background_color = random_color()
line_color = random_color()

frame_count = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)

    
    ball_collider = pygame.Rect(ball_pos.x - circle_radius, ball_pos.y - circle_radius, circle_radius*2, circle_radius*2)
    result = rect.colliderect(ball_collider) or rect2.colliderect(ball_collider)

    # if ball_pos.x + circle_radius >= screen.get_width() or ball_pos.x - circle_radius <= 0:
    if result:
        ball_vel.x *= -1
        rect_color = random_color()
        rect2_color = random_color()
        ball_color = random_color()
        background_color = random_color()
        line_color = random_color()
    if ball_pos.y + circle_radius >= screen.get_height() or ball_pos.y - circle_radius <= 0:
        ball_vel.y *= -1
        rect_color = random_color()
        rect2_color = random_color()
        ball_color = random_color()
        background_color = random_color()
        line_color = random_color()

    # if frame_count % 5 == 0:
    #     rect_color = random_color()
    # if frame_count % 5 == 1:
    #     rect2_color = random_color()
    # if frame_count % 5 == 2:
    #     ball_color = random_color()
    # if frame_count % 5 == 3:
    #     background_color = random_color()
    # if frame_count % 5 == 4:
    #     line_color = random_color()

    ball_vel.x += random.randrange(-2, 3)
    ball_vel.y += random.randrange(-2, 3) * 0.1
    ball_vel.x = pygame.math.clamp(ball_vel.x, -15, 15)
    ball_vel.y = pygame.math.clamp(ball_vel.y, -10, 10)


    
    
    ball_pos += ball_vel
    rect_height *= 0.999
    rect.height = rect_height
    rect2.height = rect_height
    circle_radius *= 0.999
    
    pygame.colordict

    pygame.draw.line(screen, line_color, (1280/2, 0), (1280/2, 720), 5)
    pygame.draw.circle(screen, ball_color, ball_pos, circle_radius)
    pygame.draw.rect(screen, rect_color, rect)
    pygame.draw.rect(screen, rect2_color, rect2)
    pygame.display.set_caption(str(left_score)+ '-' + str(right_score))



    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        if rect.y <= 0:
            rect.move_ip(0, 0) 
        else:
            rect.move_ip(0, -10)
    if keys[pygame.K_a]:
        if rect.y >= screen.get_height() - rect.height:
            rect.move_ip(0, 0)
        else:
            rect.move_ip(0, 10)
    if keys[pygame.K_u]:
        if rect2.y <= 0:
            rect2.move_ip(0, 0) 
        else:
            rect2.move_ip(0, -10)
    if keys[pygame.K_j]:
        if rect2.y >= screen.get_height() - rect.height:
            rect2.move_ip(0, 0)
        else:
            rect2.move_ip(0, 10)

  


    if ball_pos.x <= 0:
        right_score += 1
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        rect_height = float(initial_rect_height)
        circle_radius = initial_circle_radius

    
    elif ball_pos.x >= screen.get_width():
        left_score += 1
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        rect_height = float(initial_rect_height)
        circle_radius = initial_circle_radius

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    frame_count += 1