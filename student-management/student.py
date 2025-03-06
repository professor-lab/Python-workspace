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
			del self.students[student_id]
			print("Student Remove")
		else:
			print("Student Not Found")

def student_main():
	manager=StudentManager()
	while True:
		print("\n1. Add Student \n2. Remove Student \n3. enroll in courses \n4. Exit")
		choice=input("Enter Choice")
		if choice=='4':
			break
		elif choice=='1':
			student_id=input("Student ID: ")
			name=input("name: ")
			manager.add_student(student_id,name)
		elif choice=='2':
			student_id=input("Student ID remove:")
			manager.remove_student(student_id)
		elif choice=='3':
			student_id=input("Student ID:")
			course=input("Course:")
			if student_id in manager.students:
				manager.students[student_id].enroll(course)
			else:
				print("Student Not Found")
		else:
			print("invalid choice")

student_main()


			
		