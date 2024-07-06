def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
   # print(count_words(file_contents))
    characters = count_characters(file_contents)
    sorted_dict = only_characters_dict(characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()

    for ch in sorted_dict:
        print(f"The {ch['char']} character was found {ch['num']} times")
    
    print("--- End report ---")
    #print(characters)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for character in text:
        if character.lower() not in characters:
            characters[character.lower()] = 1
        else:
            character_count = characters[character.lower()] = characters[character.lower()]
            characters[character.lower()] = character_count + 1     
    return characters

def only_characters_dict(characters):
    characters_dict = []
    for ch in characters:
        if(ch.isalpha()):
            characters_dict.append({"char": ch, "num": characters[ch]})
    characters_dict.sort(reverse=True, key = sort_on)
    return characters_dict

def sort_on(d):
    return d["num"]

main()