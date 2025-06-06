import re
import pygame
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import Core
import Hub



VAL_PASSTIME = 0
VAL_CHANGETIME = 0
VAL_X = 180
VAL_Y = 320
VAL_IDSEND = ""



BOOL_INFO=False
BOOL_INFO_OBJECT = False
BOOL_CONS=False
BOOL_SEND=False
BOOL_ORDER=False
BOOL_MAGAZINE=False
BOOL_WARNING = False


def DEF_CLOCK(dt):
    global VAL_PASSTIME

    VAL_PASSTIME = VAL_PASSTIME + dt * Core.VAL_SPPEDTIME
    if VAL_PASSTIME >= 1:
        Core.VAL_MINUTES = Core.VAL_MINUTES + 1
        VAL_PASSTIME = 0

        if Core.VAL_MINUTES >= 60:
            Core.VAL_HOURS += Core.VAL_MINUTES // 60
            Core.VAL_MINUTES %= 60
        if Core.VAL_HOURS >= 24:
            Core.VAL_HOURS %= 24

def DEF_DISPLAY():
    czas = f"{Core.VAL_HOURS:02}:{Core.VAL_MINUTES:02}"
    showTime = Core.font1.render(czas, True, "white")
    showTimeRect = showTime.get_rect()
    showTimeRect.x = 15
    showTimeRect.y = 25
    Core.screen.blit(showTime, showTimeRect)

def DEF_CHANGETIME(num,t):

    match(num):
        case 0:
            Core.VAL_SPPEDTIME = t
            BUTTON_STOP.setImage(IMAGE_STOP_ON)
            BUTTON_SPEED1.setImage(IMAGE_SPEED1_OFF)
            BUTTON_SPEED2.setImage(IMAGE_SPEED2_OFF)
            BUTTON_SPEED3.setImage(IMAGE_SPEED3_OFF)
        case 1:
            Core.VAL_SPPEDTIME = t
            BUTTON_STOP.setImage(IMAGE_STOP_OFF)
            BUTTON_SPEED1.setImage(IMAGE_SPEED1_ON)
            BUTTON_SPEED2.setImage(IMAGE_SPEED2_OFF)
            BUTTON_SPEED3.setImage(IMAGE_SPEED3_OFF)
        case 2:
            Core.VAL_SPPEDTIME = t
            BUTTON_STOP.setImage(IMAGE_STOP_OFF)
            BUTTON_SPEED1.setImage(IMAGE_SPEED1_OFF)
            BUTTON_SPEED2.setImage(IMAGE_SPEED2_ON)
            BUTTON_SPEED3.setImage(IMAGE_SPEED3_OFF)
        case 3:
            Core.VAL_SPPEDTIME = t
            BUTTON_STOP.setImage(IMAGE_STOP_OFF)
            BUTTON_SPEED1.setImage(IMAGE_SPEED1_OFF)
            BUTTON_SPEED2.setImage(IMAGE_SPEED2_OFF)
            BUTTON_SPEED3.setImage(IMAGE_SPEED3_ON)

def DEF_HIDE():
    BUTTON_ADDHUB.hide()
    BUTTON_ORDERCREATE.hide()
    BUTTON_SENDTRANSPORT.hide()
    TEXTBOX_SUPPLIESEND.hide()
    TEXTBOX_AMMOSEND.hide()
    TEXTBOX_FUELSEND.hide()
    TEXTBOX_AMMORDER.hide()
    TEXTBOX_SUPPLORDER.hide()
    TEXTBOX_FUELORDER.hide()

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

    DEF_CBUTTON()

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

def SHOW_SEND(id):
        global VAL_IDSEND
        BUTTON_SENDTRANSPORT.show()
        TEXTBOX_SUPPLIESEND.show()
        TEXTBOX_AMMOSEND.show()
        TEXTBOX_FUELSEND.show()

        VAL_IDSEND  = id
        if id == Core.VAL_CENTRALHUBID:
            VAL_IDSEND  = "None"

        LineShow = Core.font2.render("ID:" + str(VAL_IDSEND), True, "White")
        LineShowRect = LineShow.get_rect()
        LineShowRect.x = VAL_X
        LineShowRect.y = VAL_Y
        Core.screen.blit(LineShow, LineShowRect)

        Ammo = Core.font2.render("Ammo: ", True, "White")
        AmmoShowRect = Ammo.get_rect()
        AmmoShowRect.x = VAL_X
        AmmoShowRect.y = VAL_Y + 30
        Core.screen.blit(Ammo, AmmoShowRect)

        Fuel = Core.font2.render("Fuel: ", True, "White")
        FuelShowRect = Fuel.get_rect()
        FuelShowRect.x = VAL_X
        FuelShowRect.y = VAL_Y + 60
        Core.screen.blit(Fuel, FuelShowRect)

        Supple = Core.font2.render("Supple: ", True, "White")
        SuppleShowRect = Supple.get_rect()
        SuppleShowRect.x = VAL_X
        SuppleShowRect.y = VAL_Y + 90
        Core.screen.blit(Supple, SuppleShowRect)

