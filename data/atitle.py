### Fama Uzi
### 26/01/2019
### Creating 'advanced' version of title() because there are some lowercase words in title; title() also can't differentiate contractions (e.g. I'm) for some reason

def atitle(sentence):
	"""
	Title with some lowercase words, atitle as in 'advanced' title().
	Hopefully will solve most capitalization problems in a title.

	Expected result: 'a 	 brIEF hISTory   of TIME   ' -> 'A Brief History of Time'
	"""
	# Articles, conjunctions, prepositions
	exceptions = [
	'a', 'an', 'the', # articles
	'and', 'as', 'but', 'for', 'if', 'nor', 'once', 'or', 'so', 'than', 'that', 'till', 'when', 'yet', # conjunctions
	'at', 'by', 'down', 'for', 'from', 'in', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'over', 'past', 'to', 'upon', 'with' # prepositions
	]
	# Some books have roman numerals for their title (e.g. biography of a king); I to XX
	roman_numerals = [
	'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii',  'viii', 'ix', 'x',
	'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx'
	]

	# Create titled word_list
	word_list = sentence.title().split()

	# Create word_check which is the lowercase of word_list
	word_check = sentence.lower().split()

	# Check every word, if there is a contraction (e.g. I'm), capitalize() it instead
	# Expected result: you're -> You're, john's book -> John's Book
	i = 0
	for word in word_list:
		# Every word contains ' except as the first character
		if "'" in word and word[0] != "'":
			word_list[i] = word_list[i].capitalize()
		i += 1

	# Check every word but the first and last word for exceptions
	# Expected result: 'an introduction to python' -> 'An Introduction to Python'
	i = 1
	for word in word_check[1:-1]:
		if word in exceptions:
			word_list[i] = word_check[i]
		i += 1

	# Check colon in every word (except the last word) so the next word will be capitalized to correct word in exceptions list
	# Expected result: 'bears: a brief history' -> 'Bears: A Brief History'
	i = 0
	for word in word_list[:-1]:
		if ":" in word:
			word_list[i + 1] = word_list[i + 1].capitalize()
		i += 1

	# Check roman numerals from I to XX and uppercase it
	# Expected result: 'autobiography of emperor charles iv' -> 'Autobiography of Emperor Charles IV'
	i = 0
	for word in word_check:
		if word in roman_numerals:
			word_list[i] = word_check[i].upper()
		i += 1

	# Join word_list to become new_sentence
	new_sentence = ' '.join(word_list)
	return new_sentence
