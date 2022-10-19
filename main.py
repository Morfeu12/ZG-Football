from tkinter import Menu
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

# Cores
c_gray = (40,40,40)
c_white = (255,255,255)

# Carregando arquivos de imagem
background_menu = pygame.image.load("assets/mainmenu.jpg")
background = pygame.image.load("assets/field.png")
player1 = pygame.image.load("assets/BRL.png")
player2 = pygame.image.load("assets/ARG.png")
ball = pygame.image.load("assets/ball.png")
score1_img = pygame.image.load("assets/score/0.png")
score2_img = pygame.image.load("assets/score/0.png")
win = pygame.image.load("assets/win-old.png")

# Definição de variavel de controle
score1 = 0
score2 = 0
player1_y = 290
player1_y_up = False
player1_y_down = False
player2_y = 290
player2_y_up = False
player2_y_down = False
ball_x = 617
ball_y = 337
ball_direction = 3
ball_direction_Y = 5.3
game_run = False
menu_run = True
kick_p1 = True
kick_p2 = True

def screen_draw(): # Cria a interface
    if score1 < 10 and score2 < 10:
        screen.blit(background, (0, 0))
        screen.blit(player1, (50, player1_y))
        screen.blit(player2, (1150, player2_y))
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(score1_img, (500, 20))
        screen.blit(score2_img, (710, 20))
        moveball()
        auto_play()
        speedball()
    else: 
        screen.blit(win, (300, 300))
        if score1 > score2: 
            p1win = pygame.image.load("assets/p1win.png")
            screen.blit(p1win, (300,420))
        else: 
            p2win = pygame.image.load("assets/p2win.png")
            screen.blit(p2win, (300,420))
        playagain = fontsys.render("Press SPACE to play again", 1, c_gray)
        screen.blit(playagain, (430,650))

def auto_play(): # Jogo de demonstração
    global player2_y
    global player1_y
    #player2_y = ball_y
    #player1_y = ball_y

def slowball(): # Reduz a velocidade da bola
    global ball_direction

    if ball_direction < 0:
        if ball_direction <= -10:
            ball_direction = ball_direction + 5
        else: ball_direction = -5
    else: 
        if ball_direction >= 10:
            ball_direction = ball_direction - 5
        else: ball_direction = 5

def speedball(): # Aumenta a velocidade da bola
    global ball_direction

    maxspeed_x = 30

    if ball_direction < maxspeed_x and ball_direction > maxspeed_x*-1:
        if ball_direction < 0:
            ball_direction += -0.0075
        elif ball_direction > 0:
            ball_direction += 0.0075    

def moveball(): # Move a bola + pontuação
    global ball_x
    global ball_y
    global ball_direction
    global ball_direction_Y
    global score1
    global score2
    global score1_img
    global score2_img
    global kick_p1
    global kick_p2
    ball_x += ball_direction
    ball_y += ball_direction_Y
    # Colisão player 1
    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                if kick_p1 == True:
                    ball_direction *= -1
                    kick_p2 = True
                    kick_p1 = False
    # Colisão player 2
    if ball_x > 1110:
        if player2_y < ball_y + 23: # 23
            if player2_y + 146 > ball_y: # 146
                if kick_p2 == True:
                    ball_direction *= -1
                    kick_p2 = False
                    kick_p1 = True
    # Limite do campo
    if ball_y > 687:
        ball_direction_Y *= -1
    elif ball_y <= 0:
        ball_direction_Y *= -1
    # Reset posição bola + pontuação
    if ball_x < 81: #120px limite - metade da largura da imagem (39px)
        ball_x = 617
        ball_y = 337
        kick_p2 = True
        kick_p1 = True
        ball_direction *= -1
        ball_direction_Y *= -1
        score2 += 1
        score2_img = pygame.image.load(f'assets/score/{score2}.png')
        slowball()
    elif ball_x > 1149: #1110px limite + metade da largura da imagem (39px)
        ball_x = 617
        ball_y = 337
        kick_p2 = True
        kick_p1 = True
        ball_direction *= -1
        ball_direction_Y *= -1 
        score1 += 1   
        score1_img = pygame.image.load(f'assets/score/{score1}.png')
        slowball()

def moveplayer(arg): # Move os jogadores
    if arg == 1:
        player = player1_y
        player_up = player1_y_up
        player_down = player1_y_down
    elif arg == 2: 
        player = player2_y
        player_up = player2_y_up
        player_down = player2_y_down
    if player_up:
        player -= 10
    else:
        player += 0
    if player_down:
        player += 10
    else:
        player += 0
    if player <= 0:
        player = 0
    elif player >= 575:
        player = 575
    return player

def restartgame(): # Reinicia o jogo com valores padrão
    global score1
    global score2
    global score1_img
    global score2_img
    global ball_direction
    global kick_p1
    global kick_p2
    score1 = 0
    score2 = 0
    score1_img = pygame.image.load("assets/score/0.png")
    score2_img = pygame.image.load("assets/score/0.png")
    ball_direction = 4
    kick_p1 = True
    kick_p2 = True

def menu(): # Tela inicial
    global menu_run
    global game_run
    while menu_run:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                menu_run = False
            if events.type == pygame.KEYDOWN: # Evento de precionar tecla
                if events.key == pygame.K_RETURN or events.key == pygame.K_KP_ENTER:
                    menu_run = False
                    game_run = True
        screen.blit(background_menu, (0,0))
        pressstart_txt = fontsys.render("< Press ENTER to play >", 1, c_white)
        screen.blit(pressstart_txt, (430,650))
        pygame.display.flip()
        pygame.time.Clock().tick()

def game(): # Tela do jogo. Fluxo do jogo
    global game_run
    global menu_run
    global player1_y
    global player2_y
    global player1_y_down
    global player1_y_up
    global player2_y_down
    global player2_y_up
    # Loop do jogo
    while game_run:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                game_run = False
            if events.type == pygame.KEYDOWN: # Evento de precionar tecla
                if events.key == pygame.K_w:
                    player1_y_up = True
                if events.key == pygame.K_s:
                    player1_y_down = True
                if events.key == pygame.K_UP:
                    player2_y_up = True
                if events.key == pygame.K_DOWN:
                    player2_y_down = True
                if events.key == pygame.K_SPACE and (score1 >= 10 or score2 >=10):
                    restartgame()
            if events.type == pygame.KEYUP: # Evento de soltar tecla
                if events.key == pygame.K_w:
                    player1_y_up = False
                if events.key == pygame.K_s:
                    player1_y_down = False
                if events.key == pygame.K_UP:
                    player2_y_up = False
                if events.key == pygame.K_DOWN:
                    player2_y_down = False        
        screen_draw()
        player1_y = moveplayer(1)
        player2_y = moveplayer(2)
        # Renderiza a tela
        pygame.display.flip()
        # Controla o FPS
        pygame.time.Clock().tick(60)

menu()
game()


