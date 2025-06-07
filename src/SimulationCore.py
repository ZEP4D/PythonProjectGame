import Objectinthemap


LIST_INFANTRY = {}
LIST_ENEMY = {}
Front = Objectinthemap.FrontLine()
FrontE = Objectinthemap.FrontLine()
def DEF_PREWHILE():
    """
    Odpowiada za wczytanie obiektów przed wejściem do głównej pętli gry


    """

    
    LIST_INFANTRY["1"] = Objectinthemap.Infantry(699, 700, "1", Front)
    LIST_INFANTRY["2"] = Objectinthemap.Infantry(800, 700, "2", Front)
    LIST_INFANTRY["3"] = Objectinthemap.Infantry(400, 700, "3", Front)
    LIST_INFANTRY["4"] = Objectinthemap.Infantry(400, 700, "4", Front)


    LIST_ENEMY["1"] = Objectinthemap.ENEMY(500, -300, FrontE)
    LIST_ENEMY["2"] = Objectinthemap.ENEMY(746, -300, FrontE)
    LIST_ENEMY["3"] = Objectinthemap.ENEMY(914, -300, FrontE)
    LIST_ENEMY["4"] = Objectinthemap.ENEMY(1182, -300, FrontE)
def DEF_INWHILE(dt,ticket):
    """
    Odpowiada za obsługę obiektów w czasie trwania pętli gry

    :param dt: Delta czas
    :param ticket: To przekazuje aktualny ticket w grze

    """


    for i in LIST_INFANTRY.values():
        i.DEF_UPDATE(dt, LIST_ENEMY)
        i.DEF_UPDATE_RES(dt)
        i.DEF_BATTLE(ticket,LIST_ENEMY)
        i.DEF_DRAW()
    for i in LIST_ENEMY:
        LIST_ENEMY[i].DEF_UPDATE(dt)
        LIST_ENEMY[i].DEF_DRAW()



