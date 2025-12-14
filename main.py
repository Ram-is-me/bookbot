from stats import get_word_count, get_character_breakup_count, character_breakup_dict_prepare_for_print
import sys

def get_book_text(input_file):
    with open(input_file) as f:
        contents =  f.read()
        return contents

def main():
    book_text = get_book_text()
    print(book_text)  


if __name__ == "__main__":
    
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    book_path = sys.argv[1]
    num_words = get_word_count(get_book_text(book_path))
    
    
    character_breakup_dict = get_character_breakup_count(get_book_text(book_path))
    # print("Character breakup count:", character_breakup_dict)
    
    final_dict = character_breakup_dict_prepare_for_print(character_breakup_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in final_dict:
        if item["char"].isalpha():
            print(str(item["char"] + ": " + str(item["num"])))
    print("============= END ===============")
    
    
    