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
font2 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',32)

VAL_AMMO = 200
VAL_FUEL = 300
VAL_SUPPLE = 400
VAL_MAXHUBS = 7
VAL_CENTRALHUBID = "HUB_C"
VAL_SPPEDTIME = 1


def DEF_ORDERSUBMIT():
    global  BOOL_SUBMIT
    BOOL_SUBMIT = True

def DEF_ODERCREATE(Number,Value):
    global VAL_AMMO,VAL_FUEL,VAL_SUPPLE,BOOL_SUBMIT
    match Number:
        case 0:
            if BOOL_SUBMIT:
                VAL_AMMO += Value
                BOOL_SUBMIT = False
        case 1:
            if BOOL_SUBMIT:
                VAL_FUEL += Value
        case 2:
            if BOOL_SUBMIT:
                VAL_SUPPLE += Value

def DEF_EXIT():
    global BOOL_EXIT
    BOOL_EXIT=True



