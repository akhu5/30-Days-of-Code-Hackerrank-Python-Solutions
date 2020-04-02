if __name__ == '__main__':
    rows, col = (6, 6)
    max_sum = hourglass_sum = -99
    array = [[int(i) for i in input().split()] for j in range(rows)]
    for columns_outer in range(0, col - 2):
        for rows_outer in range(0, rows - 2):
            hourglass_sum = 0
            for columns_inner in range(0, 3):
                for rows_inner in range(0, 3):
                    if columns_inner == 1 and rows_inner == 0:
                        continue
                    elif columns_inner == 1 and rows_inner == 2:
                        continue
                    else:
                        hourglass_sum += array[columns_outer + columns_inner][rows_inner + rows_outer]
            if hourglass_sum >= max_sum:
                max_sum = hourglass_sum

print(max_sum)
