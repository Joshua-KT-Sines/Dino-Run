import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load('Pygame/Dino Run/graphics/Player/player_walk_1.png')
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0
    def player_input(self):
        keys = pygame.key.get_pressed
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
    def apply_gravity(self):
        self.gravity += .25
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300


def display_score(start_time):
    # gives the time since the game started in milliseconds
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f"Score: {current_time//1000}", False, (64,64,64))
    score_rect = score_surface.get_rect(center = (width/2,50))
    screen.blit(score_surface, score_rect)
    return current_time//1000
def obstacle_movement(obstacle_list): 
    global difficulty, snail_surface, fly_surface
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 4 + difficulty
            if obstacle_rect.bottom == 300:
                screen.blit(snail_animation(), obstacle_rect)
            else:
                screen.blit(fly_animation(), obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right >= 0]
    return obstacle_list
def check_collision():
    global player_rect, obstacle_rect_list
    if obstacle_rect_list:
        for i in obstacle_rect_list:
            if player_rect.colliderect(i):
                return False
            else:
                pass
    return True
def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.05
        if player_index >= len(player_run):
            player_index = 0
        player_surface = player_run[int(player_index)]
    # play walking animation if waling animation if player is on floor 
    # play jump animation if player is not on the floor
def fly_animation():
    global fly_surface, fly_index
    fly_index += 0.05
    if fly_index >= len(fly_surfaces):
        fly_index = 0
    fly_surface = fly_surfaces[int(fly_index)]
    return fly_surface
def snail_animation():
    global snail_surface, snail_index

    snail_index += 0.02
    if snail_index >= len(snail_surfaces):
        snail_index = 0
    snail_surface = snail_surfaces[int(snail_index)]
    return snail_surface
    
# This starts pygame
pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
pygame.display.set_caption("title")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Pygame/Dino Run/font/Pixeltype.ttf", 50)
game_active =True
start_time = 0
difficulty = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

test_surface = pygame.Surface((100, 200))

floor_surface = pygame.image.load('Pygame\Dino Run\graphics\ground.png').convert_alpha()
sky_surface = pygame.image.load('Pygame\Dino Run\graphics\Sky.png').convert_alpha()




player_stand = pygame.image.load("Pygame/Dino Run/graphics/Player/player_stand.png").convert_alpha()

player_run1 = pygame.image.load('Pygame\Dino Run\graphics\Player\player_walk_1.png').convert_alpha()
player_run2 = pygame.image.load('Pygame\Dino Run\graphics\Player\player_walk_2.png').convert_alpha()
player_run = [player_run1, player_run2]
player_index = 0
player_jump = pygame.image.load('Pygame\Dino Run\graphics\Player\jump.png').convert_alpha()


player_surface = player_run[player_index]
# Places a rectangle around a surface
player_rect = player_surface.get_rect(midbottom = (80,300) )
player_gravity = 0


# Scales player_stand by 2 and rotates it by 0 degrees
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (width//2, height//2))




# # renders the text surface 
# score_surface = test_font.render("Josh's Game", False, (64,64,64))
# score_rect = score_surface.get_rect(center = (width/2,50))

# Makes the test_surface Red
test_surface.fill('Red')

# obstacles
# .convert() converts the image into something that pygame can work with more efficiently
snail_surface1 = pygame.image.load("Pygame/Dino Run/graphics/snail/snail1.png").convert_alpha()
snail_surface2 = pygame.image.load("Pygame/Dino Run/graphics/snail/snail2.png").convert_alpha()
snail_surfaces = [snail_surface1,snail_surface2]
snail_index = 0 
snail_surface = snail_surfaces[snail_index]



# snail_rect = snail_surface.get_rect(midbottom = (600,300))

fly_surface1 = pygame.image.load('Pygame\Dino Run\graphics\Fly\Fly1.png').convert_alpha()
fly_surface2 = pygame.image.load('Pygame\Dino Run\graphics\Fly\Fly2.png').convert_alpha()
fly_surfaces = [fly_surface1, fly_surface2]
fly_index = 0
fly_surface = fly_surfaces[fly_index]


obstacle_rect_list = []

# creates a custom event every 900 milliseconds
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 700)

while True:
    # checks for inputs 
    for event in pygame.event.get():
        # allows the user to close the window
        if event.type == pygame.QUIT:
            # closes the window
            pygame.quit()

            # Stops ALL code that is currently running
            exit()
            
        # Checks to see if any key is being pressed 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom < 300:
                    pass
                else:
                    player_gravity = -10
            if event.key == pygame.K_r:
                if not game_active:
                    game_active = True
                    obstacle_rect_list.clear()
                else:
                    pass
            
            
        
        # # checks to see if any key is relased 
        # if event.type == pygame.KEYUP:
        #     pass
        
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                player_gravity = -10
        # # # checks if the mouse has been moved 
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        
    #     # # checks to see if the mouse has been pressed
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         print("mouse click")

    #     # # checks to see if the mouse has been relased
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         print("mouse up")

    # # puts test_surface on the frame in the top left corner
    # screen.blit(test_surface,(200,100))

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_animation().get_rect(midbottom = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_animation().get_rect(midbottom = (randint(900,1100),210)))
    if game_active:
 
        screen.blit(floor_surface,(0,300))
        screen.blit(sky_surface,(0,0))

        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect,20)
        # pygame.draw.line(screen,"Black",screen_rect.topleft, screen_rect.bottomright,25)

        # snail_rect.right -= 3 
        # if snail_rect.right < 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        player_gravity += .25    
        player_rect.top += player_gravity
        
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        
        # Obstacle movement
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        player_animation()
        screen.blit(player_surface,player_rect)
        player.draw(screen)
        
        game_active = check_collision()
        difficulty += .001
        # if player_rect.colliderect(snail_rect):
        #     game_active= False
        #     print("collide")
        # # all of the buttons on the keyboard and if they are being pressed or not
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")



        # # checks to see if the player is colliding with the snail
        # # returns 0 if false and 1 if true
        # if player_rect.colliderect(snail_rect):
        #     print("collision")

        # # gets the mouse posistion
        # mouse_position = pygame.mouse.get_pos()

        # # .collidepoint((x,y)) checks to see if the player is colliding with a certain point
        # if player_rect.collidepoint((mouse_position)):
        #     pass
        #     # returns a list for each key on the mouse [0] = left click, [1] = Middle click, [3] = right click
        #     print(pygame.mouse.get_pressed())
        #     print("Collision")
        final_score=display_score(start_time)
    final_score_surface = test_font.render(f"You scored: {final_score} Points. Press R to restart", True, (64,64,64))
    if not game_active:
        screen.fill((94,129,162))
        start_time = pygame.time.get_ticks()
        screen.blit(player_stand, player_stand_rect)
        screen.blit(final_score_surface, (80,20))
        difficulty = 0
        

    # Draw all of our elements
    # Updates everything
    pygame.display.update()
    

    # tells the computer to not run the while loop more than 60 times per second
    clock.tick(165)