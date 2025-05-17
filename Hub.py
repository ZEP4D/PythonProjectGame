import Core
import pygame
import random

Dodawaaniehubbool = False
MaxNumbers_hubs = 7
Inthemoment = 0
punk_start = None
Punkt_Start_klucz = ""
Punkt_End_klucz = ""

def NumbersHubs(x,y):
    global MaxNumbers_hubs,Inthemoment,Dodawaaniehubbool
    hubid  = "HBID"+str(Inthemoment)

    if Inthemoment < MaxNumbers_hubs:
        new_ret = pygame.Rect(x, y, 20, 20)

        Core.Hublist[hubid] = new_ret
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
            for line in Core.LineList
        )
        if not exits:
            TrasaHub = Punkt_Start_klucz + "->" + Punkt_End_klucz
            Core.LineList[TrasaHub] = new_line

        punk_start = None
        Punkt_Start_klucz = ""

def Infopanel(id):
    Fuel = random.randint(1, 10)
    Ammo = random.randint(1, 10)
    Supple = random.randint(1, 10)

    Core.Fuellist[id] = Fuel
    Core.AmmoList[id] = Ammo
    Core.SuppleList[id] = Supple