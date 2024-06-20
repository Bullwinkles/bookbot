def main():
	book_path = "books/frankenstein.txt"
	text = reader(book_path)
	#print(text)
	word_count = word_counter(text)
	print(word_count)


def reader(path):
	with open(path) as f:
		return f.read()

def word_counter(book):
	word_list = book.split()
	return len(word_list) 
	

main()