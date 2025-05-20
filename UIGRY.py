import pygame
from pygame_widgets.dropdown import Dropdown

import Core
import Hub
from pygame_widgets.button import Button


VAL_MINUTES = 0
VAL_HOURS = 6
VAL_PASSTIME = 0
VAL_CHANGETIME = 0
VAL_X = 150
VAL_Y = 300
BOOL_INFO=False
BOOL_INFO_OBJECT = False
BOOL_CONS=False
BOOL_SEND=False
BOOL_ORDER=False
BOOL_MAGAZINE=False
LIST_DROPDOWN_OPTION = ["h1"]


def DEF_CLOCK(dt):
    global VAL_MINUTES, VAL_HOURS, VAL_PASSTIME

    VAL_PASSTIME = VAL_PASSTIME + dt * Core.VAL_SPPEDTIME
    if VAL_PASSTIME >= 1:
        VAL_MINUTES = VAL_MINUTES + 1
        VAL_PASSTIME = 0

        if VAL_MINUTES >= 60:
            VAL_HOURS += VAL_MINUTES // 60
            VAL_MINUTES %= 60
        if VAL_HOURS >= 24:
            VAL_HOURS %= 24

def DEF_DISPLAY():
    czas = f"{VAL_HOURS:02}:{VAL_MINUTES:02}"
    showTime = Core.font1.render(czas, True, "white")
    showTimeRect = showTime.get_rect()
    showTimeRect.x = 160
    showTimeRect.y = 75
    Core.screen.blit(showTime, showTimeRect)

def DEF_CHANGETIME(t):
    Core.VAL_SPPEDTIME = t

def DEF_HIDE():
    BUTTON_ADDHUB.hide()
    BUTTON_ORDERCREATE.hide()
    DROPDOWN_HUBSELECT.hide()

def DEF_PANEL(buttonnuber):
    global BOOL_INFO,BOOL_CONS,BOOL_SEND,BOOL_ORDER,BOOL_MAGAZINE

    match buttonnuber:
        case 0:
            DEF_HIDE()
            BOOL_INFO = True
            BOOL_CONS = False
            BOOL_SEND = False
            BOOL_ORDER = False
            BOOL_MAGAZINE = False
        case 1:
            DEF_HIDE()
            BOOL_INFO = False
            BOOL_CONS = True
            BOOL_SEND = False
            BOOL_ORDER = False
            BOOL_MAGAZINE = False
        case 2:
            DEF_HIDE()
            BOOL_INFO = False
            BOOL_CONS = False
            BOOL_SEND = True
            BOOL_ORDER = False
            BOOL_MAGAZINE = False
        case 3:
            DEF_HIDE()
            BOOL_INFO = False
            BOOL_CONS = False
            BOOL_SEND = False
            BOOL_ORDER = True
            BOOL_MAGAZINE = False
        case 4:
            DEF_HIDE()
            BOOL_INFO = False
            BOOL_CONS = False
            BOOL_SEND = False
            BOOL_ORDER = False
            BOOL_MAGAZINE = True

def SHOW_INFO(id):


    LineShow = Core.font2.render("ID:"+str(id), True, "White")
    LineShowRect = LineShow.get_rect()
    LineShowRect.x = VAL_X
    LineShowRect.y = VAL_Y
    Core.screen.blit(LineShow, LineShowRect)

    HubAmmo = Core.font2.render("Ammo: "+str(Core.DICT_AMMO[id]), True, "White")
    AmmoShowRect = HubAmmo.get_rect()
    AmmoShowRect.x = VAL_X
    AmmoShowRect.y = VAL_Y+30
    Core.screen.blit(HubAmmo, AmmoShowRect)

    HubFuel = Core.font2.render("Fuel: "+str(Core.DICT_FUEL[id]), True, "White")
    FuelShowRect = HubFuel.get_rect()
    FuelShowRect.x = VAL_X
    FuelShowRect.y = VAL_Y+60
    Core.screen.blit(HubFuel, FuelShowRect)

    HubSupple = Core.font2.render("Supple: "+str(Core.DICT_SUPPLE[id]), True, "White")
    SuppleShowRect = HubSupple.get_rect()
    SuppleShowRect.x = VAL_X
    SuppleShowRect.y = VAL_Y+90
    Core.screen.blit(HubSupple, SuppleShowRect)

def SHOW_SEND():
        DROPDOWN_HUBSELECT.show()

def SHOW_CONS():
    BUTTON_ADDHUB.show()


    Text = Core.font2.render("Cost: " + str(Core.VAL_COST_HUB), True, "White")
    ShowRect = Text.get_rect()
    ShowRect.x = VAL_X
    ShowRect.y = VAL_Y
    Core.screen.blit(Text, ShowRect)

def SHOW_MAGAZINE():

    Ammo = Core.font2.render("Ammo: "+str(Core.VAL_AMMO), True, "White")
    AmmoShowRect = Ammo.get_rect()
    AmmoShowRect.x = VAL_X
    AmmoShowRect.y = VAL_Y
    Core.screen.blit(Ammo, AmmoShowRect)

    Fuel = Core.font2.render("Fuel: "+str(Core.VAL_FUEL), True, "White")
    FuelShowRect = Fuel.get_rect()
    FuelShowRect.x = VAL_X
    FuelShowRect.y = VAL_Y + 30
    Core.screen.blit(Fuel, FuelShowRect)

    Supple = Core.font2.render("Supple: "+str(Core.VAL_SUPPLE), True, "White")
    SuppleShowRect = Supple.get_rect()
    SuppleShowRect.x = VAL_X
    SuppleShowRect.y = VAL_Y + 60
    Core.screen.blit(Supple, SuppleShowRect)

