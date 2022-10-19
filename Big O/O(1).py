# La notacion O(1) indica una ejecucion constante
# que no depende del tamaño de las entradas, por ejemplo
# se va a demorar lo mismo en ejecutar el algoritmo con un
# arreglo de 2 elementos que un arreglo de 100000

import time

array_small = ['foo' for _ in range(10)]
array_medium = ['foo' for _ in range(9999)]
array_large = ['foo' for _ in range(999999)]

def find_foo(array):
    t0 = time.time()
    print("Foo was found") # O(1)
    # for i in array:
    #     pass
    t1 = time.time()
    print(f'Time taken = {t1-t0}')

find_foo(array_small)
find_foo(array_medium)
find_foo(array_large)