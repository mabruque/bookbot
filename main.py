def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(input_string: str):
    words = input_string.split()
    return len(words)

def get_character_count(input_string: str):
    char_dict = dict()
    for char in input_string.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def print_report(filename: str, character_dict):
    print(f"--- Begin report of {filename} ---")
    print("\n")
    for char in character_dict:
        print(f"The '{char}' character was found {character_dict[char]} times")
    print("--- End report ---")


def main():
    FILENAME = "books/frankenstein.txt"
    contents = read_file(FILENAME)
    num_words = get_word_count(contents)
    character_count = get_character_count(contents)
    print_report(FILENAME, character_count)

main()