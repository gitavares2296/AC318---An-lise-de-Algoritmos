from algorithms import insertion_sort, bubble_sort, selection_sort, merge_sort, quick_sort, heap_sort

from random import randint
import time


def get_random_list(quantity: int):
    random_list = []
    while len(random_list) != quantity:
        r = randint(0, 10000)
        if r not in random_list:
            random_list.append(r)
    return random_list


class ExecutionBase:
    def execute_sort(self):
        max_vet = 10
        for i in range(3):  # change to 5
            vet_sum = 0
            for j in range(10):
                random_list = get_random_list(max_vet)
                diff = self.call_sort_method(random_list, max_vet, j)
                vet_sum = vet_sum + diff
            print('average: {}'.format(vet_sum / 10))
            max_vet = max_vet * 10

    def call_sort_method(self, random_list, max_vet, j):
        print('call method')
        return 10


class InsertionSort(ExecutionBase):
    def call_sort_method(self, random_list, max_vet, j):
        begin = time.time()
        insertion_sort(random_list)
        end = time.time()
        print('insertion sort with {} items vet[{}]: {} seconds'.format(max_vet, j + 1, end - begin))
        return end - begin


class BubbleSort(ExecutionBase):
    def call_sort_method(self, random_list, max_vet, j):
        begin = time.time()
        bubble_sort(random_list)
        end = time.time()
        print('bubble sort with {} items vet[{}]: {} seconds'.format(max_vet, j + 1, end - begin))
        return end - begin


class SelectionSort(ExecutionBase):
    def call_sort_method(self, random_list, max_vet, j):
        begin = time.time()
        selection_sort(random_list)
        end = time.time()
        print('selection sort with {} items vet[{}]: {} seconds'.format(max_vet, j + 1, end - begin))
        return end - begin


class MergeSort(ExecutionBase):
    def call_sort_method(self, random_list, max_vet, j):
        begin = time.time()
        merge_sort(random_list)
        end = time.time()
        print('merge sort with {} items vet[{}]: {} seconds'.format(max_vet, j + 1, end - begin))
        return end - begin


class QuickSort(ExecutionBase):
    def call_sort_method(self, random_list, max_vet, j):
        begin = time.time()
        quick_sort(random_list)
        end = time.time()
        print('quick sort with {} items vet[{}]: {} seconds'.format(max_vet, j + 1, end - begin))
        return end - begin


class HeapSort(ExecutionBase):
    def call_sort_method(self, random_list, max_vet, j):
        begin = time.time()
        heap_sort(random_list)
        end = time.time()
        print('heap sort with {} items vet[{}]: {} seconds'.format(max_vet, j + 1, end - begin))
        return end - begin


if __name__ == '__main__':
    InsertionSort().execute_sort()
    print('-------------------------------------------------')
    BubbleSort().execute_sort()
    print('-------------------------------------------------')
    SelectionSort().execute_sort()
    print('-------------------------------------------------')
    MergeSort().execute_sort()
    print('-------------------------------------------------')
    QuickSort().execute_sort()
    print('-------------------------------------------------')
    HeapSort().execute_sort()
