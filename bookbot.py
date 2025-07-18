from stats import *

def main():
	book_path = "books/frankenstein.txt"
	text = reader(book_path)
	char_count = char_counter(text)
	word_count = word_counter(text)
	dictionary_list = dict_list_creator(char_count) 
	sorter(dictionary_list)
	report(dictionary_list, book_path, word_count)

def reader(path):
	with open(path) as f:
		return f.read()

def report(list, path, count):
	print(f"--- Begin Report of {path} ---")
	print()
	print(f"There are {count} words in this book.")
	print()
	for char in list:
		print(f"The character '{char['name']}' was found '{char['num']}' times.")
	print()
	print("--- End Report ---")

main()
