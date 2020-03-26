if __name__ == '__main__':
    # Input from user
    N = int(input())

    # If odd
    if N % 2 == 1:
        print("Weird")

    # If even and between 2 and 5 (both included)
    if N % 2 == 0 and 2 <= N <= 5:
        print("Not Weird")

    # If even and between 6 and 20 (both included)
    if N % 2 == 0 and 6 <= N <= 20:
        print("Weird")

    # If even and greater than 20
    if N % 2 == 0 and N > 20:
        print("Not Weird")
