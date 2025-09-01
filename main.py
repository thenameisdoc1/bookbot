import sys
from stats import get_char_count_dct, sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookcontents = get_char_count_dct(f"{sys.argv[1]}")

    if bookcontents:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at \"{sys.argv[1]}\"...")
        print("----------- Word Count ----------")
        with open(f"{sys.argv[1]}") as f:
            file_contents = f.read()
        word_count = len(file_contents.split())
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        sorted_char_count = sort(f"{sys.argv[1]}")
        for dcts in sorted_char_count:
            print(f"{dcts["char"]}: {dcts["count"]}")
        print("============= END ===============")
main()
