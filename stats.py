
def get_word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_character_breakup_count(text):
    final_dict = {}
    text = text.lower()
    for t in text:
        if t in final_dict:
            final_dict[t] += 1
        else:
            final_dict[t] = 1
    return final_dict