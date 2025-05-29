import Core
import Objectinthemap


LIST_INFANTRY = { }
Front = Objectinthemap.FrontLine()
def DEF_PREWHILE():


    
    LIST_INFANTRY["1"] = Objectinthemap.Infantry(699,700, "1",Front)
    LIST_INFANTRY["2"] = Objectinthemap.Infantry(800, 700, "2",Front)
    LIST_INFANTRY["3"] = Objectinthemap.Infantry(400, 700, "3",Front)
    LIST_INFANTRY["4"] = Objectinthemap.Infantry(400, 700, "4", Front)
    LIST_INFANTRY["5"] = Objectinthemap.Infantry(400, 700, "5", Front)

def DEF_INWHILE(dt):

    for i in LIST_INFANTRY:
        LIST_INFANTRY[i].DEF_UPDATE(dt)
        LIST_INFANTRY[i].DEF_UPDATE_RES(dt)
        LIST_INFANTRY[i].DEF_DRAW()



