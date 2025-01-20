def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    FILENAME = "books/frankenstein.txt"
    contents = read_file(FILENAME)
    print(contents)

main()