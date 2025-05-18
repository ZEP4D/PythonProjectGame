import pygame
from pygame_widgets.textbox import TextBox

import Core
import Hub
from pygame_widgets.button import Button

Fuellist = {}
AmmoList = {}
SuppleList  = {}
minutes = 0
hours = 7
time_speed = 1
time_passed = 0
changeTime = 0
Infobool=False
Consbool=False
Sendbool=False
Odrderbool=False
Magazinebool=False


def Zegar(dt):
    global minutes, hours, time_passed

    time_passed = time_passed + dt * time_speed
    if time_passed >= 1:
        minutes = minutes + 1
        time_passed = 0

        if minutes >= 60:
            hours += minutes // 60
            minutes %= 60
        if hours >= 24:
            hours %= 24

def Wyswielanie():
    czas = f"{hours:02}:{minutes:02}"
    showTime = Core.font1.render(czas, True, "white")
    showTimeRect = showTime.get_rect()
    showTimeRect.x = 160
    showTimeRect.y = 75
    Core.screen.blit(showTime, showTimeRect)

def Zmiennczas(t):
    global time_speed
    time_speed = t

def ShowInfohubs(id):
    x = 150
    y = 300

    LineShow = Core.font2.render(str(id), True, "White")
    LineShowRect = LineShow.get_rect()
    LineShowRect.x = x
    LineShowRect.y = y
    Core.screen.blit(LineShow, LineShowRect)



    HubAmmo = Core.font2.render(str(Core.AmmoList[id]), True, "White")
    AmmoShowRect = HubAmmo.get_rect()
    AmmoShowRect.x = x
    AmmoShowRect.y = y+50
    Core.screen.blit(HubAmmo, AmmoShowRect)

    HubFuel = Core.font2.render(str(Core.Fuellist[id]), True, "White")
    FuelShowRect = HubFuel.get_rect()
    FuelShowRect.x = x
    FuelShowRect.y = y+100
    Core.screen.blit(HubFuel, FuelShowRect)

    HubSupple = Core.font2.render(str(Core.SuppleList[id]), True, "White")
    SuppleShowRect = HubSupple.get_rect()
    SuppleShowRect.x = x
    SuppleShowRect.y = y+150
    Core.screen.blit(HubSupple, SuppleShowRect)

    if  Core.LineList:
        Lineid = ""

        Keys = Core.LineList.keys()
        for i in Keys:
            if i.find(id) != -1:
                Lineid = i

        LineShow = Core.font2.render(str(Lineid), True, "White")
        LineShowRect = LineShow.get_rect()
        LineShowRect.x = x
        LineShowRect.y = y+200
        Core.screen.blit(LineShow, LineShowRect)

def panels(buttonnuber):
    global Infobool,Consbool,Sendbool,Odrderbool,Magazinebool

    match buttonnuber:
        case 0:
            AddHub.hide()
            OderButton.hide()
            addAmmoTB.hide()
            Infobool = True
            Consbool = False
            Sendbool = False
            Odrderbool = False
            Magazinebool = False
        case 1:
            AddHub.show()
            OderButton.hide()
            addAmmoTB.hide()
            Infobool = False
            Consbool = True
            Sendbool = False
            Odrderbool = False
            Magazinebool = False
        case 2:
            AddHub.hide()
            OderButton.hide()
            addAmmoTB.hide()
            Infobool = False
            Consbool = False
            Sendbool = True
            Odrderbool = False
            Magazinebool = False
        case 3:
            AddHub.hide()
            addAmmoTB.hide()
            Infobool = False
            Consbool = False
            Sendbool = False
            Odrderbool = True
            Magazinebool = False
        case 4:
            AddHub.hide()
            OderButton.hide()
            addAmmoTB.hide()
            Infobool = False
            Consbool = False
            Sendbool = False
            Odrderbool = False
            Magazinebool = True

