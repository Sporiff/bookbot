def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowercase_text = text.lower()
    character_count =  {}
    for character in lowercase_text:
        if character == " ":
            continue
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))

def print_report(text):
    total_words = count_words(text)
    total_characters = count_characters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")
    for character in total_characters:
        print(f"The '{character}' character was found {total_characters[character]} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)

main()
