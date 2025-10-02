import sys
from stats import count_words, count_chars, chars_to_list

def main():
    # Check CLI arguments first
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_chars(text)
    sorted_chars = chars_to_list(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as file:
        return file.read()

main()
