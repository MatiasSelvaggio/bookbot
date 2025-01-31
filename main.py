import re

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count = calcute_words(file_contents)
        print(f"{count} words found in the document")
        print()
        dictionary = count_characters(file_contents)
        print_report(dictionary)
        print("--- End report ---")


def calcute_words(file):
    words = file.split()
    return len(words)

def count_characters(file):
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
            count = dictionaries[char]
            print(f"The '{char}' character was found {count} times")
            

def sort_on(dict):
    return dict["num"]

main()