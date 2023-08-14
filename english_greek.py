from encoder_tree import encode_sentence, create_binary_tree_encode, read_word_pairs_encode
from decoder_tree import decode_sentence, create_binary_tree_decode, read_word_pairs_decode
import color


def main():
    # import dictionary of word pairs
    file_path = 'ENGLISH_GREEK.txt'
    word_pairs_encode = read_word_pairs_encode(file_path)
    word_pairs_decode = read_word_pairs_decode(file_path)
    bst_encode = create_binary_tree_encode(word_pairs_encode)  # encode BST object
    bst_decode = create_binary_tree_decode(word_pairs_decode)  # decode BST object

    # introduction
    print(f"{color.BOLD}{color.BLUE}Welcome to the Greek-English translator!{color.END}")
    print("You can enter an English phrase to be translated to Greek"
          " or a Greek phrase to be translated to English.")
    print("If your word is not found in the dictionary, you can provide a Greek "
          "translation to add it.")

    end = False

    while end is False:
        encode, decode, end = user_choice(bst_encode)
        if encode:
            encode_to_greek(bst_encode)
        elif decode:
            decode_to_english(bst_decode)
        elif end:
            print(f"\n{color.BLUE}{color.BOLD}Thank you for using the translator!{color.END}")
            break


# user chooses what action they would like to take
def user_choice(bst_encode):
    valid_choice = False
    encode = False
    decode = False

    while valid_choice is False:
        print("\n1. Translate from English to Greek\n"
              "2. Translate from Greek to English\n"
              "3. Add a new word to the dictionary\n"
              "4. Exit")
        choice = input("What would you like to do? (1, 2, 3, or 4): ")

        if choice == '1':
            encode = True
            valid_choice = True
            end = False
        elif choice == '2':
            decode = True
            valid_choice = True
            end = False
        elif choice == '3':
            english = input("Enter the English word: ")
            new_dictionary_entry(english, bst_encode)
            end = False
        elif choice == '4':
            end = True
            break
        else:
            print(f"{color.RED}Invalid choice{color.END}")
    return encode, decode, end


# encoding function
def encode_to_greek(bst_encode):
    input_sentence = input("Enter an English sentence to encode: ")
    encoded_sentence = encode_sentence(bst_encode, input_sentence)

    words_not_found = []
    for word in input_sentence.split():
        if not word_already_exists(word):
            words_not_found.append(word)

    if words_not_found:
        print(f"{color.RED}The following words were not found in the dictionary:{color.END} {', '.join(words_not_found)}")
        add_to_dictionary = input("Would you like to add them to the dictionary? (yes/no): ")

        if add_to_dictionary.lower() in ['yes', 'y']:
            for word in words_not_found:
                new_dictionary_entry(word, bst_encode)
            encoded_sentence = encode_sentence(bst_encode, input_sentence)
            print(f"Encoded Sentence: {color.BLUE}{encoded_sentence}{color.END}")

        elif add_to_dictionary.lower() in ['no', 'n']:
            print(f"Encoded Sentence: {color.BLUE}{encoded_sentence}{color.END}")
    else:
        print(f"Encoded Sentence: {color.BLUE}{encoded_sentence}{color.END}")


# decoding function
def decode_to_english(bst_decode):
    input_sentence = input("Enter a Greek word to decode: ")
    # Translate potential English letters to Greek letters
    # translated_sentence = translate_to_greek(input_sentence, read_greek_letters("english_greek_letters.txt"))
    decoded_sentence = decode_sentence(bst_decode, input_sentence)

    print(f"Decoded Sentence: {color.PURPLE}{decoded_sentence}{color.END}")


# function to read english to greek letter mappings from a file
def read_greek_letters(file_path):
    mappings = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            english, greek = line.strip().split(" - ")
            mappings[english] = greek
    return mappings


# Function to translate English letters to Greek letters
def translate_to_greek(english_text, translation_mappings):
    greek_text = ''
    for char in english_text:
        if char.lower() in translation_mappings:
            greek_text += translation_mappings[char.lower()]
        else:
            greek_text += char
    return greek_text


def word_already_exists(word):
    with open("ENGLISH_GREEK.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(word + ' - '):  # match the formatting in the txt file
                return True
    return False


# add new entry to the dictionary
def new_dictionary_entry(english, bst_encode):
    # check txt file to see if word already exists
    word_exists = word_already_exists(english)

    if word_exists:
        print(f"{color.GREEN}Word is already in the dictionary!{color.END}")

    # if not ask for the greek word
    if not word_exists:
        greek = input(f"Enter the Greek translation for '{english}': ")

        # Read the translation mappings from the file
        translation_mappings = read_greek_letters("english_greek_letters.txt")

        # Translate the Greek letters if they're English letters
        translated_greek = translate_to_greek(greek, translation_mappings)

        # Add to the ENGLISH_GREEK text file
        with open("ENGLISH_GREEK.txt", "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(f"{english} - {translated_greek}")
            print(f"{color.YELLOW}The following entry has been added to the dictionary: "
                  f"{color.BLUE}{english} - {translated_greek}{color.END}")

        # Update the bst_decode object with the new entry
        bst_encode.insert(english, translated_greek)


if __name__ == "__main__":
    main()

