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


# Read and parse the text file
def read_word_pairs_encode(file_path):
    word_pairs = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(" - ")
            english = parts[0]
            # print('printing parts') debugging
            # print(parts) debugging
            greek_translations = parts[1].split(", ")
            for greek in greek_translations:
                word_pairs[english] = greek
    return word_pairs


# Create the binary search tree
def create_binary_tree_encode(word_pairs):
    bst = BinarySearchTree()
    for english, greek in word_pairs.items():
        bst.insert(english, greek)
    return bst


def encode_sentence(bst, sentence):
    words = sentence.split()  # Split sentence into words
    encoded_words = []

    for word in words:
        greek_translation = bst.find(word)
        if greek_translation:
            encoded_words.append(greek_translation)
        else:
            encoded_words.append(word)  # If not found, keep original word

    return ' '.join(encoded_words)
