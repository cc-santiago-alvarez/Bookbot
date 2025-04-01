import sys
from stats import count_words, count_characters, sorted_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sorted_characters(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

    print(f"{num_words} words found in the document")
    print(f"{char_count}")

if __name__ == '__main__':
    main()