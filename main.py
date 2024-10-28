#!/usr/bin/env python3

def main():
    text_path = "books/frankenstein.txt"
    text = get_text(text_path)
    word_total = word_count(text)
    char_totals = count_char(text)
    pretty_printing(char_totals, word_total)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_char(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def pretty_printing(char_count, word_count):
    print(f"{word_count} words in the document")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")

if __name__ == "__main__":
    main()
