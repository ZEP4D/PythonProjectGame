import Core
import Objectinthemap

LIST_INFANTRY = { }
def DEF_PREWHILE():



    LIST_INFANTRY["1"] = Objectinthemap.Infantry(699,700, "1")
    LIST_INFANTRY["2"] = Objectinthemap.Infantry(400, 700, "2")

def DEF_INWHILE(dt):

    for i in LIST_INFANTRY:
        LIST_INFANTRY[i].DEF_UPDATE(dt)
        LIST_INFANTRY[i].DEF_DRAW()



