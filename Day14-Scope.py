class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        maxDiff = 0
        for i in range(0, int(len(self.__elements))):
            for j in range(i, int(len(self.__elements))):
                compare = abs(self.__elements[i] - self.__elements[j])
                if compare > maxDiff:
                    maxDiff = compare
        self.maximumDifference = maxDiff


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