def SHOW_CONS():
    BUTTON_ADDHUB.show()


    Text = Core.font2.render("Cost:" + str(Core.VAL_COST_HUB), True, "White")
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
    TEXTBOX_FUELORDER.show()
    TEXTBOX_AMMORDER.show()
    TEXTBOX_SUPPLORDER.show()

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

    Ammo = Core.font2.render(str(Core.VAL_CURRENCY), True, "White")
    AmmoShowRect = Ammo.get_rect()
    AmmoShowRect.x = 350
    AmmoShowRect.y = 230
    Core.screen.blit(Ammo, AmmoShowRect)

    #jest to do dropdown

def SHOW_WARNING():
    Core.screen.blit(IMAGE_WARNING,(320,50))

def DEF_ORDER():

    if TEXTBOX_AMMORDER.getText() != 0 and TEXTBOX_AMMORDER.getText() != "":
        if re.match(r'^\d+$',TEXTBOX_AMMORDER.getText()):
            if Core.VAL_CURRENCY >= (int(TEXTBOX_AMMORDER.getText()) * Core.VAL_COST_AMMO):
                Core.VAL_CURRENCY = Core.VAL_CURRENCY - (int(TEXTBOX_AMMORDER.getText()) * Core.VAL_COST_AMMO)
                Core.VAL_AMMO = Core.VAL_AMMO + int(TEXTBOX_AMMORDER.getText())
            else:
                DEF_WARNING_START()
        else:
            DEF_WARNING_START()
    else:
        DEF_WARNING_START()

    if TEXTBOX_FUELORDER.getText() != 0 and TEXTBOX_FUELORDER.getText() != "":
        if re.match(r'^\d+$', TEXTBOX_FUELORDER.getText()):
            if Core.VAL_CURRENCY >= (int(TEXTBOX_FUELORDER.getText()) * Core.VAL_COST_FUEL):
                Core.VAL_CURRENCY = Core.VAL_CURRENCY - (int(TEXTBOX_FUELORDER.getText()) * Core.VAL_COST_FUEL)
                Core.VAL_FUEL = Core.VAL_FUEL + int(TEXTBOX_FUELORDER.getText())
            else:
                DEF_WARNING_START()
        else:
            DEF_WARNING_START()
    else:
        DEF_WARNING_START()

    if TEXTBOX_SUPPLORDER.getText() != 0 and TEXTBOX_SUPPLORDER.getText() != "":
        if re.match(r'^\d+$', TEXTBOX_SUPPLORDER.getText()):
            if Core.VAL_CURRENCY >= (int(TEXTBOX_SUPPLORDER.getText()) * Core.VAL_COST_SUPPLE):
                Core.VAL_CURRENCY = Core.VAL_CURRENCY - (int(TEXTBOX_SUPPLORDER.getText()) * Core.VAL_COST_SUPPLE)
                Core.VAL_SUPPLE = Core.VAL_SUPPLE + int(TEXTBOX_SUPPLORDER.getText())
            else:
                DEF_WARNING_START()
        else:
            DEF_WARNING_START()
    else:
        DEF_WARNING_START()

    TEXTBOX_AMMORDER.setText("")
    TEXTBOX_FUELORDER.setText("")
    TEXTBOX_SUPPLORDER.setText("")

