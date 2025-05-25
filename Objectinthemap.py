import pygame
import Core
import Hub


class MOC:
    def __init__(self,x,y,id):
        self.rect = pygame.Rect(x,y,20,20)
        self.VAL_SPEED_X = 2
        self.VAL_SPEED_Y = 2
        self.VAL_POSE = pygame.Vector2(self.rect.center)
        self.VAL_ID = id
        self.VAL_AMMO = 20
        self.VAL_FUEL = 2
        self.VAL_SUPPLE = 150
        self.VAL_HEALTH = 200
        self.VAL_APC = 10
        self.VAL_Cars = 3
        self.VAL_Truck = 2
        self.VAL_MENPOWER = 100
        self.BOOL_HUB = False
        self.BOOL_HUBCONNECT = False
        self.COLOR_ID = "yellow"
        self.VAL_DYSTANS = 0
        self.BOOL_INMOVE = False
        self.VAL_TRASAPRZEBYTA = 0
    def DEF_UPDATE(self,dt):

        if self.VAL_HEALTH < 30:
            Posefromdict = Core.DICT_HUB[Core.VAL_CENTRALHUBID]
            Targetpose = pygame.Vector2(Posefromdict.center)
        else:
            Targetpose = FrontLine().getpositon()


        kierunek = Targetpose - self.VAL_POSE
        self.VAL_DYSTANS = kierunek.length()

        if self.VAL_DYSTANS > 20:
            kierunek.normalize_ip()
            self.VAL_POSE += kierunek * (20 * Core.VAL_SPPEDTIME ) * dt
            self.rect.topleft = (round(self.VAL_POSE.x), round(self.VAL_POSE.y))
            self.BOOL_INMOVE = True
        else:
            self.BOOL_INMOVE = False

        min_distance = float('inf')

        for HUBID in Core.DICT_HUB:
            hubin = Core.DICT_HUB[HUBID].center
            hub = pygame.Vector2(hubin[0],hubin[1])
            Nearestpose = self.VAL_POSE.distance_to(hub)

            if Nearestpose < min_distance:
                min_distance = Nearestpose
                self.Correcthub = hub
                if min_distance < 200 :
                    self.BOOL_HUB = True
                    self.BOOL_HUBCONNECT = True
                    Trasa = Hub.DEF_ASTAR(HUBID)
                    #for ID in Trasa:
                        #if ID == Core.VAL_CENTRALHUBID:

                else:
                    self.BOOL_HUB = False
                    self.BOOL_HUBCONNECT = False


        if self.rect.left <= 400 or self.rect.right >= Core.SizeScreenWidth:
            self.VAL_SPEED_X =  -self.VAL_SPEED_X
        if self.rect.top <=0 or self.rect.bottom >= Core.SizeScreenHeight:
            self.VAL_SPEED_Y = -self.VAL_SPEED_Y
    def DEF_UPDATE_RES(self,dt):


        if self.BOOL_INMOVE:
            self.VAL_TRASAPRZEBYTA += 1

            if self.VAL_TRASAPRZEBYTA == 100:
                self.VAL_FUEL -= 0.716
                self.VAL_TRASAPRZEBYTA = 0

            print(self.VAL_TRASAPRZEBYTA, self.VAL_FUEL, self.VAL_ID)




    def DEF_DRAW(self):
        if self.BOOL_HUB:
            pygame.draw.line(Core.screen, "black", self.rect.center, self.Correcthub)
        pygame.draw.rect(Core.screen,self.COLOR_ID,self.rect)
    def DEF_Show(self):
        ID = Core.font2.render(str(self.VAL_ID), True, "White")
        IDShowRect = ID.get_rect()
        IDShowRect.x = 150
        IDShowRect.y = 300
        Core.screen.blit(ID, IDShowRect)

        Health = Core.font2.render(str(self.VAL_HEALTH), True, "White")
        HealthoShowRect = Health.get_rect()
        HealthoShowRect.x = 150
        HealthoShowRect.y = 330
        Core.screen.blit(Health, HealthoShowRect)

        Ammo = Core.font2.render(str(self.VAL_AMMO), True, "White")
        AmmoShowRect = Ammo.get_rect()
        AmmoShowRect.x = 150
        AmmoShowRect.y = 360
        Core.screen.blit(Ammo, AmmoShowRect)

        Fuel = Core.font2.render(str(self.VAL_FUEL), True, "White")
        FuelShowRect = Fuel.get_rect()
        FuelShowRect.x = 150
        FuelShowRect.y = 390
        Core.screen.blit(Fuel, FuelShowRect)

        Supple = Core.font2.render(str(self.VAL_SUPPLE), True, "White")
        SuppleShowRect = Supple.get_rect()
        SuppleShowRect.x = 150
        SuppleShowRect.y = 420
        Core.screen.blit(Supple, SuppleShowRect)
    def GET_ID(self):
        return self.VAL_ID
    def CHANGE_HEALTH(self,HP,number):
        if number == 0:
            self.VAL_HEALTH += HP
        if number == 1:
            self.VAL_HEALTH -= HP
    def CHANGE_AMMO(self,Ammo,number):
        if number == 0:
            self.VAL_AMMO += Ammo
        if number == 1:
            self.VAL_AMMO -= Ammo

class Infantry(MOC):
    def __init__(self,x,y,id):
        super().__init__(x,y,id)
        self.VAL_HEALTH = 100
        self.VAL_FUEL = 2
        self.VAL_AMMO = 100
        self.VAL_SUPPLE = 30
        self.COLOR_ID = "Black"

class Mechanized(MOC):
    def __init__(self,x,y,id):
        super.__init__(x,y,id)

class InfantryE(MOC):
    def __init__(self,x,y,id):
        super().__init__(x,y,id)
        self.COLOR_ID = "brown"

class FrontLine:
    def __init__(self):
        self.Start = (410, 90)
        self.End = (1250, 90)
        self.pose1 = pygame.Rect(500,90,5,5)
        self.pose2 = pygame.Rect(746, 90, 5, 5)
        self.pose3 = pygame.Rect(914, 90, 5, 5)
        self.pose4 = pygame.Rect(1182, 90, 5, 5)
    def draw(self):
        pygame.draw.line(Core.screen,"Red", self.Start, self.pose1.center, 10)
        pygame.draw.line(Core.screen,"Red",self.pose1.center,self.pose2.center,10)
        pygame.draw.line(Core.screen, "Red", self.pose2.center, self.pose3.center, 10)
        pygame.draw.line(Core.screen, "Red", self.pose3.center, self.pose4.center, 10)
        pygame.draw.line(Core.screen, "Red", self.pose4.center, self.End, 10)
    def getpositon(self):
        return pygame.Vector2(self.pose1.center)
