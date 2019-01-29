### Fama Uzi
### 29/01/2019
### Main menu for books collection

# Using os to clear screen, not applicable in Python IDLE
import os

# All created program (except mainmenus) is in /data
from data.bookcreation import create_book
from data.bookcreation import edit_book
from data.library import Library

def init_user():
	"""An initial function to run Library(username, library)"""
	global username, user

	username = input("Please enter username: ")

	# Accessing library with 'library' as default library folder
	user = Library(username)

def clear_screen():
	"""Clear screen function, check if os is Windows ('nt') or not"""
	global clear_enable

	# print(os.name)
	if clear_enable == 1:
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
		print("\n--------------------" + username + "--------------------\n")
	
# -----------

print("\nWelcome to the Bookish Program\n")
init_user()

clear_enable = 2
is_changed = 0
while True:
	# Initialization error check, skip loop if OSError and SyntaxError
	if user.init_error == 'OSError':
		init_user()
		continue
	elif user.init_error == 'SyntaxError':
		is_delete = input("Enter 'delete' to delete " + user.filename + ", otherwise return to the main menu...")
		print()
		if is_delete == 'delete':
			user.delete_file()
		init_user()
		continue
	elif user.init_error != 0:
		input("An error has been occured while initalizing the program. Enter to quit the program...")
		break

	# Check whether the username is changed or not
	if is_changed == 1:
		username = new_username
		is_changed = 0
	else:
		is_changed = 0

	# Main menu interaction:
	if clear_enable == 1:
		clear_screen()
	else:
		print("\n--------------------" + username + "--------------------\n")
	print("Enter the number of the desired options below:")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("1. Add a book to the collection")
	print("2. Search for books (+ remove all/remove/edit)")
	print("3. Sort and show your collection (+ add/remove/edit)")
	print()
	print("8. Save as a new username")
	print("9. Change your username")
	print("0. Log out")
	print()
	print("q. Quit the program")
	print("Type 'delete' to delete your collection.")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	if clear_enable == 2:
		print("For Python's IDLE user, type 'disable' to disable clear screen feature.")
		print("Otherwise, there will be multiple 'pop-ups'.")
	option = input('Option: ').strip().lower()
	
	if clear_enable != 0 and option == 'disable':
		clear_enable = 0
		print("\n~~~~~Clear screen disabled~~~~~\n")
		option = input('Option: ').strip().lower()
	elif clear_enable == 2:
		clear_enable = 1

	print()

	if option == '1':
		clear_screen()
		book = create_book()
		user.add_book(book)
		input("\nEnter to continue... ")
	elif option == '2':
		clear_screen()
		print("Search options:")
		print("~~~~~~~~~~~~~~~~~~~~")
		print("1. Search in name (default)")
		print("2. Search in author")
		print("3. Search in genre")
		print("4. Search in publisher")
		print("5. Search in published year")
		print()
		print("0. Return to main menu")
		print("~~~~~~~~~~~~~~~~~~~~")
		print()
		searchoption = input('Option: ').strip().lower()
		print()

		if searchoption == '2':
			book_keys = 'Author'
		elif searchoption == '3':
			book_keys = 'Genre'
		elif searchoption == '4':
			book_keys = 'Publisher'
		elif searchoption == '5':
			book_keys = 'Year'
		elif searchoption == '0':
			indexes = []
		else: # Default
			book_keys = 'Name'

		clear_screen()
		indexes = user.find_bookindex(book_keys)
		user.show_books(indexes)
		print("\nOptions: 7.Remove all ||| 8. Remove ||| 9. Edit ||| Default to main menu")
		edit_option = input("\nEnter the option to continue... ")
		user.edit_option_removeedit(edit_option)
		if edit_option == '7':
			# Check if indexes is empty to remove books
			if not indexes:
				pass
			else:
				user.remove_book(indexes)
			input("\nEnter to continue... ")
		elif edit_option != '8' and edit_option != '9':
				edit_flag = False

	elif option == '3':
		clear_screen()
		print("Sorting options:")
		print("~~~~~~~~~~~~~~~~~~~~")
		print("1. Sort by name (default)")
		print("2. Sort by author")
		print("3. Sort by genre")
		print("4. Sort by publisher")
		print("5. Sort by published year")
		print()
		print("0. Return to main menu")
		print("~~~~~~~~~~~~~~~~~~~~")
		print()
		sortoption = input('Option: ').strip().lower()
		print()

		if sortoption == '2':
			sortby = 'Author'
		elif sortoption == '3':
			sortby = 'Genre'
		elif sortoption == '4':
			sortby = 'Publisher'
		elif sortoption == '5':
			sortby = 'Year'
		elif sortoption == '0':
			continue
		else: # Default
			sortby = 'Name'

		edit_flag = True
		while edit_flag == True:
			clear_screen()
			user.show_list(sortby)
			print("\nOptions: 1. Add ||| 8. Remove ||| 9. Edit ||| Default to main menu")
			edit_option = input("\nEnter the option to continue... ")
			user.edit_option_removeedit(edit_option)
			if edit_option == '1':
				print()
				book = create_book()
				user.add_book(book)
				input("\nEnter to continue... ")
			elif edit_option != '8' and edit_option != '9':
				edit_flag = False

	elif option == '8':
		new_username = input("Type a new username: ")
		clear_screen()
		is_changed = user.save_as_file(new_username)
		input("\nEnter to continue... ")
	elif option == '9':
		new_username = input("Type a new username: ")
		clear_screen()
		is_changed = user.change_username(new_username)
		input("\nEnter to continue... ")
	elif option == '0':
		# Doesn't actually log the user out, make them enter the new username instead.
		input("\nYou've been logged out, enter to continue...\n")
		init_user()
	elif option == 'q':
		break
	elif option == 'delete':
		user.delete_file()
		end_option = input("\nEnter 'q' to quit, otherwise return to main menu... ")
		if end_option == 'q':
			break
		else:
			init_user()
	else:
		input("The only eligible entry are the options above, try again. Enter to continue... ")
