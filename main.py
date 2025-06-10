from stats import get_book_text, get_num_words, get_char_count, get_sorted_char_report

def count_words(text: str) -> int:
    return len(text.split())

def main():
    text = get_book_text('books/frankenstein.txt')
    num = count_words(text)
    print(f"{num} words found in the document")

    char_counts = get_char_count(text)
    print(char_counts)

    report = get_sorted_char_report(char_counts)

    for entry in report:
        print(f"{entry['char']}: {entry['num']}")


if __name__ == '__main__':
    main()