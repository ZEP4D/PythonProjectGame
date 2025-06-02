import pygame
import pygame_widgets
import UIGRY
import Core
import Hub
import Objectinthemap
import SimulationCore


SimulationCore.DEF_PREWHILE()
Front = Objectinthemap.FrontLine()
Hub.DEF_HUBCENTRAL()
VAL_WHATID = Core.VAL_CENTRALHUBID
VAL_WHATIDOBJECT = ""

while Core.BOOL_RUNNING:
    Core.screen.fill("white")
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
    SimulationCore.DEF_INWHILE(dt,get_tieck)
    UIGRY.SHOW_CURRENCY()
    UIGRY.SHOW_WARNING()
    if UIGRY.BOOL_INFO:
        if UIGRY.BOOL_INFO_OBJECT:
            SimulationCore.LIST_INFANTRY[VAL_WHATIDOBJECT].DEF_Show()
        else:
            UIGRY.SHOW_INFO(VAL_WHATID)

    if UIGRY.BOOL_ORDER:
        UIGRY.SHOW_ORDER()

    if UIGRY.BOOL_MAGAZINE:
        UIGRY.SHOW_MAGAZINE()

    if UIGRY.BOOL_SEND:
        UIGRY.SHOW_SEND(VAL_WHATID)

    if UIGRY.BOOL_CONS:
        UIGRY.SHOW_CONS()
    Core.DEF_Weather()
    Core.SHOW_TICKET()
    Core.DEF_ENDGAME(get_tieck)

    for s in Core.DICT_LINE:
        Pose = Core.DICT_LINE[s]
        pygame.draw.line(Core.screen,"black",Pose[0],Pose[1],width=5)

    for i in Core.DICT_HUB:
        if i == Core.VAL_CENTRALHUBID:
            pygame.draw.rect(Core.screen, "Green", Core.DICT_HUB[i])
        else:
            pygame.draw.rect(Core.screen,"red", Core.DICT_HUB[i])

    Front.draw()
    UIGRY.DEF_DISPLAY()

    pygame_widgets.update(events)
    pygame.display.update()

    if Core.BOOL_EXIT:
        Core.BOOL_RUNNING = False

pygame.quit()
