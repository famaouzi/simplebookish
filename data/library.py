### Fama Uzi
### 29/01/2019
### Manage a library: a saved users' collections

# os is used to check, add, and remove file
import os

# For changing string of dictionary to the actual dictionary
from ast import literal_eval

from data.bookcreation import edit_book


class Library():
	"""A class to manage user file for their books collection"""

	def __init__(self, username, library = 'library'):
		"""Initialize the name of the collection"""
		
		# The collections is stored in the library folder
		# library = 'library' is default folder
		
		# Make the library folder if it doesn't exist
		if not os.path.exists(library):
			os.makedirs(library)

		# Create a collection using username file
		self.filename = username + '.txt'
		self.fullname = os.path.join(library, self.filename)

		# Initial error check
		self.init_error = 0

		# If the username.txt doesn't exist, create one
		if not os.path.exists(self.fullname):
			try:
				with open(self.fullname, 'w'):
					# Empty list
					self.book_list = []
					print("A new user " + username + " has been created.")
			except OSError:
				self.init_error = 'OSError'
				print("\nThe username can't contain any of the following characters:")
				print('\\ / : * ? " < > |\n')
		else:
			# Read the file to be accessed by the program as list of dictionaries
			with open(self.fullname, 'r') as file_object:
				lines = file_object.read().splitlines()
				try: 
					self.book_list = [literal_eval(line) for line in lines]
				except SyntaxError:
					self.init_error = 'SyntaxError'
					print("\nSyntaxError while reading the file, make sure the contents of " + self.fullname + " is a list of dictionaries.\n")
				except:
					self.init_error = 1
					print("\nUnexpected error while reading the file, make sure the contents of " + self.fullname + " is a list of dictionaries.\n")
				if self.init_error == 0:
					print("Welcome back, " + username + ".")

	def delete_file(self):
		"""Deletes user file"""
		if os.path.exists(self.fullname):
			os.remove(self.fullname)
			print(self.filename + " has been deleted.")
		else:
			print("The file does not exist.")

	def save_as_file(self, username, library = 'library'):
		"""Save the current book_list as another username, can be stored in another folder; using return to check whether the username is changed or not"""

		# Make the library folder if it doesn't exist
		if not os.path.exists(library):
			os.makedirs(library)

		# Check whether it exists or not
		check_filename = username + '.txt'
		check_fullname = os.path.join(library, check_filename)
		if not os.path.exists(check_fullname):
			# Using w+' to create and write if it doesn't exist
			self.filename = check_filename
			self.fullname = check_fullname
			try:
				with open(self.fullname, 'w+') as file_object:
					for book in self.book_list:
						file_object.write(str(book) + '\n')
					print("The collection has been saved as " + self.filename + "!") 
			except OSError:
				self.init_error = 'OSError'
				print("\nThe username can't contain any of the following characters:")
				print('\\ / : * ? " < > |\n')
			return 1
		else:
			overwrite_option = input('\n' + check_filename + " exists, overwrite? Enter 'y' or 'yes' to overwrite, otherwise return to main menu... ")
			if overwrite_option == 'y' or overwrite_option == 'yes':
				self.filename = check_filename
				self.fullname = check_fullname
				try:
					with open(self.fullname, 'w') as file_object:
						for book in self.book_list:
							file_object.write(str(book) + '\n')
						print("The collection has been saved as " + self.filename + "!")
				except OSError:
					self.init_error = 'OSError'
					print("\nThe username can't contain any of the following characters:")
					print('\\ / : * ? " < > |\n')
				return 1
			else:
				return 0

	def change_username(self, username, library = 'library'):
		"""Changing username by saving as and deleting previous name; using return to check whether the username is changed or not"""
		current_fullname = self.fullname
		is_saved = self.save_as_file(username, library)
		if is_saved == 1:
			os.remove(current_fullname)
			return 1
		else:
			return 0

	def sort_list(self, sortby):
		"""Sorting list by key"""
		self.book_list = sorted(self.book_list, key = lambda by: by[sortby])

	def find_bookindex(self, key_find):
		"""Finding the indexes of the book in the collection"""
		find = input("Type search query you want to find: ")
		indexes = []
		for book in self.book_list:
			# Search indexes which have 'find' key
			for key_value in book.values():
				if find.lower() in key_value.lower():
					indexes.append(self.book_list.index(book))
		if not indexes:
			print("\nThe book you search for with '" + find + "' can't be found!")
		return indexes

	def add_book(self, book):
		"""Add a book to the collection (auto-sorted)"""
		self.book_list.append(book)
		# with open(self.fullname, 'a') as file_object:
		# 	file_object.write(str(book) + '\n')
		# 	print(book['Name'] + " has been added to the collection.")

		# Changed from file append to file write for auto-sort by name
		self.sort_list('Name')
		with open(self.fullname, 'w') as file_object:
			for the_book in self.book_list:
				file_object.write(str(the_book) + '\n')
			print(book.get('Name') + " has been added/edited to the collection.")

	def remove_book(self, indexes):
		"""Remove books from the collection"""
		# Reversed because the list length will be reduced after an element is deleted
		indexes.sort(reverse=True)
		for index in indexes:
			book = self.book_list[index]
			print('\n'+ book.get('Name') + " has been removed/edited from the collection.")
			del self.book_list[index]
		with open(self.fullname, 'w') as file_object:
			for book in self.book_list:
				file_object.write(str(book) + '\n')

	def show_list(self, sortby = 'Name'):
		"""Print the collection of books, sort by name is default"""
		self.sort_list(sortby)
		if not self.book_list:
			print("Your collection is empty.")
		else:
			printed = '|||'.join(self.book_list[0].keys())
			print('No. ' + printed)
			print()
			i = 0
			for book in self.book_list:
				i += 1
				printed = '|||'.join(book.values())
				print(str(i) + '. ' + printed)

	def show_books(self, indexes):
		"""Print found books by find_bookindex function"""
		if indexes:
			printed = '|||'.join(self.book_list[0].keys())
			print('\nNo. ' + printed)
			print()
			for i in indexes:
				book = self.book_list[i]
				printed = '|||'.join(book.values())
				print(str(i + 1) + '. ' + printed)

	def edit_option_removeedit(self, edit_option):
		"""Edit option 8 (remove) and 9 (edit)"""
		if edit_option == '8':
			edit_index = input("\nType the number of the book you want to remove: ")
			try:
				index = int(edit_index) - 1
				book = self.book_list[index]
				indexes = []
				indexes.append(index)
				self.remove_book(indexes)
				undo_option = input("\nType 'u' to undo, enter to continue... ")
				if undo_option == 'u':
					self.add_book(book)
					input("\nEnter to continue... ")
			except:
				input("\nIt's not a positive integer, enter to continue... ")
		elif edit_option == '9':
			edit_index = input("\nType the number of the book you want to edit: ")
			try:
				index = int(edit_index) - 1
				book = edit_book(self.book_list[index])
				indexes = []
				indexes.append(index)
				self.remove_book(indexes)
				self.add_book(book)
				input("\nEnter to continue... ")
			except:
				input("\nIt's not a positive integer, enter to continue... ")
