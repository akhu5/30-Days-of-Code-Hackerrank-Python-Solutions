if __name__ == '__main__':
    rows, col = (6, 6)
    max_sum = local_sum = -99
    arr1 = [[int(i) for i in input().split()] for j in range(rows)]
    for i1 in range(0, col-2):
        for j1 in range(0, rows-2):
            local_sum = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if i == 1 and j == 0:
                        continue
                    elif i == 1 and j == 2:
                        continue
                    else:
                        local_sum += arr1[i1+i][j+j1]
            if local_sum >= max_sum:
                max_sum = local_sum

print(max_sum)
