import pygame
from pygame_widgets.textbox import TextBox

import Core
import Hub
from pygame_widgets.button import Button


VAL_MINUTES = 0
VAL_HOURS = 7
VAL_PASSTIME = 0
VAL_CHANGETIME = 0
BOOL_INFO=False
BOOL_INFO_OBJECT = False
BOOL_CONS=False
BOOL_SEND=False
BOOL_ORDER=False
BOOL_MAGAZINE=False


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

def DEF_PANEL(buttonnuber):
    global BOOL_INFO,BOOL_CONS,BOOL_SEND,BOOL_ORDER,BOOL_MAGAZINE

    match buttonnuber:
        case 0:
            BUTTON_ADDHUB.hide()
            BUTTON_ORDERCREATE.hide()
            TEXTBOX_ADDAMMO.hide()
            BOOL_INFO = True
            BOOL_CONS = False
            BOOL_SEND = False
            BOOL_ORDER = False
            BOOL_MAGAZINE = False
        case 1:
            BUTTON_ADDHUB.show()
            BUTTON_ORDERCREATE.hide()
            TEXTBOX_ADDAMMO.hide()
            BOOL_INFO = False
            BOOL_CONS = True
            BOOL_SEND = False
            BOOL_ORDER = False
            BOOL_MAGAZINE = False
        case 2:
            BUTTON_ADDHUB.hide()
            BUTTON_ORDERCREATE.hide()
            TEXTBOX_ADDAMMO.hide()
            BOOL_INFO = False
            BOOL_CONS = False
            BOOL_SEND = True
            BOOL_ORDER = False
            BOOL_MAGAZINE = False
        case 3:
            BUTTON_ADDHUB.hide()
            TEXTBOX_ADDAMMO.hide()
            BOOL_INFO = False
            BOOL_CONS = False
            BOOL_SEND = False
            BOOL_ORDER = True
            BOOL_MAGAZINE = False
        case 4:
            BUTTON_ADDHUB.hide()
            BUTTON_ORDERCREATE.hide()
            TEXTBOX_ADDAMMO.hide()
            BOOL_INFO = False
            BOOL_CONS = False
            BOOL_SEND = False
            BOOL_ORDER = False
            BOOL_MAGAZINE = True

def SHOW_INFO(id):
    x = 150
    y = 300

    LineShow = Core.font2.render(str(id), True, "White")
    LineShowRect = LineShow.get_rect()
    LineShowRect.x = x
    LineShowRect.y = y
    Core.screen.blit(LineShow, LineShowRect)



    HubAmmo = Core.font2.render(str(Core.DICT_AMMO[id]), True, "White")
    AmmoShowRect = HubAmmo.get_rect()
    AmmoShowRect.x = x
    AmmoShowRect.y = y+50
    Core.screen.blit(HubAmmo, AmmoShowRect)

    HubFuel = Core.font2.render(str(Core.DICT_FUEL[id]), True, "White")
    FuelShowRect = HubFuel.get_rect()
    FuelShowRect.x = x
    FuelShowRect.y = y+100
    Core.screen.blit(HubFuel, FuelShowRect)

    HubSupple = Core.font2.render(str(Core.DICT_SUPPLE[id]), True, "White")
    SuppleShowRect = HubSupple.get_rect()
    SuppleShowRect.x = x
    SuppleShowRect.y = y+150
    Core.screen.blit(HubSupple, SuppleShowRect)

    if  Core.DICT_LINE:
        Lineid = ""

        Keys = Core.DICT_LINE.keys()
        for i in Keys:
            if i.find(id) != -1:
                Lineid = i

        LineShow = Core.font2.render(str(Lineid), True, "White")
        LineShowRect = LineShow.get_rect()
        LineShowRect.x = x
        LineShowRect.y = y+200
        Core.screen.blit(LineShow, LineShowRect)

def SHOW_MAGAZINE():
    x = 150
    y = 300

    Ammo = Core.font2.render(str(Core.VAL_AMMO), True, "White")
    AmmoShowRect = Ammo.get_rect()
    AmmoShowRect.x = x
    AmmoShowRect.y = y + 50
    Core.screen.blit(Ammo, AmmoShowRect)

    Fuel = Core.font2.render(str(Core.VAL_FUEL), True, "White")
    FuelShowRect = Fuel.get_rect()
    FuelShowRect.x = x
    FuelShowRect.y = y + 100
    Core.screen.blit(Fuel, FuelShowRect)

    Supple = Core.font2.render(str(Core.VAL_SUPPLE), True, "White")
    SuppleShowRect = Supple.get_rect()
    SuppleShowRect.x = x
    SuppleShowRect.y = y + 150
    Core.screen.blit(Supple, SuppleShowRect)

def SHOW_ORDER():
    BUTTON_ORDERCREATE.show()
    TEXTBOX_ADDAMMO.show()

def DEF_ORDER():
    if TEXTBOX_ADDAMMO.getText():
        Core.DEF_ODERCREATE(0, int(TEXTBOX_ADDAMMO.getText()))
        if Core.BOOL_SUBMIT:
            TEXTBOX_ADDAMMO.setText(" ")

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
BUTTON_ADDHUB = Button(Core.screen, 300, 400, 70, 20, text='DodajHub', onClick=lambda: Hub.DEF_ADDHUB())
BUTTON_ORDERCREATE = Button(Core.screen, 150, 450, 100, 50, text="Order", onClick=lambda: Core.DEF_ORDERSUBMIT())
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
TEXTBOX_ADDAMMO = TextBox(Core.screen, 150, 400, 100, 50, fontSize=20, onSubmit=DEF_ORDER)
TEXTBOX_ADDAMMO.hide()


#--------------------------------------------------

