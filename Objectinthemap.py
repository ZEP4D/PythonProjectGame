import pygame
import Core
import Hub
import random

from Core import BOOL_EXIT


class MOC:
    def __init__(self,x,y,id,Front):
        self.rect = pygame.Rect(x,y,20,20)
        self.VAL_SPEED_X = 2
        self.VAL_SPEED_Y = 2
        self.VAL_POSE = pygame.Vector2(self.rect.center)
        self.VAL_ID = id
        self.VAL_AMMO = 3
        self.VAL_FUEL = 1
        self.VAL_SUPPLE = 4
        self.VAL_HEALTH = 100
        self.VAL_APC = 10
        self.VAL_Cars = 3
        self.VAL_Truck = 2
        self.VAL_Truck_Fuel = 1
        self.VAL_MENPOWER = self.VAL_HEALTH
        self.COLOR_ID = "yellow"
        self.VAL_DYSTANS = 0
        self.VAL_TRASAPRZEBYTA = 0
        self.VAL_Timepass = 0
        self.BOOL_HUB = False
        self.BOOL_HUBCONNECT = False
        self.BOOL_INMOVE = False
        self.BOOL_INBATTLE = False
        self.VAL_TARGETPOSE = pygame.Vector2(0,0)
        self.Front = Front
        self.VAL_POSENUMBER = self.Front.getnumberforposition()
        self.VAL_LASTHOUER = None
        self.VAL_DEBUFF = 0
        self.VAL_DEFENCE_BASE = 200
        self.VAL_ENEMY_ID = None

    def DEF_UPDATE(self, dt,listen):

        if self.VAL_HEALTH < 30:
            Posefromdict = Core.DICT_HUB[Core.VAL_CENTRALHUBID]
            self.VAL_TARGETPOSE = pygame.Vector2(Posefromdict.center)
            self.Front.freeposition(self.VAL_POSENUMBER)
            self.VAL_POSENUMBER = 5

        else:
            if self.VAL_POSENUMBER == 5:
                self.VAL_POSENUMBER = self.Front.getnumberforposition()

            self.VAL_TARGETPOSE = self.Front.getpositon(self.VAL_POSENUMBER, self.VAL_ID)


        kierunek = self.VAL_TARGETPOSE - self.VAL_POSE
        self.VAL_DYSTANS = kierunek.length()

        if self.VAL_DYSTANS > 30:
            kierunek.normalize_ip()
            ruch = kierunek * (5 * Core.VAL_SPPEDTIME ) * dt
            self.VAL_POSE += ruch
            self.VAL_TRASAPRZEBYTA += ruch.length()
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
                    for ID in Trasa:
                        if ID == Core.VAL_CENTRALHUBID:
                            if Core.VAL_HOURS % 5 == 0 and Core.VAL_MINUTES == 0:
                                id_hub = Trasa[len(Trasa)-1]
                                if self.VAL_FUEL < 0.8:
                                    if self.VAL_Truck_Fuel > 0:
                                        if Core.DICT_FUEL[id_hub] > 0:
                                            Core.DICT_FUEL[id_hub] -= 2
                                            self.VAL_FUEL += 2
                                if self.VAL_AMMO < 2:
                                    if Core.DICT_AMMO[id_hub] > 0:
                                        Core.DICT_AMMO[id_hub] -= 2
                                        self.VAL_AMMO += 2
                                if self.VAL_SUPPLE < 5:
                                    if Core.DICT_SUPPLE[id_hub] > 0:
                                        Core.DICT_SUPPLE[id_hub] -= 4
                                        self.VAL_SUPPLE += 4

                else:
                    self.BOOL_HUB = False
                    self.BOOL_HUBCONNECT = False

            min_distance = float('inf')
            for enemy in listen:
                enemy_distance = pygame.Vector2(listen[enemy].VAL_POSE.x, listen[enemy].VAL_POSE.y)
                Nearestpose = self.VAL_POSE.distance_to(enemy_distance)
                if Nearestpose < min_distance:
                    min_distance = Nearestpose
                    if min_distance < 80:
                        self.BOOL_INBATTLE = True
                        self.VAL_ENEMY_ID = enemy
                    else:
                        self.BOOL_INBATTLE = False

        if self.rect.left <= 400 or self.rect.right >= Core.SizeScreenWidth:
            self.VAL_SPEED_X =  -self.VAL_SPEED_X
        if self.rect.top <=0 or self.rect.bottom >= Core.SizeScreenHeight:
            self.VAL_SPEED_Y = -self.VAL_SPEED_Y
    def DEF_UPDATE_RES(self,dt):

        Fuel_Usage = Core.DEF_FUELUSE(self.VAL_APC,self.VAL_Cars,self.VAL_Truck,self.VAL_Truck_Fuel)

        if self.BOOL_INMOVE:
            if self.VAL_TRASAPRZEBYTA >= 200:
                Convert = Core.DEF_Convert(self.VAL_FUEL,1,"FUEL")
                Convert -= Fuel_Usage
                self.VAL_FUEL = Core.DEF_Convert(Convert, 2,"FUEL")
                self.VAL_TRASAPRZEBYTA -= 200
        else:
                Fuel_Usage_STOP = Fuel_Usage / 5

                if self.VAL_Timepass >= 1000:
                    Convert = Core.DEF_Convert(self.VAL_FUEL, 1, "FUEL")
                    Convert -= Fuel_Usage_STOP
                    self.VAL_FUEL = Core.DEF_Convert(Convert, 2,"FUEL")
                    self.VAL_Timepass = 0
                self.VAL_Timepass += 1

        if Core.VAL_HOURS == 12 and Core.VAL_MINUTES == 0:
            Convert = Core.DEF_Convert(self.VAL_SUPPLE,1, "SUPPLE")
            Convert -= 300
            self.VAL_SUPPLE = Core.DEF_Convert(Convert,2,"SUPPLE")
    def DEF_DRAW(self):
        if self.BOOL_HUB:
            pygame.draw.line(Core.screen, "black", self.rect.center, self.Correcthub)
        pygame.draw.rect(Core.screen,self.COLOR_ID,self.rect)
    def DEF_Show(self):
        ID = Core.font2.render("ID: "+str(self.VAL_ID), True, "White")
        IDShowRect = ID.get_rect()
        IDShowRect.x = 150
        IDShowRect.y = 300
        Core.screen.blit(ID, IDShowRect)

        Health = Core.font2.render("Health: "+str(self.VAL_HEALTH), True, "White")
        HealthoShowRect = Health.get_rect()
        HealthoShowRect.x = 150
        HealthoShowRect.y = 330
        Core.screen.blit(Health, HealthoShowRect)

        Ammo = Core.font2.render("Ammo: "+str(self.VAL_AMMO), True, "White")
        AmmoShowRect = Ammo.get_rect()
        AmmoShowRect.x = 150
        AmmoShowRect.y = 360
        Core.screen.blit(Ammo, AmmoShowRect)

        Fuel_show =self.VAL_FUEL
        if type(Fuel_show) == int:
            format_fuel = Fuel_show
        else:
            format_fuel = '{:.4f}'.format(Fuel_show)

        Fuel = Core.font2.render("Fuel: "+str(format_fuel), True, "White")
        FuelShowRect = Fuel.get_rect()
        FuelShowRect.x = 150
        FuelShowRect.y = 390
        Core.screen.blit(Fuel, FuelShowRect)

        Supple = Core.font2.render("Supple: "+str(self.VAL_SUPPLE), True, "White")
        SuppleShowRect = Supple.get_rect()
        SuppleShowRect.x = 150
        SuppleShowRect.y = 420
        Core.screen.blit(Supple, SuppleShowRect)
    def GET_ID(self):
        return self.VAL_ID
    def DEF_BATTLE(self,ticket,Enemy):

        if self.BOOL_INBATTLE:


            # dane w procentach
            if Core.BOOL_GoodW:
               self.VAL_DEBUFF = 0
            elif Core.BOOL_Rain:
                self.VAL_DEBUFF = 20
            elif Core.BOOL_fog:
                self.VAL_DEBUFF = 50
            elif Core.BOOL_Thunder:
                self.VAL_DEBUFF = 35


            if Core.VAL_HOURS % 2 == 0 and Core.VAL_MINUTES == 0:
                if self.VAL_LASTHOUER != Core.VAL_HOURS:
                    howhavemove = random.randint(1, 2)
                    match (howhavemove):
                        case 1:  # Tura AI Gracz
                            if ticket - Core.Star_Tiecket >= 3000:
                                punkty = Core.DEF_POINTSCALCULATOR(self.VAL_APC, self.VAL_Cars, self.VAL_MENPOWER)

                                if punkty > 200:
                                    howmenymanpower = random.randint(0, 20)
                                    Enemy[self.VAL_ENEMY_ID].VAL_HEALTH = Enemy[self.VAL_ENEMY_ID].VAL_HEALTH - howmenymanpower

                                else:
                                    howmenyapc = random.randint(0, 20)
                                    howmenycars = random.randint(0, 20)
                                    howmenymanpower = random.randint(0, 20)

                                    self.VAL_APC = self.VAL_APC - howmenyapc
                                    self.VAL_Cars = self.VAL_Cars - howmenycars
                                    self.VAL_Health = self.VAL_HEALTH - howmenymanpower

                        case 2:  # Tura AI Wroga
                            if ticket - Core.Star_Tiecket >= 3000:
                                print("Enemy")
                    self.VAL_LASTHOUER = Core.VAL_HOURS

