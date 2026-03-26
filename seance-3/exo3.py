
def max_liste_diviser_pour_regner(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        milieu = len(liste) // 2
        max_gauche = max_liste_diviser_pour_regner(liste[:milieu])
        max_droite = max_liste_diviser_pour_regner(liste[milieu:])
        return max(max_gauche, max_droite)

liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(max_liste_diviser_pour_regner(liste))