def DEF_SEND():
    global VAL_IDSEND


    if VAL_IDSEND == "None":
        DEF_WARNING_START()
    else:

        Trasa = Hub.DEF_ASTAR(VAL_IDSEND)

        if TEXTBOX_AMMOSEND.getText() != 0 and TEXTBOX_AMMOSEND.getText() != "":
            if re.match(r'^\d+$', TEXTBOX_AMMOSEND.getText()):
                if VAL_IDSEND != "None":
                    for ID in Trasa:
                        if ID == Core.VAL_CENTRALHUBID:
                            Core.DICT_AMMO[VAL_IDSEND] += int(TEXTBOX_AMMOSEND.getText())
                            Core.VAL_AMMO -= int(TEXTBOX_AMMOSEND.getText())
                        else:
                            DEF_WARNING_START()
                else:
                    DEF_WARNING_START()
            else:
                DEF_WARNING_START()
        else:
            DEF_WARNING_START()

        if TEXTBOX_FUELSEND.getText() != 0 and TEXTBOX_FUELSEND.getText() != "":
            if re.match(r'^\d+$', TEXTBOX_FUELSEND.getText()):
                if VAL_IDSEND != "None":
                    for ID in Trasa:
                        if ID == Core.VAL_CENTRALHUBID:
                            Core.DICT_FUEL[VAL_IDSEND] += int(TEXTBOX_FUELSEND.getText())
                            Core.VAL_FUEL -= int(TEXTBOX_FUELSEND.getText())
                        else:
                            DEF_WARNING_START()
                else:
                    DEF_WARNING_START()
            else:
                DEF_WARNING_START()
        else:
            DEF_WARNING_START()


        if TEXTBOX_SUPPLIESEND.getText() != 0 and TEXTBOX_SUPPLIESEND.getText() != "":
            if re.match(r'^\d+$', TEXTBOX_SUPPLIESEND.getText()):
                if VAL_IDSEND != "None":
                    for ID in Trasa:
                        if ID == Core.VAL_CENTRALHUBID:
                            Core.DICT_SUPPLE[VAL_IDSEND] += int(TEXTBOX_SUPPLIESEND.getText())
                            Core.VAL_SUPPLE -= int(TEXTBOX_SUPPLIESEND.getText())
                        else:
                            DEF_WARNING_START()
                else:
                    DEF_WARNING_START()
            else:
                DEF_WARNING_START()
        else:
            DEF_WARNING_START()

        TEXTBOX_AMMOSEND.setText("")
        TEXTBOX_FUELSEND.setText("")
        TEXTBOX_SUPPLIESEND.setText("")

def DEF_CBUTTON():
    global BOOL_INFO,BOOL_CONS,BOOL_ORDER,BOOL_SEND,BOOL_MAGAZINE

    if BOOL_INFO:
        BUTTON_INFO.setImage(IMAGE_INFO_ON)
        BUTTON_CONS.setImage(IMAGE_CONS)
        BUTTON_SEND.setImage(IMAGE_SEND)
        BUTTON_ORDER.setImage(IMAGE_ORDER)
        BUTTON_MAGAZINE.setImage(IMAGE_MAG)
    elif BOOL_ORDER:
        BUTTON_INFO.setImage(IMAGE_INFO)
        BUTTON_CONS.setImage(IMAGE_CONS)
        BUTTON_SEND.setImage(IMAGE_SEND)
        BUTTON_ORDER.setImage(IMAGE_ORDER_ON)
        BUTTON_MAGAZINE.setImage(IMAGE_MAG)
    elif BOOL_CONS:
        BUTTON_INFO.setImage(IMAGE_INFO)
        BUTTON_CONS.setImage(IMAGE_CONS_ON)
        BUTTON_SEND.setImage(IMAGE_SEND)
        BUTTON_ORDER.setImage(IMAGE_ORDER)
        BUTTON_MAGAZINE.setImage(IMAGE_MAG)
    elif BOOL_SEND:
        BUTTON_INFO.setImage(IMAGE_INFO)
        BUTTON_CONS.setImage(IMAGE_CONS)
        BUTTON_SEND.setImage(IMAGE_SEND_ON)
        BUTTON_ORDER.setImage(IMAGE_ORDER)
        BUTTON_MAGAZINE.setImage(IMAGE_MAG)
    elif BOOL_MAGAZINE:
        BUTTON_INFO.setImage(IMAGE_INFO)
        BUTTON_CONS.setImage(IMAGE_CONS)
        BUTTON_SEND.setImage(IMAGE_SEND)
        BUTTON_ORDER.setImage(IMAGE_ORDER)
        BUTTON_MAGAZINE.setImage(IMAGE_MAG_ON)
def DEF_WARNING_START():
    global BOOL_WARNING
    BOOL_WARNING = True
    Core.DEF_STARTICKET()
