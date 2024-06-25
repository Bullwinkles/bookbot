def main():
	book_path = "books/frankenstein.txt"
	text = reader(book_path)
	char_count = char_counter(text)
	word_count = word_counter(text)
	print(f"Amount of words in book: {word_count}")
	print(f"Character count in book: {char_count}")




def reader(path):
	with open(path) as f:
		return f.read()

def word_counter(book):
	word_list = book.split()
	return len(word_list)

def char_counter(string):
	lowered_string = string.lower()
	char_dict = {}
	for char in lowered_string:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	return char_dict

	

main()