import pygame
import pygame_widgets
import UIGRY
import Core
import Hub
import Objectinthemap

object1 = Objectinthemap.MOC()
Front = Objectinthemap.FrontLine()
Hub.HubCentral()
Whatid = "HUBC"
while Core.running:
    Core.screen.fill("white")
    dt = Core.clock.tick(60) / 1000
    UIGRY.Zegar(dt)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            Core.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pose = pygame.mouse.get_pos()

            if event.button == 1:
                if Hub.Dodawaaniehubbool:
                    if Core.leftpanel.collidepoint(pose):
                        Hub.NumbersHubs(x ,y)
                for i in Core.Hublist:
                    if UIGRY.infobutton:
                        if Core.Hublist[i].collidepoint(pose):
                            Whatid = i
                if object1.rect.collidepoint(pose):
                    print("hellow")

            elif event.button == 3:
                for i in Core.Hublist:
                    if Core.Hublist[i].collidepoint(pose):
                        Hub.Line(Core.Hublist[i].center,i)

    #lewa Strona Modul operacji
    Core.screen.blit(UIGRY.Textura0,(0,0))
    #Prawa Strona Modul mapy
    #pygame.draw.rect(Core.screen,"grey",Core.leftpanel)

    object1.update(dt)
    object1.draw()

    if UIGRY.Infobool:
        UIGRY.ShowInfohubs(Whatid)
    if UIGRY.Odrderbool:
        UIGRY.ShowOrderinfo()
    if UIGRY.Magazinebool:
        UIGRY.ShowMagazineinfo()
    for s in Core.LineList:
        Pose = Core.LineList[s]
        pygame.draw.line(Core.screen,"black",Pose[0],Pose[1],width=5)

    for i in Core.Hublist:
        pygame.draw.rect(Core.screen,"red",Core.Hublist[i])


    Front.draw()
    UIGRY.Wyswielanie()

    pygame_widgets.update(events)
    pygame.display.update()

    if Core.GotoExit:
        Core.running = False

pygame.quit()
