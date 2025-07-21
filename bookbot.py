from stats import *
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
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
