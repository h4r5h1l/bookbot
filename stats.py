def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
    
def get_sorted_dict(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))