def get_num_words(text):
	words = text.split()
	return len(words)

def get_letter_words(text):
	list_words= {}
	for letter in text:
		letter = letter.lower()
		if letter in list_words:
			list_words[letter]+=1
		else:
			list_words[letter] = 1
	return list_words
	
def sort_on(items):
        return items["num"]

def sort_letter_counts(letter_counts):
	char_list = []
	for char, count in letter_counts.items():
		another_list= {"char": char, "num": count}
		char_list.append(another_list)

	char_list.sort(reverse=True, key=sort_on)
	return char_list


