# simplebookish
This is a simple Python program to store book lists
-----------------------------------------------------------

Fama Uzi
29/01/2019

My first time creating a repository here and hopefully will not be the last.
This project is specifically created for a beginner online course in Skillshare's [Python 3: A Beginners Guide to Python Programming](https://www.skillshare.com/classes/Python-3-A-Beginners-Guide-to-Python-Programming/821742951/project-guide).

To complete the challenge, this application will need to have three main features (which are already fulfilled):
- [x] It must allow users to add new books to the collection
  - Users can access the program by executing mainmenu.py which will access /data/ folder to create their book collections in form of list of dictionaries
  - Add/Remove/Edit functions are included
- [x] The application must allow users to view all the books in their collection
  - Book collections will be saved in /library/ folder and can be accessed through the program and text editor
  - Users can also sort the list by dictionary keys
- [x] The application must allow users to find a book within their collection by any of its attributes
  - Through options, users can find keyword in specific dictionary keys
  - While searching multiple books (dictionaries), users can also remove all books in the search results
  
A note:
  This program using os.system('cls') for Windows ('nt') and os.system('clear') for others to clear the screen of the program. Because of this the users which use Python's IDLE or something similar need to type 'disable' when prompted to disable this feature.
