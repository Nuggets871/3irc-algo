import time

fibo = [5,10,20,30,40]

def fibonaci1(n):
    if n<=2:
        return n
    return fibonaci1(n-1)+fibonaci1(n-2)

# for x in fibo:
#     temps_debut=time.time()
#     print("fibo de ",  x ,  " = ",  fibonaci1(x))
#     print("temps passé: ",  time.time()-temps_debut)



def fibo2(n, F):
    if F[n] != -1:
        return F[n]
    if n<2:
        F[n]=1
        return 1
    r=fibo2(n-1,F)+fibo2(n-2,F)
    F[n]=r
    return r

# print(fibo2(4,[-1]*5))

def fibo3_recursion_terminal(n, a=1, b=1):
    if n<=2:
        return a
    return fibo3_recursion_terminal(n-1, b, a+b)

# for x in fibo:
#     temps_debut=time.time()
#     print("fibo de ",  x ,  " = ",  fibo3_recursion_terminal(x))
#     print("temps passé: ",  time.time()-temps_debut)