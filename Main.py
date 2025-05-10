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

#--------------------------
#Zegar
minutes = 0
hours = 7
time_speed = 10
time_passed = 0
changeTime = 0

def Zegar(dt):
    global minutes,hours,time_passed

    time_passed = time_passed + dt
    if time_passed >= 1:
        minutes= minutes + time_speed
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


StopButton = Button(screen,130,60,30,20, text='||', onClick= lambda: Zmiennczas(0))
Speed1Button = Button(screen,160,60,30,20, text='>', onClick=lambda:Zmiennczas(10))
Speed2Button = Button(screen,190,60,30,20, text='>>',onClick=lambda:Zmiennczas(30))
Speed3Button = Button(screen,220,60,30,20, text='>>',onClick=lambda:Zmiennczas(50))
#---------------


while running:
    screen.fill("black")
    dt = clock.tick(60) / 1000
    Zegar(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print("Yes")

    #lewa Strona Modul operacji
    pygame.draw.rect(screen,"purple",(0,0,400,720))
    
    #Prawa Strona Modul mapy
    pygame.draw.rect(screen, "black", (401, 0, 880, 720))

    Wyswielanie()

    x = 410
    for row in range(8):
        y = 10
        for column in range(6):
            pygame.draw.rect(screen, "yellow", (x, y, 100, 100))
            y = y + 110
        x = x + 110


    pygame.draw.line(screen, "black", (400, 0), (400, 720), width=3)

    pygame_widgets.update(pygame.event.get())
    pygame.display.update()


pygame.quit()
