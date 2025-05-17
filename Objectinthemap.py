import pygame
import Core
class MOC:
    def __init__(self):
        self.rect = pygame.Rect(699,700,20,20)
        self.speedx = 2
        self.speedy = 2
        self.pose = pygame.Vector2(self.rect.center)

    def update(self):
        dt = Core.clock.tick(60) / 1000
        Targetpose = FrontLine().getpositon()


        kierunek = Targetpose - self.pose
        dystans = kierunek.length()

        if dystans > 20:
            kierunek.normalize_ip()
            self.pose += kierunek * 100 * dt
            self.rect.topleft = (round(self.pose.x), round(self.pose.y))

        if self.rect.left <= 400 or self.rect.right >= Core.SizeScreenWidth:
            self.speedx =  -self.speedx
        if self.rect.top <=0 or self.rect.bottom >= Core.SizeScreenHeight:
            self.speedy = -self.speedy

    def draw(self):
        pygame.draw.rect(Core.screen,"yellow",self.rect)


class FrontLine:
    def __init__(self):
        self.Start = (410, 70)
        self.End = (1250, 70)
        self.pose1 = pygame.Rect(500,70,5,5)
        self.pose2 = pygame.Rect(746, 70, 5, 5)
        self.pose3 = pygame.Rect(914, 70, 5, 5)
        self.pose4 = pygame.Rect(1182, 70, 5, 5)


    def draw(self):
        pygame.draw.line(Core.screen,"Red", self.Start, self.End, 10)
        pygame.draw.rect(Core.screen,"Red",self.pose1)
        pygame.draw.rect(Core.screen, "Red", self.pose2)
        pygame.draw.rect(Core.screen, "Red", self.pose3)
        pygame.draw.rect(Core.screen, "Red", self.pose4)

    def getpositon(self):
        return pygame.Vector2(self.pose1.center)
