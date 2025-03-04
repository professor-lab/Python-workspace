class Question:
	"""docstring for Question"""
	def __init__(self,text,answer):
		self.text = text
		self.answer=answer

	def check_answer(self,user_answer):
		return user_answer.lower()==self.answer.lower()

class MultipleChoiceQuestion(Question):
	def __init__(self,text,options,answer):
		super().__init__(text,answer)
		self.options=options

	def display(self):
		print(self.text)
		for idx,option in enumerate(self.options,1):
			print(f"{idx}.{option}")
class Quiz:
	def __init__(self):
		self.questions=[]

	def add_question(self,question):
		self.questions.append(question)

def take_quiz(quiz):
	score=0
	for q in quiz.questions:
		if isinstance(q,MultipleChoiceQuestion):
			q.display()
			user_ans=input("Enter Option Number:")
			correct_ans=q.options[int(user_ans)-1]
		else:
			print(q.text)
			user_ans=input("Answer:")
		if q.check_answer(user_ans if not isinstance(q,MultipleChoiceQuestion) else correct_ans):
			score+=1
	print(f"Score:{score}/{len(quiz.questions)}")

quiz=Quiz()
quiz.add_question(Question("Python Is dynamically type","True"))
quiz.add_question(MultipleChoiceQuestion("2+2 ?",["2","3","4","5"],"4"))

take_quiz(quiz)


		