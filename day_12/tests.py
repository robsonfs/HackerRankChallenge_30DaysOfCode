from unittest import TestCase, mock
from day12 import Person, Student

class TestDay12(TestCase):

    def test_student_a_person_subclass(self):
        self.assertTrue(issubclass(Student, Person))

    def test_student_has_att_scores(self):
        student = Student("Sophia", "Fernandes", 201302, [90, 100, 100, 80])
        self.assertTrue(hasattr(student, 'scores'))

    def test_student_calculate_testcase0(self):
        student = Student("Sophia", "Fernandes", 201302, [90, 100, 100, 80])
        grade = student.calculate()
        self.assertEqual('O', grade)

    def test_student_calculate_testcase1(self):
        student = Student("Sophia", "Fernandes", 201302, [90, 80, 99, 80])
        grade = student.calculate()
        self.assertEqual('E', grade)

    def test_student_calculate_testcase2(self):
        student = Student("Sophia", "Fernandes", 201302, [76])
        grade = student.calculate()
        self.assertEqual('A', grade)

    def test_student_calculate_testcase3(self):
        student = Student("Sophia", "Fernandes", 201302, [66])
        grade = student.calculate()
        self.assertEqual('P', grade)

    def test_student_calculate_testcase4(self):
        student = Student("Sophia", "Fernandes", 201302, [54])
        grade = student.calculate()
        self.assertEqual('D', grade)

    def test_student_calculate_testcase5(self):
        student = Student("Sophia", "Fernandes", 201302, [39])
        grade = student.calculate()
        self.assertEqual('T', grade)
