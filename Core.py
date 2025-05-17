import pygame


pygame.init()
SizeScreenHeight = 720
SizeScreenWidth = 1280
screen = pygame.display.set_mode((SizeScreenWidth,SizeScreenHeight))
clock = pygame.time.Clock()
running = True
GotoExit=False
Hublist = {}
LineList = {}
Fuellist = {}
AmmoList = {}
SuppleList  = {}
font1 = pygame.font.Font('Font/digital-7.ttf',42)
font2 = pygame.font.Font('Font/vt323-latin-400-normal.ttf',32)



def SetGoToExit():
    global GotoExit
    GotoExit=True