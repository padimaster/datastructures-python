# La notacion O(n) indica que un algoritmo se va a ejecutar
# en el peor de los casos, "n" veces

import time

array_small = ['foo' for _ in range(10)]
array_medium = ['foo' for _ in range(9999)]
array_large = ['foo' for _ in range(999999)]

def find_foo(array):
    t0 = time.time()
    
    for _ in array:  # O(n)
        print("Foo was found") # O(1)

    t1 = time.time()
    print(f'Time taken = {t1-t0}')

find_foo(array_small)
find_foo(array_medium)
find_foo(array_large)