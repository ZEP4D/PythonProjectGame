import json
import os.path
import random

import pygame

pygame.init()
SizeScreenHeight = 720
SizeScreenWidth = 1280
leftpanelwidth = 900
leftpanelHeight = 720
leftpanel = pygame.Rect(401,0,leftpanelwidth,leftpanelHeight)
screen = pygame.display.set_mode((SizeScreenWidth,SizeScreenHeight))
clock = pygame.time.Clock()
Star_Tiecket = pygame.time.get_ticks()

BOOL_RUNNING = True
BOOL_EXIT=False
BOOL_SUBMIT = False
BOOL_GoodW = True
BOOL_Rain = False
BOOL_Thunder = False
BOOL_fog = False

DICT_HUB = {}
DICT_LINE = {}
DICT_FUEL = {}
DICT_AMMO = {}
DICT_SUPPLE = {}


font1 = pygame.font.Font('Font/digital-7.ttf',35)
font2 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',30)
font3 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',12)
font4 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',50)

IMAGE_MAP = pygame.image.load("Texture/MAP/MAPA.png")
IMAGE_GOODW = pygame.image.load("Texture/Interface/GOODW.png")
IMAGE_FOG = pygame.image.load("Texture/Interface/FOG.png")
IMAGE_RAIN = pygame.image.load("Texture/Interface/RAIN.png")
IMAGE_TUNDER = pygame.image.load("Texture/Interface/TUNDER.png")\

IMAGE_GOODW = pygame.transform.scale(IMAGE_GOODW,(80, 40))
IMAGE_FOG = pygame.transform.scale(IMAGE_FOG,(80, 40))
IMAGE_RAIN = pygame.transform.scale(IMAGE_RAIN,(80, 40))
IMAGE_TUNDER = pygame.transform.scale(IMAGE_TUNDER,(80, 40))


VAL_CONFIG = ""

if not os.path.exists("config.json"):
    pygame.quit()
else:
    with open("config.json", "r", encoding="utf-8") as f:
        VAL_CONFIG = json.load(f)


VAL_AMMO = VAL_CONFIG["VAL_AMMO"]
VAL_FUEL = VAL_CONFIG["VAL_FUEL"]
VAL_SUPPLE = VAL_CONFIG["VAL_SUPPLE"]
VAL_MAXHUBS = VAL_CONFIG["VAL_MAXHUBS"]
VAL_CENTRALHUBID = VAL_CONFIG["VAL_CENTRALHUBID"]
VAL_SPPEDTIME = VAL_CONFIG["VAL_SPPEDTIME"]
VAL_HOURS = VAL_CONFIG["VAL_HOURS"]
VAL_MINUTES = VAL_CONFIG["VAL_MINUTES"]
VAL_CURRENCY = VAL_CONFIG["VAL_CURRENCY"]
VAL_COST_HUB = VAL_CONFIG["VAL_COST_HUB"]
VAL_COST_AMMO = VAL_CONFIG["VAL_COST_AMMO"]
VAL_COST_FUEL = VAL_CONFIG["VAL_COST_FUEL"]
VAL_COST_SUPPLE = VAL_CONFIG["VAL_COST_SUPPLE"]
VAL_FUEL_APC_USAGE = VAL_CONFIG["VAL_FUEL_APC_USAGE"]
VAL_FUEL_CARS_USAGE = VAL_CONFIG["VAL_FUEL_CARS_USAGE"]
VAL_FUEL_TRUCK_USAGE = VAL_CONFIG["VAL_FUEL_TRUCK_USAGE"]
VAL_CONVERT_FUEL = VAL_CONFIG["VAL_CONVERT_FUEL"]
VAL_CONVERT_AMMO = VAL_CONFIG["VAL_CONVERT_AMMO"]
VAL_CONVERT_SUPPLE = VAL_CONFIG["VAL_CONVERT_SUPPLE"]
VAL_TRUCK_CAPACITY = VAL_CONFIG["VAL_TRUCK_CAPACITY"]
VAL_FUELTRUCK_CAPACITY = VAL_CONFIG["VAL_FUELTRUCK_CAPACITY"]
VAL_TICKET_PLAYER = VAL_CONFIG["VAL_TICKET_PLAYER"]
VAL_TICKET_ENEMY = VAL_CONFIG["VAL_TICKET_ENEMY"]
VAL_POINT_MANPOWER = VAL_CONFIG["VAL_POINT_MANPOWER"]
VAL_POINT_APC = VAL_CONFIG["VAL_POINT_APC"]
VAL_POINT_Cars = VAL_CONFIG["VAL_POINT_Cars"]
VAL_BASIC_TEMP = VAL_CONFIG["VAL_BASIC_TEMP"]
VAL_LASTHOUERCORE = None



def DEF_FUELUSE(APC,CARS,TRUCK, TRUCK_FUEL):
    Fuel_number = 0
    Fuel_number += APC * VAL_FUEL_APC_USAGE
    Fuel_number += CARS * VAL_FUEL_CARS_USAGE
    Fuel_number += TRUCK * VAL_FUEL_TRUCK_USAGE
    Fuel_number += TRUCK_FUEL * VAL_FUEL_TRUCK_USAGE

    return  Fuel_number




