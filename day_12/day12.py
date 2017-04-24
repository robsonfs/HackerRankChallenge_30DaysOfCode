class Person(object):
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here


    def calculate(self):
        grade = "O"
        average = self.__average()
        if average < 40:
            grade = "T"
        elif average < 55:
            grade = "D"
        elif average < 70:
            grade = "P"
        elif average < 80:
            grade = "A"
        elif average < 90:
            grade = 'E'

        return grade

    def __average(self):
        return sum(self.scores)/len(self.scores)
