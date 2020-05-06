#!/bin/python3

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        m = 0
        var = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                var = i & j
                if m < var < k:
                    m = var
        print(m)