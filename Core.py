import pygame

pygame.init()
SizeScreenHeight = 720
SizeScreenWidth = 1280
leftpanelwidth = 900
leftpanelHeight = 720
leftpanel = pygame.Rect(401,0,leftpanelwidth,leftpanelHeight)
screen = pygame.display.set_mode((SizeScreenWidth,SizeScreenHeight))
clock = pygame.time.Clock()
running = True
GotoExit=False
Submitbool = False
Hublist = {}
LineList = {}
Fuellist = {}
AmmoList = {}
SuppleList  = {}
font1 = pygame.font.Font('Font/digital-7.ttf',42)
font2 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',32)

Ammo = 200
Fuel = 300
Supple = 400



def SubmitOrder():
    global  Submitbool
    Submitbool = True

def CreateOrder(Number,Value):
    global Ammo,Fuel,Supple,Submitbool
    match Number:
        case 0:
            if Submitbool:
                Ammo += Value
                Submitbool = False
        case 1:
            if Submitbool:
                Fuel += Value
        case 2:
            if Submitbool:
                Supple += Value

def SetGoToExit():
    global GotoExit
    GotoExit=True



