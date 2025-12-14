
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

def character_breakup_dict_prepare_for_print(char_dict):
    final_list = []
    
    for key, value in char_dict.items():
        if key.isalpha() == False:
            continue
        final_dict = {}
        final_dict["char"] = key
        final_dict["num"] = value
        final_list.append(final_dict)

    def sort_on(items):
        return items["num"]

    final_list.sort(key=sort_on, reverse=True)
    return final_list