import pygame

pygame.init()
SizeScreenHeight = 720
SizeScreenWidth = 1280
leftpanelwidth = 900
leftpanelHeight = 720
leftpanel = pygame.Rect(401,0,leftpanelwidth,leftpanelHeight)
screen = pygame.display.set_mode((SizeScreenWidth,SizeScreenHeight))
clock = pygame.time.Clock()

BOOL_RUNNING = True
BOOL_EXIT=False
BOOL_SUBMIT = False

DICT_HUB = {}
DICT_LINE = {}
DICT_FUEL = {}
DICT_AMMO = {}
DICT_SUPPLE = {}


font1 = pygame.font.Font('Font/digital-7.ttf',42)
font2 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',30)
font3 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',12)

VAL_AMMO = 200
VAL_FUEL = 300
VAL_SUPPLE = 400
VAL_MAXHUBS = 7
VAL_CENTRALHUBID = "HUB_C"
VAL_SPPEDTIME = 1
VAL_CURRENCY = 900
VAL_COST_HUB = 200
VAL_COST_AMMO = 10
VAL_COST_FUEL = 0.5
VAL_COST_SUPPLE = 5
VAL_FUEL_APC_USAGE = 40
VAL_FUEL_CARS_USAGE = 12
VAL_FUEL_TRUCK_USAGE = 30



def DEF_FUELUSE(APC,CARS,TRUCK):
    Fuel_number = 0
    Fuel_number += APC * VAL_FUEL_APC_USAGE
    Fuel_number += CARS * VAL_FUEL_CARS_USAGE
    Fuel_number += TRUCK * VAL_FUEL_TRUCK_USAGE

    return  Fuel_number

def DEF_Convert(Fuel,number):
    one_fuel = 5000
    match(number):
        case 1:
             return Fuel * one_fuel
        case 2:
            return Fuel / one_fuel
def DEF_EXIT():
    global BOOL_EXIT
    BOOL_EXIT=True



