class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, l):
        Person.__init__(self, l[0], l[1], l[2])

    def calculate(self, c, m):
        sum = 0
        for i in range(int(len(m))):
            sum += int(m[i])
        sum = sum/c
        if 90 <= sum <= 100:
            print("Grade: O")
        elif 80 <= sum < 90:
            print("Grade: E")
        elif 70 <= sum < 80:
            print("Grade: A")
        elif 55 <= sum < 70:
            print("Grade: P")
        elif 40 <= sum < 5:
            print("Grade: D")
        else:
            print("Grade: T")


akhil = Student(input().split())
count = int(input())
marks = list(input().split())
akhil.printPerson()
akhil.calculate(count, marks)
