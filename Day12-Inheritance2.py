class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, first, last, id, scores):
        Person.__init__(self, first, last, id)
        self.scores = scores

    def calculate(self):
        sum = 0
        for i in range(int(len(self.scores))):
            sum += int(self.scores[i])
        sum = sum / int(len(self.scores))
        if 90 <= sum <= 100:
            return "O"
        elif 80 <= sum < 90:
            return "E"
        elif 70 <= sum < 80:
            return "A"
        elif 55 <= sum < 70:
            return "P"
        elif 40 <= sum < 50:
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
