class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

    def __repr__(self):
        return str(self.valeur)

class ListeChainee:
    def __init__(self):
        self.tete = None

    def estVide(self):
        return self.tete is None

    def taille(self):
        c = 0
        cur = self.tete
        while cur:
            c += 1
            cur = cur.suivant
        return c

    def inserer(self, valeur, k):
        n = Noeud(valeur)
        if k == 0 or not self.tete:
            n.suivant = self.tete
            self.tete = n
            return
        cur = self.tete
        for _ in range(k - 1):
            if not cur.suivant: break
            cur = cur.suivant
        n.suivant = cur.suivant
        cur.suivant = n

    def supprimer(self, k):
        if not self.tete: return
        if k == 0:
            self.tete = self.tete.suivant
            return
        cur = self.tete
        for _ in range(k - 1):
            if not cur.suivant: return
            cur = cur.suivant
        if cur.suivant:
            cur.suivant = cur.suivant.suivant

    def rechercher(self, valeur):
        i = 0
        cur = self.tete
        while cur:
            if cur.valeur == valeur: return i
            cur = cur.suivant
            i += 1
        return -1

    def obtenir(self, k):
        cur = self.tete
        for _ in range(k):
            if not cur: return None
            cur = cur.suivant
        return cur.valeur if cur else None

    def __repr__(self):
        res = ""
        cur = self.tete
        while cur:
            res += str(cur.valeur) + (" -> " if cur.suivant else "")
            cur = cur.suivant
        return res

print("--- EXERCICE 1 ---")
l = ListeChainee()
print("Est vide:", l.estVide())
l.inserer(10, 0)
l.inserer(20, 1)
l.inserer(15, 1)
print("Liste:", l)
print("Taille:", l.taille())
print("Recherche 15:", l.rechercher(15))
print("Obtenir index 1:", l.obtenir(1))
l.supprimer(1)
print("Apres suppression index 1:", l)

class Train(ListeChainee):
    def __init__(self, n):
        super().__init__()
        for i in range(n):
            self.inserer(0, i)

    def monter(self, k):
        t = self.taille()
        for i in range(k, t):
            if self._modifier(i, 1):
                print(self)
                return
        print("Train complet")

    def descendre(self, k):
        self._modifier(k, -1)
        print(self)

    def _modifier(self, k, diff):
        cur = self.tete
        for _ in range(k):
            if not cur: return False
            cur = cur.suivant
        if not cur: return False
        nv = cur.valeur + diff
        if 0 <= nv <= 4:
            cur.valeur = nv
            return True
        return False

print("\n--- TRAIN ---")
tr = Train(3)
print("Tr:", tr)
for _ in range(13): tr.monter(2)
tr.descendre(1)

class Pile:
    def __init__(self):
        self.tete = None

    def estVide(self):
        return self.tete is None

    def empiler(self, v):
        n = Noeud(v)
        n.suivant = self.tete
        self.tete = n

    def depiler(self):
        if not self.tete: return None
        v = self.tete.valeur
        self.tete = self.tete.suivant
        return v

    def sommet(self):
        return self.tete.valeur if self.tete else None

def analyse(s):
    p = Pile()
    ouv = "{<(["
    fer = "}>)]"
    cor = {"}": "{", ">": "<", ")": "(", "]": "["}
    for c in s:
        if c in ouv: p.empiler(c)
        elif c in fer:
            if p.estVide() or p.depiler() != cor[c]: return False
    return p.estVide()

print("\n--- EXERCICE 2 ---")
print("Analyse ({}):", analyse("{}"))
print("Analyse (({<}>)):", analyse("(({<}>))"))
print("Analyse (()[):", analyse("(()["))

