from __future__ import annotations
from typing import Dict, List, Optional

word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

word_digits_dict: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class TrieNode:
    def __init__(self) -> None:
        self.children = dict()
        self.word_ending_here = None

    def get_child(self, c) -> Optional[TrieNode]:
        return None if c not in self.children else self.children[c]

    def add_child(self, word, word_fragment: str) -> None:
        if len(word_fragment) == 0:
            self.word_ending_here = word
            return
        c = word_fragment[0]
        if c not in self.children:
            self.children[c] = TrieNode()
        node = self.children[c]
        node.add_child(word, word_fragment[1:])

    def __repr__(self) -> str:
        return str(self.children.keys())


word_digit_trie = TrieNode()
for word in word_digits:
    word_digit_trie.add_child(word, word)


def parse_input(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


# this parse function assumed that 'twone' was just 2, but that seems to not be the case :(
def parse_input_trie(filename):
    with open(filename, "r") as f:
        s = []
        node = word_digit_trie
        for line in f:
            line_chars = []
            line = line.strip()
            for c in line:
                line_chars.append(c)
                if c in node.children:
                    node = node.children[c]
                    if node.word_ending_here is not None:
                        line_chars.append(str(word_digits_dict[node.word_ending_here]))
                        node = word_digit_trie
                else:
                    if c in word_digit_trie.children:
                        node = word_digit_trie.children[c]
                    else:
                        node = word_digit_trie
            s.append("".join(line_chars))
        return s


def parse_input_pt2(filename):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            for k, v in word_digits_dict.items():
                line = line.replace(k, f"{k}{v}{k}")
            yield line
