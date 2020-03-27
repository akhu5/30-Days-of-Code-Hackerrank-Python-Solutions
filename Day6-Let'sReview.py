# Function definition
def even_odd_idx(string):
    # For printing even index characters
    for i in range(0, len(string)):
        if i % 2 == 0:
            print(string[i], end="")
    print(" ", end="")
    # For printing odd index characters
    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end="")


# Input number of TC
t = int(input())
for k in range(0, t):
    s = str(input())
    even_odd_idx(s)
    print("")
