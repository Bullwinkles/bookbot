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

def dict_list_creator(dictionary):
	dict_list = []
	for char in dictionary:
		if char.isalpha() == True:
			dict_list.append({"name" : char, "num" : dictionary[char]})
		else:
			pass
	return dict_list

def sorting_key(dict):
	return dict["num"]

def sorter(list):
	list.sort(reverse=True, key=sorting_key)
