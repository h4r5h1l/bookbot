import sys
from stats import get_num_words, get_char_count, get_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  
        sys.exit(1) 
    book_contents = get_book_text(sys.argv[1])
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_contents)} total words")
    print("--------- Character Count -------")  
    char_dict = get_char_count(book_contents)
    for key, value in get_sorted_dict(char_dict).items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
main()