from math import sqrt

T = int(input())
for i in range(T):
    n = int(input())
    c = 0
    for j in range(2, int(sqrt(n) + 1)):
        if n % j == 0:
            c = 1
            break

    if c == 0 and n >= 2:
        print("Prime")
    else:
        print("Not prime")
