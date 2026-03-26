

def decroissantRecursive(n):
    if n<=1:
        print(n)
    else:
        print(n)
        decroissantRecursive(n-1)


def croissantRecursive(n):
    if n<1:
        return
    else:
        croissantRecursive(n-1)
        print(n)



#decroissantRecursive(10)
croissantRecursive(10)