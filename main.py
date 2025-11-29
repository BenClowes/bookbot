from stats import get_book_text, count_words, count_letters, letter_report
import sys

def print_report(file_path, word_count, sorted_letters):
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for item in sorted_letters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

def main(args):
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = args[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    letter_counts = count_letters(book_text)
    sorted_letters = letter_report(letter_counts)
    print_report(file_path, word_count, sorted_letters)


main(sys.argv)