class Infantry(MOC):
    def __init__(self,x,y,id,num):
        super().__init__(x,y,id,num)
        self.VAL_HEALTH = 100
        self.VAL_FUEL = 1
        self.VAL_AMMO = 100
        self.VAL_SUPPLE = 30
        self.COLOR_ID = "Black"

class FrontLine:
    def __init__(self):
        self.Start = (410, 90)
        self.End = (1250, 90)
        self.pose1 = pygame.Rect(500,90,10,10)
        self.pose2 = pygame.Rect(746, 90,10, 10)
        self.pose3 = pygame.Rect(914, 90, 10,10)
        self.pose4 = pygame.Rect(1182, 90, 10, 10)
        self.BOOL_pose1 = True
        self.BOOL_pose2 = True
        self.BOOL_pose3 = True
        self.BOOL_pose4 = True
        self.VAL_IDpose1 = "none"
        self.VAL_IDpose2 = "none"
        self.VAL_IDpose3 = "none"
        self.VAL_IDpose4 = "none"
    def draw(self):

        pygame.draw.line(Core.screen,"Grey", self.Start, self.pose1.center, 3)
        pygame.draw.line(Core.screen,"Grey",self.pose1.center,self.pose2.center,3)
        pygame.draw.line(Core.screen, "Grey", self.pose2.center, self.pose3.center, 3)
        pygame.draw.line(Core.screen, "Grey", self.pose3.center, self.pose4.center, 3)
        pygame.draw.line(Core.screen, "Grey", self.pose4.center, self.End, 3)

        pygame.draw.rect(Core.screen, "RED", self.pose1)
        pygame.draw.rect(Core.screen, "RED", self.pose2)
        pygame.draw.rect(Core.screen, "RED", self.pose3)
        pygame.draw.rect(Core.screen, "RED", self.pose4)

    def getpositon(self,number, id):
        match(number):
            case 1:
                self.VAL_IDpose1 = id
                return pygame.Vector2(self.pose1.center)
            case 2:
                self.VAL_IDpose2 = id
                return pygame.Vector2(self.pose2.center)
            case 3:
                self.VAL_IDpose3 = id
                return pygame.Vector2(self.pose3.center)
            case 4:
                self.VAL_IDpose4 = id
                return pygame.Vector2(self.pose4.center)
            case 5:
                Posefromdict = Core.DICT_HUB[Core.VAL_CENTRALHUBID]
                return pygame.Vector2(Posefromdict.center)
    def getnumberforposition(self):
        if self.BOOL_pose1:
            self.BOOL_pose1 = False
            return 1
        elif self.BOOL_pose2:
            self.BOOL_pose2 = False
            return 2
        elif self.BOOL_pose3:
            self.BOOL_pose3 = False
            return 3
        elif self.BOOL_pose4:
            self.BOOL_pose4 = False
            return 4
        else:
            return 5
    def freeposition(self,number):
        match (number):
            case 1:
                self.BOOL_pose1 = True
            case 2:
                self.BOOL_pose2 = True
            case 3:
                self.BOOL_pose3 = True
            case 4:
                self.BOOL_pose4 = True