def DEF_WARNING_ACTIVE():
    global IMAGE_WARNING, BOOL_WARNING

    if BOOL_WARNING:

        IMAGE_WARNING = pygame.image.load("Texture/Interface/Warning_RED.png")
        IMAGE_WARNING = pygame.transform.scale(IMAGE_WARNING, (80, 40))
        if pygame.time.get_ticks() - Core.Star_Tiecket >= 2000:
            IMAGE_WARNING = pygame.image.load("Texture/Interface/Warning_BLACK.png")
            IMAGE_WARNING = pygame.transform.scale(IMAGE_WARNING, (80, 40))
            BOOL_WARNING = False

IMAGE_LEFTPANEL = pygame.image.load("Texture/Interface/Grafika01.png").convert_alpha()
IMAGE_LEFTPANEL = pygame.transform.scale(IMAGE_LEFTPANEL, (400, 720))
SURFACE_LEFTPANEL = pygame.Surface((400, 720))
SURFACE_LEFTPANEL.blit(IMAGE_LEFTPANEL, (0, 0))
#-----------------------------------------------------------------------------------------------------------------------
IMAGE_STOP_OFF = pygame.image.load("Texture/Interface/BUTTONS/PAUSE_OFF.png")
IMAGE_SPEED1_OFF = pygame.image.load("Texture/Interface/BUTTONS/1SPEED_OFF.png")
IMAGE_SPEED2_OFF = pygame.image.load("Texture/Interface/BUTTONS/2SPEED_OFF.png")
IMAGE_SPEED3_OFF = pygame.image.load("Texture/Interface/BUTTONS/3SPEED_OFF.png")

IMAGE_STOP_ON = pygame.image.load("Texture/Interface/BUTTONS/PAUSE_ON.png")
IMAGE_SPEED1_ON = pygame.image.load("Texture/Interface/BUTTONS/1SPEED_ON.png")
IMAGE_SPEED2_ON = pygame.image.load("Texture/Interface/BUTTONS/2SPEED_ON.png")
IMAGE_SPEED3_ON = pygame.image.load("Texture/Interface/BUTTONS/3SPEED_ON.png")

IMAGE_INFO = pygame.image.load("Texture/Interface/BUTTONS/INFO_OFF.png")
IMAGE_CONS = pygame.image.load("Texture/Interface/BUTTONS/CONS_OFF.png")
IMAGE_SEND = pygame.image.load("Texture/Interface/BUTTONS/SEND_OFF.png")
IMAGE_ORDER = pygame.image.load("Texture/Interface/BUTTONS/ODER_OFF.png")
IMAGE_MAG = pygame.image.load("Texture/Interface/BUTTONS/MAGAZINE_OFF.png")
IMAGE_EXIT = pygame.image.load("Texture/Interface/BUTTONS/EXIT.png")

IMAGE_INFO_ON = pygame.image.load("Texture/Interface/BUTTONS/INFO_ON.png")
IMAGE_CONS_ON = pygame.image.load("Texture/Interface/BUTTONS/CONS_ON.png")
IMAGE_SEND_ON = pygame.image.load("Texture/Interface/BUTTONS/SEND_ON.png")
IMAGE_ORDER_ON = pygame.image.load("Texture/Interface/BUTTONS/ODER_ON.png")
IMAGE_MAG_ON = pygame.image.load("Texture/Interface/BUTTONS/MAGAZINE_ON.png")

IMAGE_WARNING = pygame.image.load("Texture/Interface/Warning_BLACK.png")
IMAGE_S_SEND = pygame.image.load("Texture/Interface/BUTTONS/SEND.png")
IMAGE_S_ORDER = pygame.image.load("Texture/Interface/BUTTONS/ORDER.png")
IMAGE_S_HUB = pygame.image.load("Texture/Interface/BUTTONS/HUB.png")


IMAGE_INFO = pygame.transform.scale(IMAGE_INFO, (80, 40))
IMAGE_CONS = pygame.transform.scale(IMAGE_CONS, (80, 40))
IMAGE_SEND = pygame.transform.scale(IMAGE_SEND, (80, 40))
IMAGE_ORDER = pygame.transform.scale(IMAGE_ORDER, (80, 40))
IMAGE_MAG = pygame.transform.scale(IMAGE_MAG, (80, 40))
IMAGE_EXIT = pygame.transform.scale(IMAGE_EXIT, (80, 40))
IMAGE_INFO_ON = pygame.transform.scale(IMAGE_INFO_ON, (80, 40))
IMAGE_CONS_ON = pygame.transform.scale(IMAGE_CONS_ON, (80, 40))
IMAGE_SEND_ON = pygame.transform.scale(IMAGE_SEND_ON, (80, 40))
IMAGE_ORDER_ON = pygame.transform.scale(IMAGE_ORDER_ON, (80, 40))
IMAGE_MAG_ON = pygame.transform.scale(IMAGE_MAG_ON, (80, 40))
IMAGE_WARNING = pygame.transform.scale(IMAGE_WARNING, (80, 40))


