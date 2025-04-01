def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count 

def sorted_characters(char_count):
    char_list = [{"char": char, "count": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=lambda d: d["count"])  # Sort descending by count
    return char_list