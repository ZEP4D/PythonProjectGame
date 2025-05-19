import pygame
import Core
import Hub


class MOC:
    def __init__(self):
        self.rect = pygame.Rect(699,700,20,20)
        self.VAL_SPEED_X = 2
        self.VAL_SPEED_Y = 2
        self.VAL_POSE = pygame.Vector2(self.rect.center)
        self.VAL_ID = "Jednostka"
        self.BOOL_HUB = False
        self.BOOL_HUBCONNECT = False



    def DEF_UPDATE(self,dt):
        Targetpose = FrontLine().getpositon()


        kierunek = Targetpose - self.VAL_POSE
        dystans = kierunek.length()



        if dystans > 20:
            kierunek.normalize_ip()
            self.VAL_POSE += kierunek * 100 * dt
            self.rect.topleft = (round(self.VAL_POSE.x), round(self.VAL_POSE.y))

        min_distance = float('inf')

        for i in Core.DICT_HUB:
            hubin = Core.DICT_HUB[i].center
            hub = pygame.Vector2(hubin[0],hubin[1])
            Nearestpose = self.VAL_POSE.distance_to(hub)

            if Nearestpose < min_distance:
                min_distance = Nearestpose
                self.Correcthub = hub
                if min_distance < 200 :
                    self.BOOL_HUB = True
                    self.BOOL_HUBCONNECT = True

                    info = Hub.DEF_ASTAR(i)
                else:
                    self.BOOL_HUB = False
                    self.BOOL_HUBCONNECT = False





        if self.rect.left <= 400 or self.rect.right >= Core.SizeScreenWidth:
            self.VAL_SPEED_X =  -self.VAL_SPEED_X
        if self.rect.top <=0 or self.rect.bottom >= Core.SizeScreenHeight:
            self.VAL_SPEED_Y = -self.VAL_SPEED_Y

    def DEF_DRAW(self):
        if self.BOOL_HUB:
            pygame.draw.line(Core.screen, "black", self.rect.center, self.Correcthub)

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
