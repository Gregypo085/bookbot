def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
        
def sort_on(item):
    return item["num"]

def chars_to_list(char_dict):
    # Convert dict into a list of dicts
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha(): # Only include alph characters
            char_list.append({"char": char, "num": count})
    # Sort list by num
    char_list.sort(key=sort_on, reverse=True)
    return char_list
        