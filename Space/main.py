import pygame 
import sys, os, time

pygame.init()
largura,altura = 1200,650
display = pygame.display.set_mode((largura,altura))
fundo=pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
nave=pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))

navRec= nave.get_rect(center=(500,500))
print(navRec)

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
   
    display.blit(bg1, bgR1)
    display.blit(nave, navRec)
    if navRec.y >=10:
        navRec.y -=1
    
   # display.blit(nave, (200,pos_y))
   # pos_y-=1 
   # if pos_y < 0:
   #     pos_y =720
    pygame.display.update()

    #Limitando os Frames
    relogio.tick(30)
    
    end = int(round(time.time()*1000))
    
    print(f"{end-start} ms")
   
    display.blit(texto, recText)

    pygame.display.update()

pygame.quit()