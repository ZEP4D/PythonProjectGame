import random

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
Hublist = {}
LineList = {}
Fuellist = {}
AmmoList = {}
SuppleList  = {}
GotoExit=False
Dodawaaniehubbool = False
MaxNumbers_hubs = 7
Inthemoment = 0
punk_start = None
Punkt_Start_klucz = ""
Punkt_End_klucz = ""

def NumbersHubs(x,y):
    global MaxNumbers_hubs,Inthemoment,Dodawaaniehubbool
    hubid  = "HBID"+str(Inthemoment)

    if Inthemoment < MaxNumbers_hubs:
        new_ret = pygame.Rect(x, y, 20, 20)

        Hublist[hubid] = new_ret
        Infopanel(hubid)
        Inthemoment = Inthemoment +1
        Dodawaaniehubbool = False

def DodawanieHub():
    global Dodawaaniehubbool
    Dodawaaniehubbool = True

def Line(position,Hubkey):
    global punk_start, Punkt_Start_klucz, Punkt_End_klucz

    if punk_start is None:
        punk_start = position
        Punkt_Start_klucz = Hubkey
    else:
        punk_konca = position
        Punkt_End_klucz = Hubkey
        new_line = (punk_start,punk_konca)

        exits  = any(
            (line[0] == new_line[1] and line[1] == new_line[1]) or
            (line[0] == new_line[1] and line[1] == new_line[0])
            for line in LineList
        )
        if not exits:
            TrasaHub = Punkt_Start_klucz + "->" + Punkt_End_klucz
            LineList[TrasaHub] = new_line

        punk_start = None
        Punkt_Start_klucz = ""

def SetGoToExit():
    global GotoExit
    GotoExit=True

def Infopanel(id):
    Fuel = random.randint(1, 10)
    Ammo = random.randint(1, 10)
    Supple = random.randint(1, 10)

    Fuellist[id] = Fuel
    AmmoList[id] = Ammo
    SuppleList[id] = Supple

def ShowInfohubs(id):


    HubID = font1.render(str(id), True, "black")
    IDShowRect = HubID.get_rect()
    IDShowRect.x = 250
    IDShowRect.y = 150
    screen.blit(HubID, IDShowRect)



    HubAmmo = font1.render(str(AmmoList[id]), True, "black")
    AmmoShowRect = HubAmmo.get_rect()
    AmmoShowRect.x = 250
    AmmoShowRect.y = 200
    screen.blit(HubAmmo, AmmoShowRect)

    HubFuel = font1.render(str(Fuellist[id]), True, "black")
    FuelShowRect = HubFuel.get_rect()
    FuelShowRect.x = 250
    FuelShowRect.y = 250
    screen.blit(HubFuel, FuelShowRect)

    HubSupple = font1.render(str(SuppleList[id]), True, "black")
    SuppleShowRect = HubSupple.get_rect()
    SuppleShowRect.x = 250
    SuppleShowRect.y = 300
    screen.blit(HubSupple, SuppleShowRect)

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
AddHub = Button(screen,10,400,70,20, text='DodajHub', onClick=lambda:DodawanieHub())
#--------------
#Down panel



ExitButton = Button(screen,350,670,50,50, text='Exit', onClick=lambda: SetGoToExit())
SettingButton = Button(screen,0,670,50,50, text='Setting', onClick=lambda: print("hello"))

leftpanel = pygame.Rect(401,0,900,720)
enem = pygame.draw.rect(screen, "yellow", (800, 250, 30, 30))
Whatid = ''
Hubexist = False
while running:
    screen.fill("white")
    dt = clock.tick(60) / 1000
    Zegar(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                x, y = pygame.mouse.get_pos()
                pose = pygame.mouse.get_pos()

                if Dodawaaniehubbool:
                    if leftpanel.collidepoint(pose):
                        NumbersHubs(x ,y)
                        Hubexist = True

                for i in Hublist:
                    if Hublist[i].collidepoint(pygame.mouse.get_pos()):
                        Whatid = i


            elif pygame.mouse.get_pressed(3)[2]:

                for i in Hublist:
                    if Hublist[i].collidepoint(pygame.mouse.get_pos()):
                        Line(Hublist[i].center,i)

    #lewa Strona Modul operacji
    pygame.draw.rect(screen,"purple",(0,0,400,720))
    pygame.draw.rect(screen,"grey",(0,160,400,500))
    pygame.draw.rect(screen,"white",(0,650,400,100))

    #Prawa Strona Modul mapy
    pygame.draw.rect(screen,"grey",leftpanel)

    HubShow = font1.render(str(Inthemoment), True, "black")
    MaxShowRect = HubShow.get_rect()
    MaxShowRect.x = 350
    MaxShowRect.y = 40
    screen.blit(HubShow, MaxShowRect)

    if Hubexist:
        ShowInfohubs(Whatid)

    for s in LineList:
        Pose = LineList[s]
        pygame.draw.line(screen,"black",Pose[0],Pose[1],width=5)

    for i in Hublist:
        pygame.draw.rect(screen,"red",Hublist[i])



    Wyswielanie()
    pygame.draw.line(screen, "black", (400, 0), (400, 720), width=3)

    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

    if GotoExit:
        running = False

pygame.quit()
