def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_word = count_words(text)
    count_character = count_characters(text)
    char_count_list = sorted_list(count_character)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_word} words found in the document")
    print("")

    for item in char_count_list:
        print(f"The {item.get('char')} character was found {item.get('count')} times")

    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    character = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if c in character:
                character[c] += 1
            else:
                character[c] = 1

    return character


def sorted_list(list):
    char_count_list = [{"char": char, "count": count} for char, count in list.items()]
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list


def sort_on(dict):
    return dict["count"]

if __name__ == "__main__":
    main()
