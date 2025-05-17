import random

import pygame
import pygame_widgets
from pygame_widgets.button import Button

#core
pygame.init()
SizeScreenHeight = 720
SizeScreenWidth = 1280
screen = pygame.display.set_mode((SizeScreenWidth,SizeScreenHeight))
clock = pygame.time.Clock()
running = True
font1 = pygame.font.Font('Font/digital-7.ttf',42)
font2 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',32)
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
Infobool=False
Consbool=False
Sendbool=False
Odrderbool=False
Magazinebool=False
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


    HubID = font2.render(str(id), True, "White")
    IDShowRect = HubID.get_rect()
    IDShowRect.x = 250
    IDShowRect.y = 150
    screen.blit(HubID, IDShowRect)



    HubAmmo = font2.render(str(AmmoList[id]), True, "White")
    AmmoShowRect = HubAmmo.get_rect()
    AmmoShowRect.x = 250
    AmmoShowRect.y = 200
    screen.blit(HubAmmo, AmmoShowRect)

    HubFuel = font2.render(str(Fuellist[id]), True, "White")
    FuelShowRect = HubFuel.get_rect()
    FuelShowRect.x = 250
    FuelShowRect.y = 250
    screen.blit(HubFuel, FuelShowRect)

    HubSupple = font2.render(str(SuppleList[id]), True, "White")
    SuppleShowRect = HubSupple.get_rect()
    SuppleShowRect.x = 250
    SuppleShowRect.y = 300
    screen.blit(HubSupple, SuppleShowRect)
#----Textury---------------
Textura0 = pygame.image.load("Texture/Interface/Grafika01.png").convert_alpha()
Textura0 = pygame.transform.scale(Textura0,(400,720))
Surface0 = pygame.Surface((400,720))
Surface0.blit(Textura0, (0,0))
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
    showTime = font1.render(czas,True,"white")
    showTimeRect= showTime.get_rect()
    showTimeRect.x = 160
    showTimeRect.y = 75
    screen.blit(showTime,showTimeRect)

def Zmiennczas(t):
    global time_speed
    time_speed= t
Buttonimage = pygame.image.load("Texture/Interface/Pause.png")
Buttonimage = pygame.transform.scale(Buttonimage,(40,40))
StopButton = Button(screen,60,70,40,40, image=Buttonimage, onClick= lambda:Zmiennczas(0))

Speed1image = pygame.image.load("Texture/Interface/1x.png")
Speed1image = pygame.transform.scale(Speed1image,(40,40))
Speed1Button = Button(screen,100,70,40,40, image=Speed1image, onClick=lambda:Zmiennczas(1))
Speed2image = pygame.image.load("Texture/Interface/2x.png")
Speed2image = pygame.transform.scale(Speed2image,(40,40))
Speed2Button = Button(screen,260,70,40,40, image=Speed2image,onClick=lambda:Zmiennczas(10))
Speed3image = pygame.image.load("Texture/Interface/3x.png")
Speed3image = pygame.transform.scale(Speed3image,(40,40))
Speed3Button = Button(screen,300,70,40,40, image=Speed3image,onClick=lambda:Zmiennczas(20))
#---------------
#Mainpanel
AddHub = Button(screen,300,400,70,20, text='DodajHub', onClick=lambda:DodawanieHub())
AddHub.hide()

def panels(buttonnuber):
    global Infobool,Consbool,Sendbool,Odrderbool,Magazinebool

    match buttonnuber:
        case 0:
            AddHub.hide()
            Infobool = True
            Consbool = False
            Sendbool = False
            Odrderbool = False
            Magazinebool = False
        case 1:
            AddHub.show()
            Infobool = False
            Consbool = True
            Sendbool = False
            Odrderbool = False
            Magazinebool = False
        case 2:
            AddHub.hide()
            Infobool = False
            Consbool = False
            Sendbool = True
            Odrderbool = False
            Magazinebool = False
        case 3:
            AddHub.hide()
            Infobool = False
            Consbool = False
            Sendbool = False
            Odrderbool = True
            Magazinebool = False
        case 4:
            AddHub.hide()
            Infobool = False
            Consbool = False
            Sendbool = False
            Odrderbool = False
            Magazinebool = True


infobutton = Button(screen,20,300,80,40, text="info",colour="green",onClick= lambda: panels(0))
ConsButton = Button(screen,20,365,80,40, text="Cons",colour="green",onClick= lambda: panels(1))
SendButton = Button(screen,20,430,80,40, text="Send",colour="green",onClick= lambda: panels(2))
OrderButton = Button(screen,20,495,80,40, text="Order",colour="green",onClick= lambda: panels(3))
Magazine = Button(screen,20,560,80,40, text="Magazine",colour="green",onClick= lambda: panels(4))

#--------------
#Down panel

ExitButton = Button(screen,350,670,50,30, text='Exit', onClick=lambda: SetGoToExit())
SettingButton = Button(screen,0,670,50,30, text='Setting', onClick=lambda: print("hello"))

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
                    if infobutton:
                        if Hublist[i].collidepoint(pygame.mouse.get_pos()):
                            Whatid = i


            elif pygame.mouse.get_pressed(3)[2]:

                for i in Hublist:
                    if Hublist[i].collidepoint(pygame.mouse.get_pos()):
                        Line(Hublist[i].center,i)

    #lewa Strona Modul operacji
    screen.blit(Textura0,(0,0))
    #Prawa Strona Modul mapy
    pygame.draw.rect(screen,"grey",leftpanel)

    HubShow = font2.render(str(Inthemoment), True, "black")
    MaxShowRect = HubShow.get_rect()
    MaxShowRect.x = 350
    MaxShowRect.y = 40
    screen.blit(HubShow, MaxShowRect)
    

    if Infobool:
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
