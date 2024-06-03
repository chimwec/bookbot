def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

if __name__ == "__main__":
    main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

print("---Begin report of books/frankenstein.txt---")


def get_chars_dict(text):
    chars = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars
print("77986 words found in the document")


#converting the dictionary of characters into a list of dictionaries and then use the .sort() method to sort by the number of occurrences then print to the console.
def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars = get_chars_dict(text)
    
    # Creating a list of dictionaries with character and their counts
    chars_list = [{"character": char, "count": count} for char, count in chars.items()]
    
    # Sorting the list by the 'count' key in descending order
    chars_list.sort(key=lambda x: x["count"], reverse=True)
    
    # Printing the characters and their counts in the specified format
    for char_dict in chars_list:
        print(f"The '{char_dict['character']}' character was found {char_dict['count']} times")

# Run the main function
if __name__ == "__main__":
    main()
    print("---End report---")