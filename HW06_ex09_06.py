#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

##############################################################################
def main():
    with open("words.txt", "r") as fin:
		count_abc = 0
		total_words = 0
		for line in fin:
			total_words += 1
			word = line.strip()
			if is_abecedarian(word):
				count_abc+= 1
		print count_abc



    # print is_abecedarian('best')

if __name__ == '__main__':
    main()
