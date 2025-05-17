import pygame
import pygame_widgets
import UIGRY
import Core
import Hub
import Objectinthemap


Whatid = ''
Hubexist = False
object1 = Objectinthemap.MOC()
Front = Objectinthemap.FrontLine()
while Core.running:
    Core.screen.fill("white")
    dt = Core.clock.tick(60) / 1000
    UIGRY.Zegar(dt)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Core.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                x, y = pygame.mouse.get_pos()
                pose = pygame.mouse.get_pos()
                if Hub.Dodawaaniehubbool:
                    if Core.leftpanel.collidepoint(pose):
                        Hub.NumbersHubs(x ,y)
                        Hubexist = True
                for i in Core.Hublist:
                    if UIGRY.infobutton:
                        if Core.Hublist[i].collidepoint(pygame.mouse.get_pos()):
                            Whatid = i
            elif pygame.mouse.get_pressed(3)[2]:
                for i in Core.Hublist:
                    if Core.Hublist[i].collidepoint(pygame.mouse.get_pos()):
                        Hub.Line(Core.Hublist[i].center,i)

    #lewa Strona Modul operacji
    Core.screen.blit(UIGRY.Textura0,(0,0))
    #Prawa Strona Modul mapy
    #pygame.draw.rect(Core.screen,"grey",Core.leftpanel)

    object1.update()
    if UIGRY.Infobool:
        if Hubexist:
            UIGRY.ShowInfohubs(Whatid)

    for s in Core.LineList:
        Pose = Core.LineList[s]
        pygame.draw.line(Core.screen,"black",Pose[0],Pose[1],width=5)

    for i in Core.Hublist:
        pygame.draw.rect(Core.screen,"red",Core.Hublist[i])

    object1.draw()
    Front.draw()
    UIGRY.Wyswielanie()

    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

    if Core.GotoExit:
        Core.running = False

pygame.quit()
