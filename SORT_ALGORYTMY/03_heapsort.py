def max_heapify(T, heap_size, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < heap_size and T[l] > T[i]:
        largest = l
    if r < heap_size and T[r] > T[largest]:
        largest = r
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        max_heapify(T, heap_size, largest)


def build_max_heap(T, heap_size):
    for i in range(len(T)//2, -1, -1):
        max_heapify(T, heap_size, i)


def heapsort(T):
    heap_size = len(T)
    build_max_heap(T, heap_size)
    for i in range(len(T)-1, -1, -1):
        T[0], T[i] = T[i], T[0]
        heap_size -= 1
        max_heapify(T, heap_size, 0)

#==================================================

def heapify(T, heap_size, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < heap_size and T[i] < T[l]:
        largest = l
    if r < heap_size and T[largest] < T[r]:
        largest = r
    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, heap_size, largest)


def heapsort_b(T):
    heap_size = len(T)
    for i in range(heap_size//2, -1, -1):
        heapify(T, heap_size, i)
    for j in range(heap_size-1, 0, -1):
        T[j], T[0] = T[0], T[j]
        heapify(T, j, 0)