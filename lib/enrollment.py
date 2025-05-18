from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  
        self._grades = {}  

    def enroll(self, enrollment):
        self._enrollments.append(enrollment)

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:
            return 0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses
        return average_grade

class Course:
    def __init__(self, title):
        self.title = title
        self.enrollments = [] 

    def add_enrollment(self, enrollment):
        self.enrollments.append(enrollment)

class Enrollment:
    all = []  

    def __init__(self, student, course, enrollment_date=None):
        if enrollment_date is None:
            enrollment_date = datetime.now()
        self.student = student
        self.course = course
        self._enrollment_date = enrollment_date

       
        student.enroll(self)
        course.add_enrollment(self)

        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
