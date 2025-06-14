import Core
import pygame
import random

BOOL_ADDHUB = False
BOOL_SELECTED = False
VAL_STARTDOT = None
VAL_HUBSNOW = 0
VAL_STARTDOTKEY = ""
VAL_ENDDOTKEY = ""
VAL_ROADHUB = ""
VAL_SELECTED_ID = ''


VAL_TEXUTRE_ON = pygame.image.load("../Texture/MAP/HUB_ON.png").convert_alpha()
VAL_TEXUTRE_OFF = pygame.image.load("../Texture/MAP/HUB_OFF.png").convert_alpha()

IMAGE_HUB_C = VAL_TEXUTRE_OFF
IMAGE_HUB = VAL_TEXUTRE_OFF
IMAGE_HUB = pygame.transform.scale(IMAGE_HUB,(40,40))


def DEF_HUBNUMBER(x,y):
    """
    Metoda odpowiada za dodanie/utworzenie nowego hub na pozycji które zostały podana i program sprawdza czy ilosc Waluty jest wystarczająca i też czy liczba hub nie przekracza
    maksymalnej ilości

    :param x: Pozycja x
    :param y: Pozycja y
    """
    global VAL_HUBSNOW,BOOL_ADDHUB
    hubid  = "HUB_"+str(VAL_HUBSNOW)

    if Core.VAL_CURRENCY >= Core.VAL_COST_HUB:
        if VAL_HUBSNOW < Core.VAL_MAXHUBS:
            new_ret = pygame.Rect(x, y, 40, 40)

            Core.DICT_HUB[hubid] = new_ret
            DEF_INFOPANEL(hubid)
            VAL_HUBSNOW = VAL_HUBSNOW + 1
            BOOL_ADDHUB = False

        Core.VAL_CURRENCY = Core.VAL_CURRENCY - Core.VAL_COST_HUB
    else:
        return

def DEF_ADDHUB():
    """
    Metoda do zmiany flagi z BOOL_ADDHUB na True

    """
    global BOOL_ADDHUB
    BOOL_ADDHUB = True

def DEF_LINE(position,hubkey):
    """
    Metoda odpowiada za utworzenie połączenia dwóch hub wybranych przez gracza

    :param position: koordynaty wybranej pozycji
    :param hubkey: id hub

    """
    global VAL_STARTDOT, VAL_STARTDOTKEY, VAL_ENDDOTKEY, VAL_ROADHUB

    if VAL_STARTDOT is None:
        VAL_STARTDOT = position
        VAL_STARTDOTKEY = hubkey
    else:
        punk_konca = position
        VAL_ENDDOTKEY = hubkey
        new_line = (VAL_STARTDOT, punk_konca)

        exits  = any(
            (line[0] == new_line[1] and line[1] == new_line[1]) or
            (line[0] == new_line[1] and line[1] == new_line[0])
            for line in Core.DICT_LINE
        )
        if not exits:
            if VAL_ENDDOTKEY == Core.VAL_CENTRALHUBID:
                VAL_ROADHUB = VAL_ENDDOTKEY + "->" + VAL_STARTDOTKEY
            else:
                VAL_ROADHUB = VAL_STARTDOTKEY + "->" + VAL_ENDDOTKEY

            Core.DICT_LINE[VAL_ROADHUB] = new_line

        VAL_STARTDOT = None
        VAL_STARTDOTKEY = ""

def DEF_INFOPANEL(id):
    """
    Metoda która dla każdego nowego hub przypisuje wartości

    :param id: id hub
    """
    Fuel = 0
    Ammo = 0
    Supple = 0


    if id == Core.VAL_CENTRALHUBID:
        Core.DICT_FUEL[id] = Core.VAL_FUEL
        Core.DICT_AMMO[id] = Core.VAL_AMMO
        Core.DICT_SUPPLE[id] = Core.VAL_SUPPLE
    else:
        Core.DICT_FUEL[id] = Fuel
        Core.DICT_AMMO[id] = Ammo
        Core.DICT_SUPPLE[id] = Supple

def DEF_HUBCENTRAL():
    """
    Metoda odpowiada za utworzenie hub centralnego

    """
    x = random.randint(410,1200)
    y = random.randint(600,690)
    new_ret = pygame.Rect(x,y, 50, 50)
    Core.DICT_HUB[Core.VAL_CENTRALHUBID] = new_ret
    DEF_INFOPANEL(Core.VAL_CENTRALHUBID)

def DEF_ASTAR(target):
    """
    Algorytm A*

    :param target: Cel w który algorytm ma znaleść trasę
    :return:
    """
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
    heapq.heappush(open_set, (0, Core.VAL_CENTRALHUBID))
    came_from = {}
    g_score = {node: float('inf') for node in Core.DICT_HUB}
    g_score[Core.VAL_CENTRALHUBID] = 0

    f_score  = {node: float('inf') for node in Core.DICT_HUB}
    f_score[Core.VAL_CENTRALHUBID] = HEU(Core.DICT_HUB[Core.VAL_CENTRALHUBID], Core.DICT_HUB[target])

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == target:
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
                f_score[neighbor] = tentative_g + HEU(Core.DICT_HUB[neighbor], Core.DICT_HUB[target])
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def DEF_SHOW(id):
    """
    Metoda do wyświetlenie na mapie hub i modyfikacja wyglądu kiedy jest wybrany

    :param id: ID Hub
    """
    global BOOL_SELECTED, VAL_SELECTED_ID, IMAGE_HUB,IMAGE_HUB_C



    if id == Core.VAL_CENTRALHUBID and  id == VAL_SELECTED_ID and BOOL_SELECTED:
        IMAGE_HUB_C = VAL_TEXUTRE_ON
        image = IMAGE_HUB_C
    elif id == Core.VAL_CENTRALHUBID:
        IMAGE_HUB_C = VAL_TEXUTRE_OFF
        image = IMAGE_HUB_C
    elif id == VAL_SELECTED_ID and BOOL_SELECTED:
        IMAGE_HUB = VAL_TEXUTRE_ON
        image = IMAGE_HUB
    else:
        IMAGE_HUB = VAL_TEXUTRE_OFF
        image = IMAGE_HUB

    Core.screen.blit(image, Core.DICT_HUB[id])
def DEF_SELECTED(id):
    """
    Metoda do przypisanie do zmiennej VAL_SELECTED_ID id hub i zmianna flagi BOOL_SELECTED na True
    :param id: ID Hub
    """
    global IMAGE_HUB, BOOL_SELECTED, VAL_SELECTED_ID

    BOOL_SELECTED = True
    VAL_SELECTED_ID = id






