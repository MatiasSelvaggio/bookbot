import re

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_to_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_sorted_list(chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    #print_report(chars_dict)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_to_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(file):
    words = file.split()
    return len(words)

def get_chars_dict(file):
    file_lower = file.lower()
    output = {}
    for char in file_lower:
        if( char in output):
            output[char]+=1
        else:
            output[char]=1
    return output

def print_report(dictionaries):
    char_parttern= r'[a-zA-Z]'
    dict(sorted(dictionaries.items(), key=lambda item: item[1]))
    for char in dictionaries:
        if re.match(char_parttern,char):
            num_words = dictionaries[char]
            print(f"The '{char}' character was found {num_words} times")
            

def sort_on(dict):
    return dict["num"]

def chars_dict_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()