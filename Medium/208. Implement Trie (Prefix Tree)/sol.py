# Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self):
        # Initialize the node with an empty dictionary for children and a boolean to mark the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert a word into the Trie
        node = self.root
        for char in word:
            # For each character in the word, check if it exists in the current node's children
            if char not in node.children:
                # If the character is not present, create a new TrieNode
                node.children[char] = TrieNode()
            # Move to the child node corresponding to the character
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Search for a word in the Trie
        node = self.root
        for char in word:
            # For each character in the word, check if it exists in the current node's children
            if char not in node.children:
                # If the character is not found, the word does not exist in the Trie
                return False
            # Move to the child node corresponding to the character
            node = node.children[char]
        # Return True if the current node marks the end of a word, otherwise return False
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Check if there is any word in the Trie that starts with the given prefix
        node = self.root
        for char in prefix:
            # For each character in the prefix, check if it exists in the current node's children
            if char not in node.children:
                # If the character is not found, no word with the given prefix exists in the Trie
                return False
            # Move to the child node corresponding to the character
            node = node.children[char]
        # If all characters of the prefix are found, return True
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
