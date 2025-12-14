from stats import get_word_count, get_character_breakup_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        contents =  f.read()
        return contents

def main():
    book_text = get_book_text()
    print(book_text)  


if __name__ == "__main__":
    num_words = get_word_count(get_book_text())
    print(f"Found {num_words} total words")
    
    character_breakup_dict = get_character_breakup_count(get_book_text())
    print("Character breakup count:", character_breakup_dict)
    
    