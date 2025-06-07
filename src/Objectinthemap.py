import pygame
import Core
import Hub
import random




class MOC:
    def __init__(self,x,y,id,Front):
        self.texture = pygame.image.load("../Texture/MAP/placeholder.png").convert_alpha()
        self.image = self.texture
        self.rect = self.image.get_rect(center=(x,y))
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
        self.BOOL_SELECTED = False

    def DEF_UPDATE(self, dt,listen):
        """
        if self.VAL_HEALTH < 30:
            Posefromdict = Core.DICT_HUB[Core.VAL_CENTRALHUBID]
            self.VAL_TARGETPOSE = pygame.Vector2(Posefromdict.center)
            self.Front.freeposition(self.VAL_POSENUMBER)
            self.VAL_POSENUMBER = 5
        else:
            if self.VAL_POSENUMBER == 5:
            self.VAL_POSENUMBER = self.Front.getnumberforposition()
        self.VAL_TARGETPOSE = self.Front.getpositon(self.VAL_POSENUMBER, self.VAL_ID)

        Jeżeli zdrowie jednostki spadnie poniżej 30:
            - Pobierana jest pozycja centralnego huba (Core.VAL_CENTRALHUBID).
            - Jednostka ustawia cel VAL_TARGETPOSE
            - Aktualna pozycja zostaje zwolniona, a jednostka przypisywana jest do pozycji nr 5
        W innym przypadku:
            - Jeśli jednostka znajduje się na pozycji awaryjnej, przydzielana jest nowa pozycja.
            - Cel ruchu zostaje zaktualizowany zgodnie z nową pozycją.

        kierunek = self.VAL_TARGETPOSE - self.VAL_POSE
        self.VAL_DYSTANS = kierunek.length()
        if self.VAL_DYSTANS > 30:
            kierunek.normalize_ip()
            ruch = kierunek * (5 * Core.VAL_SPPEDTIME) * dt
            self.VAL_POSE += ruch
            self.VAL_TRASAPRZEBYTA += ruch.length()
            self.rect.topleft = (round(self.VAL_POSE.x), round(self.VAL_POSE.y))
            self.BOOL_INMOVE = True
        else:
            self.BOOL_INMOVE = False

        - Obliczany jest wektor kierunku i dystans do celu.
        - Jeżeli jednostka znajduje się dalej niż 30 pikseli od celu:
        - Przemieszcza się w jego kierunku z prędkością zależną od Core.VAL_SPPEDTIME i dt.
        - Aktualizowana jest pozycja graficzna
        - Ustawiany jest znacznik ruchu BOOL_INMOVE.

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

        - Dla każdego huba w Core.DICT_HUB:
        - Obliczana jest odległość od jednostki.
        - Jeżeli najbliższy hub znajduje się w promieniu 200 pikseli:
        - Jednostka łączy się z hubem (BOOL_HUB, BOOL_HUBCONNECT).
        - Jeżeli do huba prowadzi bezpośrednia trasa:
        - Co dwie godziny , zdrowie jednostki regeneruje się.
        - Co 5 godzin jednostka może zatankować, uzupełnić amunicję i zaopatrzenie

        - Przeglądana jest lista przeciwników (listen).
        - Jeżeli któryś znajduje się bliżej niż 80 pikseli:
        - Jednostka wchodzi w stan walki (BOOL_INBATTLE) i zapamiętuje ID wroga.

        min_distance_ene = float('inf')
        for enemy in listen:
            min_distance_en = pygame.Vector2(listen[enemy].VAL_POSE.x, listen[enemy].VAL_POSE.y)
            Nearestpose = self.VAL_POSE.distance_to(min_distance_en)
            if Nearestpose < min_distance_ene:
            min_distance_ene = Nearestpose
            if min_distance_ene < 80:
                self.BOOL_INBATTLE = True
                self.VAL_ENEMY_ID = enemy
            else:
                self.BOOL_INBATTLE = False

        :param dt: Delta time
        :param listen: Lista przeciwników
        """
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
            ruch = kierunek * (5 * Core.VAL_SPPEDTIME) * dt
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

                    if len(Trasa) == 1:
                        if Trasa[0] == Core.VAL_CENTRALHUBID:
                            if self.VAL_HEALTH < 100:
                                if Core.VAL_HOURS % 2 == 0 and Core.VAL_MINUTES == 0:
                                        self.VAL_HEALTH += 10
                    for ID in Trasa:
                        if ID == Core.VAL_CENTRALHUBID:
                            if Core.VAL_HOURS % 5 == 0 and Core.VAL_MINUTES == 0:
                                id_hub = Trasa[len(Trasa)-1]
                                if self.VAL_FUEL < 0.8:
                                    if self.VAL_Truck_Fuel > 0:
                                        if Core.DICT_FUEL[id_hub] > 0:
                                            Core.DICT_FUEL[id_hub] -= 2
                                            self.VAL_FUEL += 2
                                if self.VAL_AMMO < 5:
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

        min_distance_ene = float('inf')
        for enemy in listen:
            min_distance_en = pygame.Vector2(listen[enemy].VAL_POSE.x, listen[enemy].VAL_POSE.y)
            Nearestpose = self.VAL_POSE.distance_to(min_distance_en)
            if Nearestpose < min_distance_ene:
                min_distance_ene = Nearestpose
                if min_distance_ene < 80:
                    self.BOOL_INBATTLE = True
                    self.VAL_ENEMY_ID = enemy
                else:
                    self.BOOL_INBATTLE = False


        if  self.BOOL_SELECTED:
            self.image = self.texture


        if self.rect.left <= 400 or self.rect.right >= Core.SizeScreenWidth:
            self.VAL_SPEED_X =  -self.VAL_SPEED_X
        if self.rect.top <=0 or self.rect.bottom >= Core.SizeScreenHeight:
            self.VAL_SPEED_Y = -self.VAL_SPEED_Y
    def DEF_UPDATE_RES(self,dt):
        """
            Obliczane jest zużycie paliwa na podstawie typu pojazdów (APC, Cars, Truck, Truck_Fuel).

            Fuel_Usage = Core.DEF_FUELUSE(self.VAL_APC, self.VAL_Cars, self.VAL_Truck, self.VAL_Truck_Fuel)

            Gdy jednostka się porusza (BOOL_INMOVE):
            - Po przebyciu co najmniej 200 pikseli:
            - Paliwo jest konwertowane na wartość liczbową, pomniejszane o zużycie, i konwertowane z powrotem.

                if self.BOOL_INMOVE:
                    if self.VAL_TRASAPRZEBYTA >= 200:
                        Convert = Core.DEF_Convert(self.VAL_FUEL, 1, "FUEL")
                        Convert -= Fuel_Usage
                        self.VAL_FUEL = Core.DEF_Convert(Convert, 2, "FUEL")
                        self.VAL_TRASAPRZEBYTA -= 200

        Gdy jednostka jest zatrzymana:
        - Zużycie paliwa jest 5 razy mniejsze.
        - Co 1000 jednostek czasu (VAL_Timepass), zużywane jest paliwo według tego samego schematu.

         Fuel_Usage_STOP = Fuel_Usage / 5

            if self.VAL_Timepass >= 1000:
                Convert = Core.DEF_Convert(self.VAL_FUEL, 1, "FUEL")
                Convert -= Fuel_Usage_STOP
                self.VAL_FUEL = Core.DEF_Convert(Convert, 2, "FUEL")
                self.VAL_Timepass = 0
                self.VAL_Timepass += 1


        O każdej 12:00 zużywane jest 300 jednostek zaopatrzenia.

            if Core.VAL_HOURS == 12 and Core.VAL_MINUTES == 0:
                Convert = Core.DEF_Convert(self.VAL_SUPPLE, 1, "SUPPLE")
                Convert -= 300
                self.VAL_SUPPLE = Core.DEF_Convert(Convert, 2, "SUPPLE")

        :param dt: Delta time
        """
        Fuel_Usage = Core.DEF_FUELUSE(self.VAL_APC, self.VAL_Cars, self.VAL_Truck, self.VAL_Truck_Fuel)

        if self.BOOL_INMOVE:
            if self.VAL_TRASAPRZEBYTA >= 200:
                Convert = Core.DEF_Convert(self.VAL_FUEL, 1, "FUEL")
                Convert -= Fuel_Usage
                self.VAL_FUEL = Core.DEF_Convert(Convert, 2, "FUEL")
                self.VAL_TRASAPRZEBYTA -= 200
        else:
                Fuel_Usage_STOP = Fuel_Usage / 5

                if self.VAL_Timepass >= 1000:
                    Convert = Core.DEF_Convert(self.VAL_FUEL, 1, "FUEL")
                    Convert -= Fuel_Usage_STOP
                    self.VAL_FUEL = Core.DEF_Convert(Convert, 2, "FUEL")
                    self.VAL_Timepass = 0
                self.VAL_Timepass += 1

        if Core.VAL_HOURS == 12 and Core.VAL_MINUTES == 0:
            Convert = Core.DEF_Convert(self.VAL_SUPPLE, 1, "SUPPLE")
            Convert -= 300
            self.VAL_SUPPLE = Core.DEF_Convert(Convert, 2, "SUPPLE")
    def DEF_DRAW(self):
        """
                Wyświetlenie  na ekranie obiektu
        """

        if self.BOOL_HUB:
            pygame.draw.line(Core.screen, "black", self.rect.center, self.Correcthub)

        
        Core.screen.blit(self.image, self.rect)
    def DEF_Show(self):
        """
                Wyświetlenie informacji w panelu o zasobach jednostki
        """
        self.image = pygame.image.load("../Texture/MAP/AI_P_ON.png").convert_alpha()
        ID = Core.font2.render("ID: " + str(self.VAL_ID), True, "White")
        IDShowRect = ID.get_rect()
        IDShowRect.x = 180
        IDShowRect.y = 420
        Core.screen.blit(ID, IDShowRect)

        Health = Core.font2.render("Health: " + str(self.VAL_HEALTH), True, "White")
        HealthoShowRect = Health.get_rect()
        HealthoShowRect.x = 180
        HealthoShowRect.y = 450
        Core.screen.blit(Health, HealthoShowRect)

        Ammo_show = self.VAL_AMMO
        if type(Ammo_show) == int:
            format_ammo =  Ammo_show
        else:
            format_ammo = '{:.4f}'.format( Ammo_show)


        Ammo = Core.font2.render("Ammo: " + str(format_ammo), True, "White")
        AmmoShowRect = Ammo.get_rect()
        AmmoShowRect.x = 180
        AmmoShowRect.y = 480
        Core.screen.blit(Ammo, AmmoShowRect)

        Fuel_show =self.VAL_FUEL
        if type(Fuel_show) == int:
            format_fuel = Fuel_show
        else:
            format_fuel = '{:.4f}'.format(Fuel_show)

        Fuel = Core.font2.render("Fuel: " + str(format_fuel), True, "White")
        FuelShowRect = Fuel.get_rect()
        FuelShowRect.x = 180
        FuelShowRect.y = 510
        Core.screen.blit(Fuel, FuelShowRect)

        Supple = Core.font2.render("Supple: " + str(self.VAL_SUPPLE), True, "White")
        SuppleShowRect = Supple.get_rect()
        SuppleShowRect.x = 180
        SuppleShowRect.y = 540
        Core.screen.blit(Supple, SuppleShowRect)
    def GET_ID(self):
        """
        :return: Zwracanie ID obiektu
        """
        return self.VAL_ID
    def DEF_BATTLE(self,ticket,Enemy):
        """
        Na podstawie warunków pogodowych ustawiany jest debuff:
          - Dobra pogoda: brak debuffa.
          - Deszcz (Rain): -20% skuteczności.
          - Mgła (fog): -50% skuteczności.
          - Burza (Thunder): -35% skuteczności.



        Losowanie tury ataku

        Gracz:
            - Obliczane są punkty ataku.
            - Porównywane z obroną przeciwnika.
            - Jeżeli przewaga punktów: wróg traci zdrowie, gracz traci amunicję.
            - W przeciwnym przypadku: gracz traci APC, samochody, zdrowie i amunicję.
        Wróg:
            - Analogicznie porównywana jest siła ataku wroga z obroną gracza.
            - Przy przewadze: gracz traci zasoby.
            - W przeciwnym przypadku: wróg traci zdrowie.


        :param ticket: Aktualny ticekt czasu
        :param Enemy: Lista przeciwnika
        """
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
                            if ticket - Core.Star_Ticket >= 3000:
                                punkty = Core.DEF_POINTSCALCULATOR(self.VAL_APC, self.VAL_Cars, self.VAL_MENPOWER)
                                VAL_ENEMY_DEFENCE = Enemy[self.VAL_ENEMY_ID].VAL_DEFENCE_BASE

                                fpunkty = punkty - (punkty * (self.VAL_DEBUFF / 100))

                                if fpunkty > VAL_ENEMY_DEFENCE:
                                    howmenymanpower = random.randint(2, 20)
                                    Enemy[self.VAL_ENEMY_ID].VAL_HEALTH = Enemy[self.VAL_ENEMY_ID].VAL_HEALTH - howmenymanpower
                                    Core.VAL_TICKET_ENEMY -= 5
                                    Ammolost = random.randint(4,12)
                                    Ammolost = Ammolost / 10
                                    self.VAL_AMMO = self.VAL_AMMO - Ammolost

                                else:
                                    howmenyapc = random.randint(4, 20)
                                    howmenycars = random.randint(4, 20)
                                    howmenymanpower = random.randint(2, 20)
                                    Ammolost = random.randint(4, 12)
                                    Ammolost = Ammolost / 10

                                    Core.VAL_TICKET_PLAYER -= 5
                                    self.VAL_AMMO = self.VAL_AMMO - Ammolost
                                    self.VAL_APC = self.VAL_APC - howmenyapc
                                    self.VAL_Cars = self.VAL_Cars - howmenycars
                                    self.VAL_HEALTH -= howmenymanpower

                        case 2:  # Tura AI Wroga
                            if ticket - Core.Star_Ticket >= 3000:
                                VAL_ENEMY_POINT = Enemy[self.VAL_ENEMY_ID].VAL_ATTACK_POINT
                                fpunkty = VAL_ENEMY_POINT - (VAL_ENEMY_POINT * (self.VAL_DEBUFF / 100))
                                if fpunkty > self.VAL_DEFENCE_BASE:
                                    howmenyapc = random.randint(4, 20)
                                    howmenycars = random.randint(4, 20)
                                    howmenymanpower = random.randint(2, 20)
                                    Ammolost = random.randint(4, 12)
                                    Ammolost = Ammolost / 10
                                    Core.VAL_TICKET_PLAYER -= 5
                                    self.VAL_AMMO = self.VAL_AMMO - Ammolost
                                    self.VAL_APC = self.VAL_APC - howmenyapc
                                    self.VAL_Cars = self.VAL_Cars - howmenycars
                                    self.VAL_HEALTH = self.VAL_HEALTH - howmenymanpower
                                else:
                                    Ammolost = random.randint(4, 12)
                                    Ammolost = Ammolost / 10
                                    self.VAL_AMMO = self.VAL_AMMO - Ammolost
                                    howmenymanpower = random.randint(0, 20)
                                    Core.VAL_TICKET_ENEMY -= 5
                                    Enemy[self.VAL_ENEMY_ID].VAL_HEALTH = Enemy[self.VAL_ENEMY_ID].VAL_HEALTH - howmenymanpower
                    self.VAL_LASTHOUER = Core.VAL_HOURS
    def DEF_SETBOOL(self,flaga,id):
        """
        Zmienianie flagi BOOL_SELECTED dla wybranej jednostki przez jej ID
        :param flaga: parametr True/False
        :param id:  id jednostki
        :return:
        """
        if self.VAL_ID == id:
            self.BOOL_SELECTED = flaga
        else:
            self.BOOL_SELECTED = False

