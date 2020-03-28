if __name__ == '__main__':
    # Inputing the number
    N = int(input())

    # Defining the recursive factorial fn
    def factorial(n):
        if n > 0:
            return n * int(factorial(n - 1))
        else:
            return 1

    # Printing
    print(factorial(N))
