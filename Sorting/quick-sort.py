import timeit

start = timeit.default_timer()
def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

def quick_sort(a, p , r):
    if p<r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


a = [5, 4, 3, 2, 1]
p = 0
r = len(a) - 1
quick_sort(a, p, r)
print(a)
stop = timeit.default_timer()
execution_time = stop-start

print(f"code executed in {execution_time}")