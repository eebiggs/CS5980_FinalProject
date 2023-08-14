import color
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)

        return node

    def find(self, key):
        return self._find_recursive(self.root, key)

    def _find_recursive(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node.value
        elif key < node.key:
            return self._find_recursive(node.left, key)
        else:
            return self._find_recursive(node.right, key)


def read_word_pairs_decode(file_path):
    word_pairs = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(" - ")
            english = parts[0]
            greek_translations = parts[1].split(", ")
            for greek in greek_translations:
                if greek in word_pairs:
                    word_pairs[greek].append(english)
                else:
                    word_pairs[greek] = [english]
    return word_pairs


def create_binary_tree_decode(word_pairs):
    bst = BinarySearchTree()
    for greek, english in word_pairs.items():
        bst.insert(greek, english)
    return bst


def decode_sentence(bst, sentence):
    words = sentence.split()  # Split sentence into words
    decoded_words = []

    for word in words:
        # print(f"Trying to decode: {word}") # Debugging
        english_translation = bst.find(word)
        # print(f"Word: {word}, English Translation: {english_translation}")  # Debugging
        if english_translation:
            decoded_words.append(', '.join(english_translation))
        else:
            decoded_words.append(word)  # If not found, keep original word
            print(f"{color.RED}Your word was not found in the dictionary!{color.END}")

    return ' '.join(decoded_words)
