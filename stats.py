def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_string):
    words = book_string.split()
    return len(words)

def count_letters(book_string):
    result = {}
    for letter in book_string.lower():
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result

def sort_by_num(item):
    return item["num"]

def letter_report(letter_dict: dict):
    result = []
    for letter, count in letter_dict.items():
        result.append({
            "char": letter,
            "num": count
        })
    result.sort(reverse=True, key=sort_by_num)
    return result