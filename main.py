from stats import calculate_num_words, calculate_num_characters, sort_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("========== Book Bot ==========")
    print("Analyzing book found at books/frankenstein.txt")
    print("---------- Word Count ----------")
    print(f'Found {calculate_num_words(get_book_text(sys.argv[1]))} total words')
    print("-------- Character Count -------")
    char_dict = calculate_num_characters(get_book_text(sys.argv[1]))
    sorted_dict = sort_dicts(char_dict)

    for x in sorted_dict:
        print(f'{x["char"]}: {x["num"]}')
    
    print("------------ End ------------")

    

main()
