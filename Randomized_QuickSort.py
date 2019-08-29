import numpy as np
from  random import choice


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            t = A[i]
            A[i] = A[j]
            A[j] = t

    t2 = A[i+1]
    A[i+1] = A[r]
    A[r] = t2

    return i + 1


def randomized_partition(A, p, r):
    l = list(range(p, r+1))
    i = choice(l)

    t3 = A[i]
    A[i] = A[r]
    A[r] = t3

    return partition(A, p, r)


def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)


if __name__ == '__main__':
    A_size = 16
    A = list(np.random.randint(-100, 100, size=A_size))
    print('Unsorted list:', A)

    randomized_quicksort(A, 0, len(A)-1)
    print('\nSorted list:', A)