# Input the number
N = int(input())
max1 = result = 0

# Counting consecutive 1 when converting the number to binary
while N > 0:
    if N % 2 == 1:
        result += 1
        if result > max1:
            max1 = result
    else:
        result = 0
    N = N//2

print(max1)