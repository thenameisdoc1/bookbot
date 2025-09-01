def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return len(file_contents.split())

def get_char_count_dct(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    char_count = {}
    for char in file_contents.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    char_count = {}
    for char in file_contents.lower(): # Create 1 dct with count of times chars appear
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_count_ls = [{'char': char, 'count': count} for char, count in char_count.items()] 
    return sorted(char_count_ls, key=lambda x: (-x['count'], x['char'])) # return ls that sorts each dct in char_count_ls by ls in "count"