class Infantry(MOC):
    def __init__(self,x,y,id,num):
        super().__init__(x,y,id,num)
        self.texture = pygame.image.load("../Texture/MAP/AI_P_OFF.png").convert_alpha()
        self.image = self.texture
        self.VAL_HEALTH = 100
        self.VAL_FUEL = 2
        self.VAL_AMMO = 50
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
        """
                Wyświetlenie  na ekranie obiektu
        """
        pygame.draw.line(Core.screen, "Grey", self.Start, self.pose1.center, 3)
        pygame.draw.line(Core.screen, "Grey", self.pose1.center, self.pose2.center, 3)
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
        self.image = pygame.image.load("../Texture/MAP/AI_E.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.VAL_X = x
        self.Front = front
        self.VAL_POSENUMBER = self.Front.getnumberforposition()
        self.VAL_TARGETPOSE = pygame.Vector2(0, 0)
        self.VAL_DYSTANS = 0
        self.VAL_POSE = pygame.Vector2(self.rect.center)
        self.VAL_DEFENCE_BASE = 200
        self.VAL_ATTACK_POINT = 220
        self.BOOL_Move = False
    def DEF_UPDATE(self,dt):
        """
        if self.VAL_HEALTH < 30:
            Posefromdict = Core.DICT_HUB[Core.VAL_CENTRALHUBID]
            self.VAL_TARGETPOSE = pygame.Vector2(Posefromdict.center)
            self.Front.freeposition(self.VAL_POSENUMBER)
            self.VAL_POSENUMBER = 5
        else:
            if self.VAL_POSENUMBER == 5:
            self.VAL_POSENUMBER = self.Front.getnumberforposition()
        self.VAL_TARGETPOSE = self.Front.getpositon(self.VAL_POSENUMBER, self.VAL_ID)

        Jeżeli zdrowie jednostki spadnie poniżej 30:
            - Pobierana jest pozycja centralnego huba (Core.VAL_CENTRALHUBID).
            - Jednostka ustawia cel VAL_TARGETPOSE
            - Aktualna pozycja zostaje zwolniona, a jednostka przypisywana jest do pozycji nr 5
        W innym przypadku:
            - Jeśli jednostka znajduje się na pozycji awaryjnej, przydzielana jest nowa pozycja.
            - Cel ruchu zostaje zaktualizowany zgodnie z nową pozycją.

        kierunek = self.VAL_TARGETPOSE - self.VAL_POSE
        self.VAL_DYSTANS = kierunek.length()
        if self.VAL_DYSTANS > 30:
            kierunek.normalize_ip()
            ruch = kierunek * (5 * Core.VAL_SPPEDTIME) * dt
            self.VAL_POSE += ruch
            self.VAL_TRASAPRZEBYTA += ruch.length()
            self.rect.topleft = (round(self.VAL_POSE.x), round(self.VAL_POSE.y))
            self.BOOL_INMOVE = True
        else:
            self.BOOL_INMOVE = False

        - Obliczany jest wektor kierunku i dystans do celu.
        - Jeżeli jednostka znajduje się dalej niż 30 pikseli od celu:
        - Przemieszcza się w jego kierunku z prędkością zależną od Core.VAL_SPPEDTIME i dt.
        - Aktualizowana jest pozycja graficzna
        - Ustawiany jest znacznik ruchu BOOL_INMOVE.
        :param dt: Delta time
        """
        if self.VAL_HEALTH < 30:
            self.VAL_TARGETPOSE = pygame.Vector2(self.VAL_X,-1)
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
            ruch = kierunek * (5 * Core.VAL_SPPEDTIME) * dt
            self.VAL_POSE += ruch
            self.rect.topleft = (round(self.VAL_POSE.x), round(self.VAL_POSE.y))
            self.BOOL_Move = True
        else:
            self.BOOL_Move = False

        if not self.BOOL_Move:
            if self.VAL_HEALTH < 30:
                self.VAL_HEALTH = 100
    def DEF_DRAW(self):
        """
        Wyświetlenie  na ekranie obiektu
        """
        Core.screen.blit(self.image, self.rect)
    def GET_HEALTH(self):
        """
        :return: Zwrócenie ilości życia
        """
        return self.VAL_HEALTH
    def SET_HEALTH(self,val):
        """
        Ustawienie życia o parametr podany do metody

        :param val: liczba życia podana do metody
        """
        self.VAL_HEALTH = val