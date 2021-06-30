import timeit

def max_heapify(a, i):
    l = 2*i
    r = 2*i + 1
    
    n = len(a)

    if l < n and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < len(a) and a[r] > a[largest]:
        largest = r
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)

def build_max_heap(a):
    n = len(a)
    for i in range(n//2, -1, -1):
        max_heapify(a, i)
                                                                                                                                                                                                                                                


def extract_max(a):
    n = len(a)-1
    if len(a) < 1:
        print("heap underflow")
    else:
        max = a[0]
        a[0], a[n] = a[n], a[0]
        del a[n-1]
        max_heapify(a, 0)
    return max

def heap_sort(a):
    build_max_heap(a)
    n = len(a)
    for i in range(len(a)):
        print(a[0])
        a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
        del a[len(a)-1]
        max_heapify(a, 0)

start = timeit.default_timer()
a = [ x for x in range(10000) ]

# build_max_heap(a)
# print(a)
heap_sort(a)
stop = timeit.default_timer()

print(f"the code executed in {stop-start} time")