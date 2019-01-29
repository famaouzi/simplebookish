### Fama Uzi
### 29/01/2019
### Program to create and edit book

from data.atitle import atitle

def empty_check():
	"""A function to check if input is empty"""
	entry = input().strip()
	if entry == '':
		return '-'
	else:
		return entry

def not_empty_check():
	"""A function to make sure the input is not empty"""
	while True:
		entry = input().strip()
		if entry == '':
			print("This entry must not be empty, try again: ")
		else:
			return entry
			break

def int_check():
	"""A loop function to check whether it is a positive integer or not"""
	while True:
		entry = empty_check()
		if entry != '-':
			try:
				check = int(entry)
				if check > 0:
					return entry
					break
				else:
					print("Not accepting ancient books, please enter a positive integer: ")
			except ValueError:
				print("Not an integer, please enter an integer number: ")
		else:
			return entry
			break

def new_book(name, author, genre, publisher, published_year):
	"""A function to create a new book as dictionary."""
	book = {'Name': name, 'Author': author, 'Genre': genre, 'Publisher': publisher, 'Year': published_year}
	return book

def create_book():
	"""Collecting information for the book and then create it."""
	print("Enter the name of the book: ")
	entry = not_empty_check()
	name = atitle(entry)
	print("Enter the author of " + name + ": ")
	entry = empty_check()
	author = atitle(entry)
	print("Enter the genre of " + name + ": ")
	entry = empty_check()
	genre = atitle(entry)
	print("Enter the publisher of " + name + ": ")
	entry = empty_check()
	publisher = atitle(entry)
	print("Enter the year of publishing of " + name + ": ")
	entry = int_check()
	published_year = atitle(entry)

	book = new_book(name, author, genre, publisher, published_year)
	return book

def edit_book(book):
	"""A function to edit a book"""
	print("\nEditing " + book.get('Name') + ": (To skip, leave it empty and enter)\n")
	for key, value in book.items():
		print(value)
		entry = input("is changed to: ")
		if entry == '':
			pass
		else:
			book[key] = atitle(entry)

	return book