class ENEMY:
    def __init__(self,x,y,front):
        self.VAL_HEALTH = 100
        self.VAL_ID = "e1"
        self.rect = pygame.Rect(x, y, 20, 20)
        self.Front = front
        self.VAL_POSENUMBER = self.Front.getnumberforposition()
        self.VAL_TARGETPOSE = pygame.Vector2(0, 0)
        self.VAL_DYSTANS = 0
        self.VAL_POSE = pygame.Vector2(self.rect.center)
        self.VAL_DEFENCE_BASE = 100
        self.VAL_ATTACK_POINT = 220

    def DEF_UPDATE(self,dt):

        if self.VAL_HEALTH < 30:
            self.VAL_TARGETPOSE = pygame.Vector2(400,-1)
            self.Front.freeposition(self.VAL_POSENUMBER)
            self.VAL_POSENUMBER = 5

        else:
            if self.VAL_POSENUMBER == 5:
                self.VAL_POSENUMBER = self.Front.getnumberforposition()

            self.VAL_TARGETPOSE = self.Front.getpositon(self.VAL_POSENUMBER, self.VAL_ID)


        kierunek = self.VAL_TARGETPOSE - self.VAL_POSE
        self.VAL_DYSTANS = kierunek.length()

        if self.VAL_DYSTANS > 50:
            kierunek.normalize_ip()
            ruch = kierunek * (5 * Core.VAL_SPPEDTIME ) * dt
            self.VAL_POSE += ruch
            self.rect.topleft = (round(self.VAL_POSE.x), round(self.VAL_POSE.y))

    def DEF_DRAW(self):
        pygame.draw.rect(Core.screen,"BROWN",self.rect)

    def GET_HEALTH(self):
        return self.VAL_HEALTH

    def SET_HEALTH(self,val):
        self.VAL_HEALTH = val