import Core
import pygame
import random

Dodawaaniehubbool = False
MaxNumbers_hubs = 7
Inthemoment = 0
punk_start = None
Punkt_Start_klucz = ""
Punkt_End_klucz = ""
HubCenralID = "HUB_C"
TrasaHub = " "

def NumbersHubs(x,y):
    global MaxNumbers_hubs,Inthemoment,Dodawaaniehubbool
    hubid  = "HBID_"+str(Inthemoment)

    if Inthemoment < MaxNumbers_hubs:
        new_ret = pygame.Rect(x, y, 30, 30)

        Core.Hublist[hubid] = new_ret
        Infopanel(hubid)
        Inthemoment = Inthemoment +1
        Dodawaaniehubbool = False

def DodawanieHub():
    global Dodawaaniehubbool
    Dodawaaniehubbool = True

def Line(position,Hubkey):
    global punk_start, Punkt_Start_klucz, Punkt_End_klucz, HubCenralID, TrasaHub

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
            numerE = Punkt_End_klucz.split("_")[1]
            numerS = Punkt_Start_klucz.split("_")[1]
            if Punkt_End_klucz == HubCenralID:
                TrasaHub = Punkt_End_klucz + " -> " + Punkt_Start_klucz
            else:
                TrasaHub = Punkt_Start_klucz + " -> " + Punkt_End_klucz
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

def HubCentral():
    x = random.randint(410,1200)
    y = random.randint(550,710)
    new_ret = pygame.Rect(x,y, 30, 30)

    Core.Hublist[HubCenralID] = new_ret
    Infopanel(HubCenralID)

def Cihicwc():
    #Check if hub is connect with Central hub
    print("5")