# Input the array
N = int(input())
s = str(input())
for i in range(0, N):
    list_array = s.split()

# Output as reverse
for j in range(N-1, -1, -1):
    print(list_array[j], end=" ")
