# a=5
# b=6
# c=10
# for i in range(n):
#     for j in range(n):
#         x = i * i
#         y = j * j
#         z = i * j
# for k in range(n):
#     w = a*k + 45
#     v = b*b
# d = 33
#
#
#
#
# i = n
# while i > 0:
#     k = 2 + 2
#     i = i // 2

from math import sqrt

def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


import time
start_time = time.time() # Démarrage du chronomètre
prime(1000000007)
end_time = time.time() # Fin du chronomètre
print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")

numbers_to_test = [4337894221, 118922974492981, 7138449485398663, 35831403792388187, 621467444825020319, 8939187427700486623]
for number in numbers_to_test:
    start_time = time.time()
    result = prime(number)
    end_time = time.time()
    print(f"Number: {number}, Is Prime: {result}, Time: {end_time - start_time:.6f} seconds")






