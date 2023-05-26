import pygame 
import sys, os, time

def update_laser(laser_list,speed=300):
    for laserREC in laser_list:
        laserREC.y -= round(speed*dt) # type: ignore
        if laserREC.midbottom[1] < 0:
            laser_list.remove(laserREC) 

def displayScore(display,font):
    score_text = str(f'S T A R - G A M E {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True,(178,34,34)) 
    recText = texto.get_rect(midleft=(30,15))
    display.blit(texto, recText)

pygame.init()
largura,altura = 1200,650
display = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
lasersurface = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurface = pygame.transform.scale(lasersurface,(4,40))

navRec= nave.get_rect(center=(500,500))
#laserREC = lasersurface.get_rect(midbottom=navRec.midtop)
# Carregando imagem de fundo
laser_list = []
#print(navRec)

bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
bgR1 = bg1.get_rect(center=((largura/2,(altura/2))))

font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True,(178,34,34))
recText = texto.get_rect(center=(70,10))

pygame.display.set_caption(("Space Combat"))
loop = True
pos_y = 300
relogio = pygame.time.Clock()

while loop:
    start = int(round(time.time()*1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            navRec.center = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Tiro {event.pos}")
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            laserREC = lasersurface.get_rect(midbottom=navRec.midtop)
            laser_list.append(laserREC)
          
   
    display.blit(bg1, bgR1)
    # Utilizando o retângulo para posicionar a nave
    display.blit(nave, navRec)

    displayScore(display=display,font=font)

    #Limitando os Frames
    dt = relogio.tick(120)/1000
    navRec.center = pygame.mouse.get_pos()
    # Desenhando o laser da nave
    update_laser(laser_list)
    for laserREC in laser_list:
        display.blit(lasersurface,laserREC)
        
    
    print(laser_list)
    #if navRec.y >=10:
    #    navRec.y -=1
    
   # display.blit(nave, (200,pos_y))
   # pos_y-=1 
   # if pos_y < 0:
   #     pos_y =720
    pygame.display.update()

    
    
    
    end = int(round(time.time()*1000))
    
    print(f"{end-start} ms")
   
    display.blit(texto, recText)

    pygame.display.update()

pygame.quit()