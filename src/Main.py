import pygame
import pygame_widgets
import UIGRY
import Core
import Hub
import Objectinthemap
import SimulationCore
from pygame_widgets.button import Button

IMAGE_MAIN = pygame.image.load("../Texture/MainMenu.png").convert_alpha()
IMAGE_LOGO = pygame.image.load("../Texture/logo.png").convert_alpha()
IMAGE_START = pygame.image.load("../Texture/START.png").convert_alpha()
IMAGE_EXIT = pygame.image.load("../Texture/EXIT.png").convert_alpha()
pygame.display.set_caption("SHRIMP CONQUEST")


BUTTON_STAR_GAME = Button(Core.screen, 950, 300, 200, 80, colour=(255, 0, 0, 0), image=IMAGE_START, onClick=lambda: CHANGE_FLAG())
BUTTON_EXIT_GAME = Button(Core.screen, 950, 470, 200, 80, image=IMAGE_EXIT, onClick=lambda: Core.DEF_EXIT())

BOOL_GAMESCENE = False

def CHANGE_FLAG():
    """
        Moduł służy do zmiany flagi w przyciskach w menu Startowym BOOL_GAMESCENE = TRUE
    """
    global BOOL_GAMESCENE
    BOOL_GAMESCENE = True

SimulationCore.DEF_PREWHILE()
Front = Objectinthemap.FrontLine()
Hub.DEF_HUBCENTRAL()
VAL_WHATID = Core.VAL_CENTRALHUBID
VAL_WHATIDOBJECT = ""


def GAME_SCENE():
    """
    Moduł jest odpowiedziany za wyświetlenie i obsługę eventów i logiki w grze
    """

    global VAL_WHATID,VAL_WHATIDOBJECT
    UIGRY.BUTTON_INFO.show()
    UIGRY.BUTTON_ORDER.show()
    UIGRY.BUTTON_SEND.show()
    UIGRY.BUTTON_MAGAZINE.show()
    UIGRY.BUTTON_EXIT.show()
    UIGRY.BUTTON_STOP.show()
    UIGRY.BUTTON_CONS.show()
    UIGRY.BUTTON_SPEED1.show()
    UIGRY.BUTTON_SPEED2.show()
    UIGRY.BUTTON_SPEED3.show()
    BUTTON_STAR_GAME.hide()
    BUTTON_EXIT_GAME.hide()

    while Core.BOOL_RUNNING:
        Core.screen.fill("white")
        Core.screen.blit(Core.IMAGE_MAP, (400, 0))
        dt = Core.clock.tick(60) / 1000
        UIGRY.DEF_CLOCK(dt)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                Core.BOOL_RUNNING = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pose = pygame.mouse.get_pos()
                if event.button == 1:
                    if Hub.BOOL_ADDHUB:
                        if Core.leftpanel.collidepoint(pose):
                            Hub.DEF_HUBNUMBER(x, y)
                    for i in Core.DICT_HUB:
                        if UIGRY.BUTTON_INFO:
                            if Core.DICT_HUB[i].collidepoint(pose):
                                VAL_WHATID = i
                                UIGRY.BOOL_INFO_OBJECT = False

                    for i in SimulationCore.LIST_INFANTRY:
                        if SimulationCore.LIST_INFANTRY[i].rect.collidepoint(pose):
                            VAL_WHATIDOBJECT = SimulationCore.LIST_INFANTRY[i].GET_ID()
                            UIGRY.BOOL_INFO_OBJECT = True
                elif event.button == 3:
                    for i in Core.DICT_HUB:
                        if Core.DICT_HUB[i].collidepoint(pose):
                            Hub.DEF_LINE(Core.DICT_HUB[i].center, i)

        Core.screen.blit(UIGRY.IMAGE_LEFTPANEL, (0, 0))

        if not VAL_WHATID in Core.DICT_HUB:
            VAL_WHATID = Core.VAL_CENTRALHUBID

        get_tieck = pygame.time.get_ticks()
        SimulationCore.DEF_INWHILE(dt, get_tieck)
        UIGRY.SHOW_CURRENCY()
        UIGRY.SHOW_WARNING()
        if UIGRY.BOOL_INFO:

            if UIGRY.BOOL_INFO_OBJECT:
                SimulationCore.LIST_INFANTRY[VAL_WHATIDOBJECT].DEF_Show()
                Hub.BOOL_SELECTED = False
                for u in SimulationCore.LIST_INFANTRY.values():
                    if u.VAL_ID == VAL_WHATIDOBJECT:
                        u.BOOL_SELECTED = False
                    else:
                        u.BOOL_SELECTED = True

            else:
                if VAL_WHATIDOBJECT != '':
                    SimulationCore.LIST_INFANTRY[VAL_WHATIDOBJECT].DEF_SETBOOL(True, VAL_WHATIDOBJECT)


                Hub.DEF_SELECTED(VAL_WHATID)
                UIGRY.SHOW_INFO(VAL_WHATID)
        else:
            Hub.BOOL_SELECTED = False
        if UIGRY.BOOL_ORDER:
            UIGRY.SHOW_ORDER()

        if UIGRY.BOOL_MAGAZINE:
            UIGRY.SHOW_MAGAZINE()

        if UIGRY.BOOL_SEND:
            UIGRY.SHOW_SEND(VAL_WHATID)

        if UIGRY.BOOL_CONS:
            UIGRY.SHOW_CONS()

        UIGRY.DEF_WARNING_ACTIVE()
        Core.DEF_Currency()
        Core.DEF_Weather()
        Core.SHOW_POGODA()
        Core.SHOW_TICKET()
        Core.DEF_ENDGAME(get_tieck)

        for s in Core.DICT_LINE:
            Pose = Core.DICT_LINE[s]
            pygame.draw.line(Core.screen, "black", Pose[0], Pose[1], width=5)

        for i in Core.DICT_HUB:
            Hub.DEF_SHOW(i)

        Front.draw()
        UIGRY.DEF_DISPLAY()
        pygame.draw.line(Core.screen, "Black", (400, 0), (400, 720))

        pygame_widgets.update(events)
        pygame.display.update()

        if Core.BOOL_EXIT:
            Core.BOOL_RUNNING = False
def MAIN_SCENE():
    """
        Moduł odpowiedziany za wyświetlenie menu startowego
    """
    UIGRY.BUTTON_INFO.hide()
    UIGRY.BUTTON_ORDER.hide()
    UIGRY.BUTTON_SEND.hide()
    UIGRY.BUTTON_MAGAZINE.hide()
    UIGRY.BUTTON_EXIT.hide()
    UIGRY.BUTTON_STOP.hide()
    UIGRY.BUTTON_CONS.hide()
    UIGRY.BUTTON_SPEED1.hide()
    UIGRY.BUTTON_SPEED2.hide()
    UIGRY.BUTTON_SPEED3.hide()
    Core.screen.blit(IMAGE_MAIN, (0, 0))
    Core.screen.blit(IMAGE_LOGO, (800, 100))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            Core.BOOL_RUNNING = False


    pygame_widgets.update(events)
    pygame.display.update()

    if Core.BOOL_EXIT:
        Core.BOOL_RUNNING = False


while Core.BOOL_RUNNING:

    if BOOL_GAMESCENE:
        GAME_SCENE()
    else:
        MAIN_SCENE()


pygame.quit()
