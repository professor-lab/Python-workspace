class Book:
	"""docstring for Book"""
	def __init__(self,title,author,isbn):
		self.title=title
		self.author=author
		self.isbn=isbn
		self.available=True

class Library:
	def __init__(self):
		self.books=[]

	def add_book(self,book):
		self.books.append(book)
		print(f"Added '{book.title}'")
	
	def remove_book(self,isbn):
		for book in self.books:
			if book.isbn==isbn:
				self.books.remove(book)
				print(f"remove '{book.title}'")
				return
		print("book not found")

class User:
	"""docstring for User"""
	def __init__(self,name):
		self.name=name
		self.borroed_books=[]

def library_main():
	lib=Library()
	while True:
		print("\n1.Add Book \n2.Remove Book \n3.exit")
		choice=input("enter choice : ")
		if choice=='1':
			title=input("title : ")
			author=input("author : ")
			isbn=input("ISBN :")
			lib.add_book(Book(title,author,isbn))
		elif choice=='2':
			isbn=input("ISBN To remove :")
			lib.remove_book(isbn)
		elif choice=='3':
			break
		else:
			print("invalid choice")

library_main()
		
		
		