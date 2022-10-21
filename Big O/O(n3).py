import time

array_small = ['foo' for _ in range(10)]

print(array_small)

array_medium = ['foo' for _ in range(9999)]
array_large = ['foo' for _ in range(999999)]

def find_foo(array):
    t0 = time.time()
    
    for _ in array:  
        print("Foo was found")
        for _ in array: 
            print("Foo was found") 
            for _ in array: 
                print("Foo was found") 

    t1 = time.time()
    print(f'Time taken = {t1-t0}')

# find_foo(array_small)
# find_foo(array_medium)
# find_foo(array_large)