def ShowMagazineinfo():
    x = 150
    y = 300

    Ammo = Core.font2.render(str(Core.Ammo), True, "White")
    AmmoShowRect = Ammo.get_rect()
    AmmoShowRect.x = x
    AmmoShowRect.y = y + 50
    Core.screen.blit(Ammo, AmmoShowRect)

    Fuel = Core.font2.render(str(Core.Fuel), True, "White")
    FuelShowRect = Fuel.get_rect()
    FuelShowRect.x = x
    FuelShowRect.y = y + 100
    Core.screen.blit(Fuel, FuelShowRect)

    Supple = Core.font2.render(str(Core.Supple), True, "White")
    SuppleShowRect = Supple.get_rect()
    SuppleShowRect.x = x
    SuppleShowRect.y = y + 150
    Core.screen.blit(Supple, SuppleShowRect)

def ShowOrderinfo():
    OderButton.show()
    addAmmoTB.show()

def Order():
    if addAmmoTB.getText():
        Core.CreateOrder(0,int(addAmmoTB.getText()))
        if Core.Submitbool:
            addAmmoTB.setText(" ")
#-----------------------------------------------------------------------------------------------------------------------
Buttonimage = pygame.image.load("Texture/Interface/Pause.png")
Buttonimage = pygame.transform.scale(Buttonimage, (40, 40))
StopButton = Button(Core.screen, 60, 70, 40, 40, image=Buttonimage, onClick=lambda: Zmiennczas(0))

Speed1image = pygame.image.load("Texture/Interface/1x.png")
Speed1image = pygame.transform.scale(Speed1image, (40, 40))
Speed1Button = Button(Core.screen, 100, 70, 40, 40, image=Speed1image, onClick=lambda: Zmiennczas(1))
Speed2image = pygame.image.load("Texture/Interface/2x.png")
Speed2image = pygame.transform.scale(Speed2image, (40, 40))
Speed2Button = Button(Core.screen, 260, 70, 40, 40, image=Speed2image, onClick=lambda: Zmiennczas(10))
Speed3image = pygame.image.load("Texture/Interface/3x.png")
Speed3image = pygame.transform.scale(Speed3image, (40, 40))
Speed3Button = Button(Core.screen, 300, 70, 40, 40, image=Speed3image, onClick=lambda: Zmiennczas(20))

Textura0 = pygame.image.load("Texture/Interface/Grafika01.png").convert_alpha()
Textura0 = pygame.transform.scale(Textura0,(400,720))
Surface0 = pygame.Surface((400,720))
Surface0.blit(Textura0, (0,0))

AddHub = Button(Core.screen,300,400,70,20, text='DodajHub', onClick=lambda:Hub.DodawanieHub())
AddHub.hide()

OderButton = Button(Core.screen,150,450,100,50,text="Order", onClick=lambda: Core.SubmitOrder())
OderButton.hide()
infobutton = Button(Core.screen,20,300,80,40, text="info",colour="green",onClick= lambda: panels(0))
ConsButton = Button(Core.screen,20,365,80,40, text="Cons",colour="green",onClick= lambda: panels(1))
SendButton = Button(Core.screen,20,430,80,40, text="Send",colour="green",onClick= lambda: panels(2))
OrderButton = Button(Core.screen,20,495,80,40, text="Order",colour="green",onClick= lambda: panels(3))
Magazine = Button(Core.screen,20,560,80,40, text="Magazine",colour="green",onClick= lambda: panels(4))

ExitButton = Button(Core.screen,350,670,50,30, text='Exit', onClick=lambda: Core.SetGoToExit())
SettingButton = Button(Core.screen,0,670,50,30, text='Setting', onClick=lambda: print("hello"))

#--------------------------------------------------
addAmmoTB = TextBox(Core.screen,150,400,100,50,fontSize=20, onSubmit=Order)
addAmmoTB.hide()


#--------------------------------------------------

