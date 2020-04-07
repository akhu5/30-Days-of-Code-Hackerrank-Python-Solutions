s = str(input())
try:
    print(int(s))
except ValueError:
    print("Bad String")