def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(input_string: str):
    words = input_string.split()
    return len(words)

def main():
    FILENAME = "books/frankenstein.txt"
    contents = read_file(FILENAME)
    num_words = get_word_count(contents)
    print(num_words)

main()