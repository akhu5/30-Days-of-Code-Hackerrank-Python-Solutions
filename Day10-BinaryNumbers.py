# Recursive Binary function
def decimal2binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + (10 * decimal2binary(int(n / 2)))

# Counts consecutive 1 digits in binary numbers
def consecutive1count(s):
    m = c = 0
    s = str(s)
    for i in range(0, int(len(s))):
        if int(s[i]) == 1:
            c += 1
            if c > m:
                m = c
        else:
            c = 0
    return m

# Input the number
N = int(input())
B = decimal2binary(N)
print(consecutive1count(B))
