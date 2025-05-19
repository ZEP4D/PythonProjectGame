import Core
import pygame
import random

BOOL_ADDHUB = False
VAL_MAXHUBS = 7
VAL_HUBSNOW = 0
VAL_STARTDOT = None
VAL_STARTDOTKEY = ""
VAL_ENDDOTKEY = ""
VAL_CENTRALHUBID = "HUB_C"
VAL_ROADHUB = " "

def DEF_HUBNUMBER(x,y):
    global VAL_MAXHUBS,VAL_HUBSNOW,BOOL_ADDHUB
    hubid  = "HBID_"+str(VAL_HUBSNOW)

    if VAL_HUBSNOW < VAL_MAXHUBS:
        new_ret = pygame.Rect(x, y, 30, 30)

        Core.DICT_HUB[hubid] = new_ret
        DEF_INFOPANEL(hubid)
        VAL_HUBSNOW = VAL_HUBSNOW + 1
        BOOL_ADDHUB = False

def DEF_ADDHUB():
    global BOOL_ADDHUB
    BOOL_ADDHUB = True

def DEF_LINE(position,Hubkey):
    global VAL_STARTDOT, VAL_STARTDOTKEY, VAL_ENDDOTKEY, VAL_CENTRALHUBID, VAL_ROADHUB

    if VAL_STARTDOT is None:
        VAL_STARTDOT = position
        VAL_STARTDOTKEY = Hubkey
    else:
        punk_konca = position
        VAL_ENDDOTKEY = Hubkey
        new_line = (VAL_STARTDOT, punk_konca)

        exits  = any(
            (line[0] == new_line[1] and line[1] == new_line[1]) or
            (line[0] == new_line[1] and line[1] == new_line[0])
            for line in Core.DICT_LINE
        )
        if not exits:
            numerE = VAL_ENDDOTKEY.split("_")[1]
            numerS = VAL_STARTDOTKEY.split("_")[1]
            if VAL_ENDDOTKEY == VAL_CENTRALHUBID:
                VAL_ROADHUB = VAL_ENDDOTKEY + "->" + VAL_STARTDOTKEY
            else:
                VAL_ROADHUB = VAL_STARTDOTKEY + "->" + VAL_ENDDOTKEY
            Core.DICT_LINE[VAL_ROADHUB] = new_line

        VAL_STARTDOT = None
        VAL_STARTDOTKEY = ""

def DEF_INFOPANEL(id):
    Fuel = random.randint(1, 10)
    Ammo = random.randint(1, 10)
    Supple = random.randint(1, 10)

    Core.DICT_FUEL[id] = Fuel
    Core.DICT_AMMO[id] = Ammo
    Core.DICT_SUPPLE[id] = Supple

def DEF_HUBCENTRAL():
    x = random.randint(410,1200)
    y = random.randint(550,710)
    new_ret = pygame.Rect(x,y, 30, 30)

    Core.DICT_HUB[VAL_CENTRALHUBID] = new_ret
    DEF_INFOPANEL(VAL_CENTRALHUBID)

def Cihicwc():
    #Check if hub is connect with Central hub

    for i in Core.DICT_LINE:
        idS = i.split("->")[0]
        idE = i.split("->")[1]


