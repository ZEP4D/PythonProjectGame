import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print("hello")

    #lewa Strona Modul operacji
    pygame.draw.rect(screen,"purple",(0,0,400,720))

    #Prawa Strona Modul mapy
    pygame.draw.rect(screen, "black", (401, 0, 880, 720))

    x = 410
    for row in range(8):
        y = 10
        for column in range(6):
            pygame.draw.rect(screen, "yellow", (x, y, 100, 100))
            y = y + 110
        x = x + 110


    pygame.draw.line(screen, "black", (400, 0), (400, 720), width=3)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
