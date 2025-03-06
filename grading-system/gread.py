
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = {}
    
class Course:
    def __init__(self, course_code):
        self.course_code = course_code
        self.students = []

class GradingSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student_id, course_code,grade):
        if student_id in self.students and course_code in self.courses:
            self.students[student_id].grades[course_code] = grade
            print("Grade added successfully")
        else:
            print("Student or course not found")
    def calulate_avarage(self, student_id):
        if student_id in self.students:
            grades = self.students[student_id].grades.values()
            return sum(grades)/len(grades) if grades else 0
        return 0
    
def grading_main():
    system = GradingSystem()
    system.students["1"] = Student("1", "Alice",{})
    system.students["2"] = Student("2", "Bob",{})
    system.courses["101"] = Course("101")
    system.courses["102"] = Course("102")
   

    while True:
        print("\n1. add grade \n2. calculate average \n3. exit")
        choice = input("Enter your choice: ")
        if choice=='3':
            break
        elif choice=='1':
            student_id = input("Enter student id: ")
            course_code = input("Enter course code: ")
            grade = float(input("Enter grade: "))
            system.add_grade(student_id, course_code, grade)
        elif choice=='2':
            student_id = input("Enter student id: ")
            avg= system.calculate_average(student_id)
            print(f"Average: {avg:.2f}")
        else:
            print("Invalid choice") 
grading_main()



   