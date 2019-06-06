def insertion_sort(vet):
    for i in range(1, len(vet)):
        key = vet[i]
        j = i - 1
        while j >= 0 and key < vet[j]:
            vet[j + 1] = vet[j]
            j -= 1
        vet[j + 1] = key


def bubble_sort(vet):
    n = len(vet)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vet[j] > vet[j + 1]:
                vet[j], vet[j + 1] = vet[j + 1], vet[j]


def selection_sort(vet):
    for i in range(len(vet)):
        min_index = i
        for j in range(i + 1, len(vet)):
            if vet[min_index] > vet[j]:
                min_index = j
        vet[i], vet[min_index] = vet[min_index], vet[i]


def merge_sort(vet):
    if len(vet) > 1:
        mid = len(vet) // 2
        left_half = vet[:mid]
        right_half = vet[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vet[k] = left_half[i]
                i = i + 1
            else:
                vet[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            vet[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            vet[k] = right_half[j]
            j = j + 1
            k = k + 1


def quick_sort(vet):
    less = []
    equal = []
    greater = []

    if len(vet) > 1:
        pivot = vet[0]
        for x in vet:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return vet


def heap_sort(vet):
    build_max_heap(vet)
    for i in range(len(vet) - 1, 0, -1):
        vet[0], vet[i] = vet[i], vet[0]
        max_heapify(vet, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(vet):
    length = len(vet)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(vet, index=start, size=length)
        start = start - 1


def max_heapify(vet, index, size):
    l = left(index)
    r = right(index)
    if l < size and vet[l] > vet[index]:
        largest = l
    else:
        largest = index
    if r < size and vet[r] > vet[largest]:
        largest = r
    if largest != index:
        vet[largest], vet[index] = vet[index], vet[largest]
        max_heapify(vet, largest, size)
