class Student:
	"""docstring for Student"""
	def __init__(self,student_id,name):
		self.student_id = student_id
		self.name=name
		self.courses=[]

	def enroll(self,courses):
		if course not in self.courses:
			self.courses.append(course)
			print(f"{self.name} enrolled in {course}")
		else:
			print("Already enrolled")

class StudentManager:
	def __init__(self):
		self.students={}

	def add_student(self,student_id,name):
		if student_id not in self.students:
			self.students[student_id]=Student(student_id,name)
			print("Studnet Added")
		else:
			print("Studnet ID Already exists")

	def remove_student(self,student_id):
		if student_id in self.students:
			

			
		