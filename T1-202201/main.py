from bebestibles import Jugo, Gaseosa, Brebaje_magico
from casino import Casino
from juegos import Juego
from menus import Compra_bebestible, Estado_jugador, Menu_inicio, Menu_principal, MenusDic, Opciones_juego, Opciones_jugador

def bebidas(file):
    b = []
    mifile = open(file).readlines()
    for i in range(1, len(mifile)):
        o = mifile[i].split(",")
        if o[1] == "Jugo":
            b.append(Jugo(o[0], o[1], int(o[2].rstrip()) ))
        elif o[1] == "Gaseosa":
            b.append(Gaseosa(o[0], o[1], int(o[2].rstrip()) ))
        else:
            b.append(Brebaje_magico(o[0], o[1], int(o[2].rstrip()) ))
    
    return b


def juegos(file):
    j = {}
    mifile = open(file).readlines()
    for i in range(1, len(mifile)):
        o = mifile[i].split(",")
        j[o[0]] = Juego(o[0], int(o[1]), int(o[2]), int(o[3]))
    return j




if __name__ == "__main__":
    
    brebajes = bebidas("bebestibles.csv")
    games = juegos("juegos.csv")

    micasino = Casino(games, brebajes)
    
    menus = MenusDic()

    menus["inicio"] = Menu_inicio(micasino)
    menus["Principal"] = Menu_principal(micasino)
    menus["opciones"] = Opciones_jugador(micasino)
    menus["juegos"] = Opciones_juego(micasino)
    menus["Bebestibles"] = Compra_bebestible(micasino)
    menus["Estado Jugador"] = Estado_jugador(micasino)

    while True:
        menus.cambio()