def SHOW_ORDER():
    BUTTON_ORDERCREATE.show()

    Ammo = Core.font2.render("Ammo: ", True, "White")
    AmmoShowRect = Ammo.get_rect()
    AmmoShowRect.x = VAL_X
    AmmoShowRect.y = VAL_Y
    Core.screen.blit(Ammo, AmmoShowRect)

    Fuel = Core.font2.render("Fuel: ", True, "White")
    FuelShowRect = Fuel.get_rect()
    FuelShowRect.x = VAL_X
    FuelShowRect.y = VAL_Y + 30
    Core.screen.blit(Fuel, FuelShowRect)

    Supple = Core.font2.render("Supple: ", True, "White")
    SuppleShowRect = Supple.get_rect()
    SuppleShowRect.x = VAL_X
    SuppleShowRect.y = VAL_Y + 60
    Core.screen.blit(Supple, SuppleShowRect)

def SHOW_CURRENCY():
    global LIST_DROPDOWN_OPTION

    Ammo = Core.font2.render("Currency: " + str(Core.VAL_CURRENCY), True, "White")
    AmmoShowRect = Ammo.get_rect()
    AmmoShowRect.x = 200
    AmmoShowRect.y = 260
    Core.screen.blit(Ammo, AmmoShowRect)

    #jest to do dropdown

def SHOW_WARNING():
    pygame.draw.rect(Core.screen,"black",RECT_STROMWARNING)
    pygame.draw.rect(Core.screen, "Red", RECT_MISSILEWARNING)
    pygame.draw.rect(Core.screen, "orange", RECT_ATTACKWARNING)

IMAGE_LEFTPANEL = pygame.image.load("Texture/Interface/Grafika01.png").convert_alpha()
IMAGE_LEFTPANEL = pygame.transform.scale(IMAGE_LEFTPANEL, (400, 720))
SURFACE_LEFTPANEL = pygame.Surface((400, 720))
SURFACE_LEFTPANEL.blit(IMAGE_LEFTPANEL, (0, 0))
#-----------------------------------------------------------------------------------------------------------------------
IMAGE_STOP = pygame.image.load("Texture/Interface/Pause.png")
IMAGE_SPEED1 = pygame.image.load("Texture/Interface/1x.png")
IMAGE_SPEED2 = pygame.image.load("Texture/Interface/2x.png")
IMAGE_SPEED3 = pygame.image.load("Texture/Interface/3x.png")


IMAGE_STOP = pygame.transform.scale(IMAGE_STOP, (40, 40))
IMAGE_SPEED1 = pygame.transform.scale(IMAGE_SPEED1, (40, 40))
IMAGE_SPEED2 = pygame.transform.scale(IMAGE_SPEED2, (40, 40))
IMAGE_SPEED3 = pygame.transform.scale(IMAGE_SPEED3, (40, 40))

BUTTON_STOP = Button(Core.screen, 60, 70, 40, 40, image=IMAGE_STOP, onClick=lambda: DEF_CHANGETIME(0))
BUTTON_SPEED1 = Button(Core.screen, 100, 70, 40, 40, image=IMAGE_SPEED1, onClick=lambda: DEF_CHANGETIME(1))
BUTTON_SPEED2 = Button(Core.screen, 260, 70, 40, 40, image=IMAGE_SPEED2, onClick=lambda: DEF_CHANGETIME(4.5))
BUTTON_SPEED3 = Button(Core.screen, 300, 70, 40, 40, image=IMAGE_SPEED3, onClick=lambda: DEF_CHANGETIME(7.5))
BUTTON_ADDHUB = Button(Core.screen, 280, 300, 80, 30, text='DodajHub', onClick=lambda: Hub.DEF_ADDHUB())
BUTTON_ORDERCREATE = Button(Core.screen, 150, 390, 70, 20, text="Order")
BUTTON_INFO = Button(Core.screen, 20, 300, 80, 40, text="info", colour="green", onClick= lambda: DEF_PANEL(0))
BUTTON_CONS = Button(Core.screen, 20, 365, 80, 40, text="Cons", colour="green", onClick= lambda: DEF_PANEL(1))
BUTTON_SEND = Button(Core.screen, 20, 430, 80, 40, text="Send", colour="green", onClick= lambda: DEF_PANEL(2))
BUTTON_ORDER = Button(Core.screen, 20, 495, 80, 40, text="Order", colour="green", onClick= lambda: DEF_PANEL(3))
BUTTON_MAGAZINE = Button(Core.screen, 20, 560, 80, 40, text="Magazine", colour="green", onClick= lambda: DEF_PANEL(4))
BUTTON_EXIT = Button(Core.screen, 350, 670, 50, 30, text='Exit', onClick=lambda: Core.DEF_EXIT())
BUTTON_SETTING = Button(Core.screen, 0, 670, 50, 30, text='Setting', onClick=lambda: print("hello"))

BUTTON_ORDERCREATE.hide()
BUTTON_ADDHUB.hide()
#--------------------------------------------------

DROPDOWN_HUBSELECT = Dropdown(Core.screen, 150, 300, 100,20,name="HUB",choices=LIST_DROPDOWN_OPTION,direction="down")
DROPDOWN_HUBSELECT.hide()

#-------------------
RECT_STROMWARNING = pygame.Rect(25,150,100,50)
RECT_MISSILEWARNING = pygame.Rect(150,150,100,50)
RECT_ATTACKWARNING = pygame.Rect(275,150,100,50)