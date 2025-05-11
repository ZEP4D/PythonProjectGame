import sys
from importlib.util import source_hash

import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle

#core
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
font1 = pygame.font.Font('Font/IBMPlexMono-Regular.ttf',32)
Rectlist = []

#--------------------------
#Zegar
minutes = 0
hours = 7
time_speed = 1
time_passed = 0
changeTime = 0

def Zegar(dt):
    global minutes,hours,time_passed

    time_passed = time_passed + dt * time_speed
    if time_passed >= 1:
        minutes= minutes + 1
        time_passed = 0
        
        if minutes >=60:
            hours += minutes // 60
            minutes %= 60
        if hours >= 24:
            hours %= 24


def Wyswielanie():
    czas=f"{hours:02}:{minutes:02}"
    showTime = font1.render(czas,True,"red")
    showTimeRect= showTime.get_rect()
    showTimeRect.x = 150
    showTimeRect.y = 20
    screen.blit(showTime,showTimeRect)

def Zmiennczas(t):
    global time_speed
    time_speed= t


StopButton = Button(screen,130,60,30,20, text='||', onClick= lambda:Zmiennczas(0))
Speed1Button = Button(screen,160,60,30,20, text='>', onClick=lambda:Zmiennczas(1))
Speed2Button = Button(screen,190,60,30,20, text='>>',onClick=lambda:Zmiennczas(10))
Speed3Button = Button(screen,220,60,30,20, text='>>',onClick=lambda:Zmiennczas(20))
#---------------
#Mainpanel
#--------------
#Down panel

GotoExit=False
def SetGoToExit():
    global GotoExit
    GotoExit=True


ExitButton = Button(screen,350,670,50,50, text='Exit', onClick=lambda: SetGoToExit())
SettingButton = Button(screen,0,670,50,50, text='Setting', onClick=lambda: print("hello"))

enem = pygame.draw.rect(screen, "yellow", (800, 250, 30, 30))

while running:
    screen.fill("white")
    dt = clock.tick(60) / 1000
    Zegar(dt)



    for i in Rectlist:
        pygame.draw.rect(screen,"red",i)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            new_ret=pygame.Rect(x,y,20,20)
            Rectlist.append(new_ret)


    #lewa Strona Modul operacji
    pygame.draw.rect(screen,"purple",(0,0,400,720))
    pygame.draw.rect(screen,"grey",(0,360,400,360))
    pygame.draw.rect(screen,"white",(0,650,400,100))


    #Prawa Strona Modul mapy



    Wyswielanie()
    pygame.draw.line(screen, "black", (400, 0), (400, 720), width=3)

    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

    if (GotoExit):
        pygame.quit()

pygame.quit()
