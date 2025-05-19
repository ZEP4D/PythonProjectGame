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

def DEF_ASTAR(Target):
    import heapq, math

    def neigbors_bulid():
        neighbor = {}
        for conn in Core.DICT_LINE:
            a, b = conn.split("->")
            neighbor.setdefault(a,[]).append(b)
            neighbor.setdefault(b, []).append(a)
        return neighbor

    def HEU(a,b):
        return math.hypot(b[0]-a[0],b[1]-a[1])

    neig = neigbors_bulid()
    open_set = []
    heapq.heappush(open_set,(0,VAL_CENTRALHUBID))
    came_from = {}
    g_score = {node: float('inf') for node in Core.DICT_HUB}
    g_score[VAL_CENTRALHUBID] = 0

    f_score  = {node: float('inf') for node in Core.DICT_HUB}
    f_score[VAL_CENTRALHUBID] = HEU(Core.DICT_HUB[VAL_CENTRALHUBID],Core.DICT_HUB[Target])

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == Target:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in neig.get(current, []):
            tentative_g = g_score[current] + HEU(Core.DICT_HUB[current], Core.DICT_HUB[neighbor])
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + HEU(Core.DICT_HUB[neighbor], Core.DICT_HUB[Target])
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []







