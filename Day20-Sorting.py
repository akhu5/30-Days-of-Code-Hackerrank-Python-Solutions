n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def bubbleSort(n, a):
    numswaps = 0
    for i in range(0, n):
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                numswaps += 1
                swap(a[j], a[j+1], j)
    print("Array is sorted in", numswaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])


def swap(v1, v2, j):
    t = v2
    a[j+1] = v1
    a[j] = t

bubbleSort(n, a)