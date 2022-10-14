import pygame

# Para iniciar o pygame, sempre começa com esse código
pygame.init()
pygame.font.init() 

# Definindo as configurações da janela
size_width = 1280 # Eixo X
size_height = 720 # Eixo Y
size_screen = (size_width,size_height)
screen = pygame.display.set_mode(size_screen)

# Titulo que aparece na janela do game
title = pygame.display.set_caption("Zodia Games | Z-Football 2022")

# Icone que aparece na barra de tarefa quando o game estiver aberto
icon = pygame.image.load('assets/ico.png')
pygame.display.set_icon(icon)

# Fontes
font = pygame.font.get_default_font()
fontsys=pygame.font.SysFont(font, 50)
fontwin=pygame.font.SysFont(font, 80)     


# Carregando arquivos de imagem
background = pygame.image.load("assets/field.png")
player1 = pygame.image.load("assets/player1.png")
player2 = pygame.image.load("assets/player2.png")
ball = pygame.image.load("assets/ball.png")
score1_img = pygame.image.load("assets/score/0.png")
score2_img = pygame.image.load("assets/score/0.png")
win = pygame.image.load("assets/win.png")

score1 = 0
score2 = 9
player1_y = 290
player1_y_up = False
player1_y_down = False
player2_y = 290
player2_y_up = False
player2_y_down = False
ball_x = 617
ball_y = 337
ball_direction = -5
ball_direction_Y = 10


def screen_draw():
    if score1 or score2 < 10:
        screen.blit(background, (0, 0))
        screen.blit(player1, (50, player1_y))
        screen.blit(player2, (1150, player2_y))
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(score1_img, (500, 20))
        screen.blit(score2_img, (710, 20))
        move_ball()
        move_player()
        move_player2()
        ball_speed()
    else: 
        screen.blit(win, (300, 330))
        if score1 > score2: 
            winner_txt = "Player 1 won!"
        else: 
            winner_txt = "Player 2 won!"
        winner = fontwin.render(winner_txt, 1,(255,212,42), (0,128,0,5))
        playagain = fontsys.render("Press SPACE to play again", 1,(65,65,65))
        screen.blit(winner, (450,450))
        screen.blit(playagain, (430,650))


def move_player2():
    global player2_y
    global player1_y

    player2_y = ball_y
    #player1_y = ball_y

def move_ball():
    global ball_x
    global ball_y
    global ball_direction
    global ball_direction_Y
    global score1
    global score2
    global score1_img
    global score2_img

    ball_x += ball_direction
    ball_y += ball_direction_Y

    # Colisão player 1
    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_direction *= -1

    # Colisão player 2
    if ball_x > 1110:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_direction *= -1


    # Limite do campo
    if ball_y > 687:
        ball_direction_Y *= -1
    elif ball_y <= 0:
        ball_direction_Y *= -1

    # Reset bola + pontuação
    if ball_x < 35:
        ball_x = 617
        ball_y = 337
        ball_direction *= -1
        ball_direction_Y *= -1
        score2 += 1
        score2_img = pygame.image.load(f'assets/score/{score2}.png')
        
    elif ball_x > 1255:
        ball_x = 617
        ball_y = 337
        ball_direction *= -1
        ball_direction_Y *= -1 
        score1 += 1   
        score1_img = pygame.image.load(f'assets/score/{score1}.png')
    
    

def ball_speed():
    global ball_direction

    maxspeed_x = 30

    if ball_direction < maxspeed_x and ball_direction > maxspeed_x*-1:
        if ball_direction < 0:
            ball_direction += -0.01
        elif ball_direction > 0:
            ball_direction += 0.01




def move_player():
    global player1_y

    if player1_y_up:
        player1_y -= 10
    else:
        player1_y += 0

    if player1_y_down:
        player1_y += 10
    else:
        player1_y += 0

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575


run = True

while run:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.KEYDOWN: # Evento de precionar tecla
            if events.key == pygame.K_w:
                player1_y_up = True
            if events.key == pygame.K_s:
                player1_y_down = True
            if events.key == pygame.K_SPACE and (score1 >= 10 or score2 >=10):
                score1 = 0
                score2 = 0
                score1_img = pygame.image.load("assets/score/0.png")
                score2_img = pygame.image.load("assets/score/0.png") 

        if events.type == pygame.KEYUP: # Evento de precionar tecla
            if events.key == pygame.K_w:
                player1_y_up = False
            if events.key == pygame.K_s:
                player1_y_down = False
            

    screen_draw()
    




    pygame.display.update()


