from collections import defaultdict


def solution(words, queries):
    word_map = Trie('')
    reversed_word_map = Trie('')
    for word in words:
        word_map.insert(word)
        reversed_word_map.insert(word[::-1])
    result = list()
    for query in queries:
        if query.endswith('?'):
            result.append(word_map.search(query))
        else:
            result.append(reversed_word_map.search(query[::-1]))
    return result


class Trie(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.children_count = defaultdict(int)

    def insert(self, word):
        current = self
        for i in range(len(word)):
            length = len(word[i:])
            current.children_count[length] += 1
            
            if current.children.get(word[i]):
                current = current.children[word[i]]
            else:
                new_node = Trie(word[i])
                current.children[word[i]] = new_node
                current = new_node

    def search(self, word):
        current = self
        for i in range(len(word)):
            if word[i] == '?':
                return current.children_count[len(word[i:])]
            else:
                child = current.children.get(word[i])
                if not child:
                    return 0
                current = child

if __name__ == '__main__':
    x = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
    print(x)

