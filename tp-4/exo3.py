
# question 1:

# Si on trie les deux premiers tiers d'un tableau, on place dans le premier tier les 'petits' nombre, puis les grand dans le deuxieme
# Si on trie les deux derniers tier ensuite, on va donc mettre les plus grande valeur de tout le tableau dans le dernier tier
# Si on retrie les deux premiers tier, alors là, on aura maintenant les plus petit nombre à gauche et le reste du tableau trié,
# ce qui donne un tableau complètement trié


def tri_par_tiers(L):
    if len(L)==0:
        return
    if len(L)==1:
        return L
    if len(L)==2:
        if L[1]>L[0]:
            return L
        else:
            return [L[1],L[0]]
    n=len(L)
    i=n//3
    j=n-i
    L[:j]=tri_par_tiers(L[:j])
    L[i:]=tri_par_tiers(L[i:])
    L[:j]=tri_par_tiers(L[:j])
    return L

L1 = [3,8,5]
L2 = [8,1,38,12,9,73,36,92,3]
L3 = [3,4,1,2]

print(tri_par_tiers(L3))



