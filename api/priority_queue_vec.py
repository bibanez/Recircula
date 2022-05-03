from re import L
from typing import List


def swap(v: List, i: int, j: int):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux


def comp(v1: List, v2: List):
    return v1[-1] < v2[-1]


class Priority_queue:

    def __init__(self, initial_k: List) -> None:
        self._heap = []
        self._build_heap(initial_k, len(initial_k))
        self._size = len(initial_k)

    def size(self):
        return self._size

    def insert(self, v):
        self._size += 1
        self._heap.append(v)
        self._bubble_up(self._size-1)

    def _build_heap(self, initial_k: List, k: int):
        self._heap = [None]
        for i in range(len(initial_k)):
            self._heap.append(initial_k[i])
        for j in range(k//2, 0, -1):
            self._bubble_down(j)

    def _bubble_down(self, i: int):
        ind = i
        work = True
        while 2*ind+1 < len(self._heap) and work:
            if comp(self._heap[2*ind], self._heap[2*ind+1]):
                if comp(self._heap[2*ind], self._heap[ind]):
                    swap(self._heap, ind, 2*ind)
                    ind *= 2
                else:
                    work = False
            else:
                if comp(self._heap[2*ind+1], self._heap[ind]):
                    swap(self._heap, ind, 2*ind+1)
                    ind = 2*ind+1
                else:
                    work = False
        if 2*ind < len(self._heap) and comp(self._heap[2*ind], self._heap[ind]):
            swap(self._heap, ind, 2*ind)

    def _bubble_up(self, i: int):
        work = True
        ind = i
        while (work == True):
            work = comp(self._heap[ind], self._heap[ind//2])
            if work:
                swap(self._heap, ind//2, ind)
                ind = i//2
            if ind == 0:
                work = False

    def remove_min(self):  # or remove_min according to comp
        aux = self._heap[self._size]
        self._heap.pop()
        min_e = self._heap[1]
        self._heap[1] = aux
        self._bubble_down(1)
        self._size -= 1
        return min_e

    def queue_to_list(self):
        l = []
        for i in range(1, len(self._heap)):
            l.append(self._heap[i][:len(self._heap[i])])
        return l
