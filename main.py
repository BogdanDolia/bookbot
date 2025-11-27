import os
import sys

from stats import get_num_words, characters_counter, sort_on


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    book_path = os.path.join(script_dir, path_to_book)
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except Exception as e:
        print(f"Error: {e}")

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    counted = characters_counter(text)
    converted_data = []
    for char, count in counted.items():
        if char.isalpha():
            converted_data.append({"char": char, "num": count})
    converted_data.sort(reverse=True, key=sort_on)
    for i in converted_data:
        print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
