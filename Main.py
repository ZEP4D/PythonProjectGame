import pygame
import pygame_widgets
import UIGRY
import Core
import Hub


leftpanel = pygame.Rect(401,0,900,720)
enem = pygame.draw.rect(Core.screen, "yellow", (800, 250, 30, 30))
Whatid = ''
Hubexist = False
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
                    if leftpanel.collidepoint(pose):
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
    pygame.draw.rect(Core.screen,"grey",leftpanel)

    HubShow = Core.font2.render(str(Hub.Inthemoment), True, "black")
    MaxShowRect = HubShow.get_rect()
    MaxShowRect.x = 350
    MaxShowRect.y = 40
    Core.screen.blit(HubShow, MaxShowRect)
    

    if UIGRY.Infobool:
        if Hubexist:
            UIGRY.ShowInfohubs(Whatid)

    for s in Core.LineList:
        Pose = Core.LineList[s]
        pygame.draw.line(Core.screen,"black",Pose[0],Pose[1],width=5)

    for i in Core.Hublist:
        pygame.draw.rect(Core.screen,"red",Core.Hublist[i])



    UIGRY.Wyswielanie()
    pygame.draw.line(Core.screen, "black", (400, 0), (400, 720), width=3)

    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

    if Core.GotoExit:
        Core.running = False

pygame.quit()