def DEF_POINTSCALCULATOR(APC,CARS,MENPOWER):
    Points = 0
    Points += APC * VAL_POINT_APC
    Points += CARS * VAL_POINT_Cars
    Points += MENPOWER * VAL_POINT_MANPOWER

    return Points

def DEF_Convert(Number,INFO1,INFO2):
    match(INFO1):
        case 1:
            match(INFO2):
                case "FUEL":
                    return Number * VAL_CONVERT_FUEL
                case "AMMO":
                    return Number * VAL_CONVERT_AMMO
                case "SUPPLE":
                    return Number * VAL_CONVERT_SUPPLE

        case 2:
            match (INFO2):
                case "FUEL":
                    return Number / VAL_CONVERT_FUEL
                case "AMMO":
                    return Number / VAL_CONVERT_AMMO
                case "SUPPLE":
                    return Number / VAL_CONVERT_SUPPLE

def DEF_HUBREMOVE(id_hub):
    if id_hub == VAL_CENTRALHUBID:
        return
    if id_hub in DICT_HUB:
        DICT_HUB.pop(id_hub)
        DICT_FUEL.pop(id_hub)
        DICT_AMMO.pop(id_hub)
        DICT_SUPPLE.pop(id_hub)

        conntopop = []
        for conn in DICT_LINE:
            a, b = conn.split("->")
            if a == id_hub or b == id_hub:
                print(conntopop)
                conntopop.append(conn)

        for i in conntopop:
            DICT_LINE.pop(i)

def SHOW_TICKET():

    TicketPLAYER = font2.render(str(VAL_TICKET_PLAYER), True, "White")
    TicketPLAYERShowRect = TicketPLAYER.get_rect()
    TicketPLAYERShowRect.x = 10
    TicketPLAYERShowRect.y = 100
    screen.blit(TicketPLAYER, TicketPLAYERShowRect)

    TicketEnemy = font2.render(str(VAL_TICKET_ENEMY), True, "White")
    TicketEnemyRShowRect = TicketEnemy.get_rect()
    TicketEnemyRShowRect.x = 80
    TicketEnemyRShowRect.y = 100
    screen.blit(TicketEnemy, TicketEnemyRShowRect)

def SHOW_POGODA():
    if BOOL_GoodW:
        screen.blit(IMAGE_GOODW,(320,10))
    elif BOOL_fog:
        screen.blit(IMAGE_FOG, (320, 10))
    elif BOOL_Rain:
        screen.blit(IMAGE_RAIN, (320, 10))
    elif BOOL_Thunder:
        screen.blit(IMAGE_TUNDER, (320, 10))

def DEF_EXIT():
    global BOOL_EXIT
    BOOL_EXIT=True

def DEF_ENDGAME(ticket):
    global BOOL_EXIT, Star_Tiecket

    if VAL_TICKET_ENEMY < 0 and  VAL_TICKET_PLAYER < 0:
        VICTORY = font4.render("DRAW", True, "Black")
        VICTORYShowRect = VICTORY.get_rect()
        VICTORYShowRect.x = 640
        VICTORYShowRect.y = 350
        screen.blit(VICTORY, VICTORYShowRect)

        if ticket - Star_Tiecket >= 10000:
            BOOL_EXIT = True

    elif VAL_TICKET_ENEMY < 0:
        VICTORY = font4.render("VICTORY", True, "Black")
        VICTORYShowRect = VICTORY.get_rect()
        VICTORYShowRect.x = 640
        VICTORYShowRect.y = 350
        screen.blit(VICTORY, VICTORYShowRect)

        if ticket - Star_Tiecket >= 10000:
            BOOL_EXIT = True

    elif VAL_TICKET_PLAYER < 0:
        VICTORY = font4.render("LOSE", True, "Black")
        VICTORYShowRect = VICTORY.get_rect()
        VICTORYShowRect.x = 640
        VICTORYShowRect.y = 350
        screen.blit(VICTORY, VICTORYShowRect)

        if ticket - Star_Tiecket >= 10000:
            BOOL_EXIT = True

def DEF_Weather():
    global VAL_LASTHOUERCORE, VAL_MINUTES, VAL_HOURS, BOOL_GoodW,BOOL_Rain,BOOL_fog,BOOL_Thunder

    if VAL_HOURS == 8 and VAL_MINUTES == 0:
        if VAL_LASTHOUERCORE != VAL_HOURS:
            pogoda = random.randint(0,3)

            match(pogoda):
                case 0:
                    BOOL_GoodW = True
                    BOOL_Thunder = False
                    BOOL_Rain = False
                    BOOL_fog = False
                case 1:
                    BOOL_Rain = True
                    BOOL_GoodW = False
                    BOOL_Thunder = False
                    BOOL_fog = False
                case 2:
                    BOOL_fog = True
                    BOOL_GoodW = False
                    BOOL_Thunder = False
                    BOOL_Rain = False
                case 3:
                    BOOL_Thunder = True
                    BOOL_GoodW = False
                    BOOL_Rain = False
                    BOOL_fog = False
            VAL_LASTHOUERCORE = VAL_HOURS

def DEF_STARTICKET():
    global Star_Tiecket
    Star_Tiecket = pygame.time.get_ticks()