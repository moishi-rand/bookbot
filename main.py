

def print_words(file_contents):
    words = file_contents.split(" ")
    print(len(words))


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print_words(file_contents)    