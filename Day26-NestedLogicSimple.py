return_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))
fine = 0

if return_date[2] > due_date[2]:
    fine = 10000
else:
    if return_date[1] < due_date[1]:
        fine = 0
    elif return_date[1] > due_date[1]:
        if return_date[2] == due_date[2]:
            fine = 500 * (return_date[1] - due_date[1])
        else:
            fine = 0
    else:
        if return_date[2] == due_date[2]:
            if return_date[0] > due_date[0]:
                fine = 15 * (return_date[0]-due_date[0])
            else:
                fine = 0
        else:
            fine = 0


print(fine)

#Shorter, but same logic:

# return_date = list(map(int, input().split()))
# due_date = list(map(int, input().split()))
# fine = 0
#
# if return_date[2] > due_date[2]:
#     fine = 10000
# elif return_date[2] == due_date[2]:
#     if return_date[1] == due_date[1]:
#         fine = 15 * (return_date[0] - due_date[0])
#     elif return_date[1] > due_date[1]:
#         fine = 500 * (return_date[1]-due_date[1])
#
# print(fine)
