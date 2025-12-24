from stats import get_num_words, get_letter_words, sort_letter_counts
import sys
def main():
	if len(sys.argv)<2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = get_book_text(book_path)

	num_words = get_num_words(text)
	letter_counts = get_letter_words(text)
	sorted_chars = sort_letter_counts(letter_counts)

	print(f"Found {num_words} total words")
    
	for item in sorted_chars:
		char=item["char"]
		num=item["num"]
		if char.isalpha():
			print(f"{char}: {num}")


def get_book_text(path):
	with open(path) as f:
		return f.read()

main()
