#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
# def has_no_e(word):
# 	"""This should traverse all the characters in the word and return False if 
# 	any of them are 'e'. However, it is only returning False if the word starts 
# 	with 'e'. Why is that???"""
# 	for letter in word:
# 		if letter == 'e':
# 			return False
# 		return True

def has_no_e(word):
	"""this function uses find to find the index of the first appearance of the
	the letter 'e'. If it never appears, the index is -1, therefore returns True
	if there is no 'e'. This is working correctly but I still want to know Why
	the one above isn't!"""
	if word.find("e") == -1:
		return True
	else:
		return False


##############################################################################
def main():
    with open("words.txt", "r") as fin:
		count_no_e = 0
		total_words = 0
		for line in fin:
			total_words += 1
			word = line.strip()
			if has_no_e(word):
				count_no_e += 1
		print count_no_e / float(total_words) * 100

	# print has_no_e('em')

if __name__ == '__main__':
    main()