BUTTON_STOP = Button(Core.screen, 180, 0, 40, 40, image=IMAGE_STOP_OFF, onClick=lambda: DEF_CHANGETIME(0,0))
BUTTON_SPEED1 = Button(Core.screen, 180, 40, 40, 40, image=IMAGE_SPEED1_ON, onClick=lambda: DEF_CHANGETIME(1,1))
BUTTON_SPEED2 = Button(Core.screen, 220, 0, 40, 40, image=IMAGE_SPEED2_OFF, onClick=lambda: DEF_CHANGETIME(2,4.5))
BUTTON_SPEED3 = Button(Core.screen, 220, 40, 40, 40, image=IMAGE_SPEED3_OFF, onClick=lambda: DEF_CHANGETIME(3,7.5))
BUTTON_ADDHUB = Button(Core.screen, 280, 320, 80, 30,image=IMAGE_S_HUB, onClick=lambda: Hub.DEF_ADDHUB())
BUTTON_ORDERCREATE = Button(Core.screen, 190, 450, 70, 20, image=IMAGE_S_ORDER, onClick=lambda: DEF_ORDER())
BUTTON_SENDTRANSPORT = Button(Core.screen,190,450,50,30, image=IMAGE_S_SEND, onClick=lambda: DEF_SEND())
BUTTON_INFO = Button(Core.screen, 5, 270, 80, 40, image=IMAGE_INFO, onClick= lambda: DEF_PANEL(0),)
BUTTON_CONS = Button(Core.screen, 5, 310, 80, 40, image=IMAGE_CONS, onClick= lambda: DEF_PANEL(1))
BUTTON_SEND = Button(Core.screen, 5, 350, 80, 40, image=IMAGE_SEND, onClick= lambda: DEF_PANEL(2))
BUTTON_ORDER = Button(Core.screen, 5, 390, 80, 40, image=IMAGE_ORDER, onClick= lambda: DEF_PANEL(3))
BUTTON_MAGAZINE = Button(Core.screen, 5, 430, 80, 40, image=IMAGE_MAG, onClick= lambda: DEF_PANEL(4))
BUTTON_EXIT = Button(Core.screen, 5, 470, 80, 40, image=IMAGE_EXIT, onClick=lambda: Core.DEF_EXIT())
#BUTTON_SETTING = Button(Core.screen, 0, 670, 50, 30, text='Setting', onClick=lambda: print("hello"))

BUTTON_ORDERCREATE.hide()
BUTTON_ADDHUB.hide()
BUTTON_SENDTRANSPORT.hide()
#-------------------
TEXTBOX_AMMOSEND = TextBox(Core.screen,300,350,70,35, fontsize=10,borderThickness=1,colour="#078AE8")
TEXTBOX_FUELSEND = TextBox(Core.screen,300,380,70,35, fontsize=10,borderThickness=1,colour="#078AE8")
TEXTBOX_SUPPLIESEND = TextBox(Core.screen,300,410,70,35, fontsize=10,borderThickness=1,colour="#078AE8")

TEXTBOX_AMMORDER = TextBox(Core.screen,300,320,70,35, fontsize=10,borderThickness=1,colour="#078AE8")
TEXTBOX_FUELORDER = TextBox(Core.screen,300,350,70,35, fontsize=10,borderThickness=1,colour="#078AE8")
TEXTBOX_SUPPLORDER = TextBox(Core.screen,300,380,70,35, fontsize=10,borderThickness=1,colour="#078AE8")


TEXTBOX_AMMORDER.hide()
TEXTBOX_SUPPLORDER.hide()
TEXTBOX_FUELORDER.hide()
TEXTBOX_SUPPLIESEND.hide()
TEXTBOX_AMMOSEND.hide()
TEXTBOX_FUELSEND.hide()
#-------------------
RECT_STROMWARNING = pygame.Rect(25,150,100,50)
RECT_MISSILEWARNING = pygame.Rect(150,150,100,50)
RECT_ATTACKWARNING = pygame.Rect(275,150,100,50)