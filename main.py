def main():
    book_loc = "books/frankenstein.txt"
    with open(book_loc) as f:
        file_contents = f.read()
        report_info(book_loc, file_contents)


def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    
    char_dic = {}
    for word in book:
        for letter in word.lower():
            if letter in char_dic and letter.isalpha():
                char_dic[letter] += 1
            elif letter.isalpha():
                char_dic[letter] = 1
    return char_dic

def report_info(book_loc, book):
    print(f"--- Begin report of {book_loc} ---")
    print(f"{word_count(book)} words found in the document\n")
    char_dic = char_count(book)
    sorted_dic = {k: v for k, v in sorted(char_dic.items(), key=lambda item: item[1], reverse=True)}
    for key, value in sorted_dic.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

main()