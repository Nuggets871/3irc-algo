


def tour_hanoin(n, depart, arrivee, intermediaire):
    if n==1:
        print("deplacer le disque du pilier ", depart, " vers le pilier ", arrivee)
    else:
        tour_hanoin(n-1, depart, intermediaire, arrivee)
        print("deplacer le disque du pilier ", depart, " vers le pilier", arrivee)
        tour_hanoin(n-1, intermediaire, arrivee, depart)

n = 3
tour_hanoin(n, '1', '2', '3')
