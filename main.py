#!/usr/bin/env python3

def main():
    text_path = "books/frankenstein.txt"
    text = get_text(text_path)
    return count_words(text)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

if __name__ == "__main__":
    main()
