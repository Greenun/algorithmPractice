# 예시
def count_leaf(tmp_trie, depth):
    space = [(tmp_trie, k, depth) for k in tmp_trie.keys()]

    cnt = 0
    while len(space) > 0:
        tmp_trie, k, depth = space[0]
        space = space[1:]

        if depth == 0 and k == '@@@':
            cnt += 1
            continue

        if depth > 0 and k != '@@@':
            space.extend([(tmp_trie[k], new_k, depth-1) for new_k in tmp_trie[k].keys() if type(tmp_trie)])

    return cnt

def solutionx(words, queries):
    answer = []

    fow_trie = {}

    for word in words:
        tmp_trie = fow_trie

        if 'count' not in tmp_trie:
            tmp_trie['count'] = {}

        if len(word) not in tmp_trie['count']:
            tmp_trie['count'][len(word)] = 1
        else:
            tmp_trie['count'][len(word)] += 1

        for i, c in enumerate(word, 1):
            if c not in tmp_trie:
                tmp_trie[c] = {}
            tmp_trie = tmp_trie[c]

            if 'count' not in tmp_trie:
                tmp_trie['count'] = {}

            if (len(word) - i) not in tmp_trie['count']:
                tmp_trie['count'][len(word) - i] = 1
            else:
                tmp_trie['count'][len(word) - i] += 1

            if i == len(word):
                tmp_trie['@@@'] = word
    print(fow_trie)

    rev_trie = {}

    for word in words:
        tmp_trie = rev_trie
        word = word[::-1]

        if 'count' not in tmp_trie:
            tmp_trie['count'] = {}

        if len(word) not in tmp_trie['count']:
            tmp_trie['count'][len(word)] = 1
        else:
            tmp_trie['count'][len(word)] += 1

        for i, c in enumerate(word, 1):
            if c not in tmp_trie:
                tmp_trie[c] = {}
            tmp_trie = tmp_trie[c]

            if 'count' not in tmp_trie:
                tmp_trie['count'] = {}

            if (len(word) - i) not in tmp_trie['count']:
                tmp_trie['count'][len(word) - i] = 1
            else:
                tmp_trie['count'][len(word) - i] += 1

            if i == len(word):
                tmp_trie['@@@'] = word

    for query in queries:

        if query[0] == '?':
            query = query[::-1]
            tmp_trie = rev_trie
        else:
            tmp_trie = fow_trie

        cnt = 0
        for i, c in enumerate(query):
            if c == '?':
                if 'count' in tmp_trie:
                    cnt = tmp_trie['count'].get(len(query) - i, 0)
                break

            if c not in tmp_trie:
                break
            tmp_trie = tmp_trie[c]

        answer.append(cnt)

    return answer

class Trie:
    def __init__(self, val, depth=0):
        self.child = {}
        self.num = {}
        self.val = val
        self.depth = depth

    def push(self, word):
        node = self
        while len(word) > 0:
            node.num[len(word)] = node.num.get(len(word), 0) + 1
            if word[0] not in node.child:
                node.child[word[0]] = Trie(word[0], node.depth + 1)
            node = node.child[word[0]]
            word = word[1:]


    def search(self, word):
        node = self
        while len(word) > 0:
            if word[0] == '?':
                return node.num.get(len(word), 0)
            if word[0] not in node.child:
                return 0
            node = node.child[word[0]]
            word = word[1:]

    def __repr__(self):
        return 'num: {}; val: {};'.format(str(self.num), self.val)

def solution(words, queries):
    answer = []
    t1 = Trie('')
    t2 = Trie('')
    for word in words:
        t1.push(word)
        t2.push(word[::-1])

    for query in queries:
        if query[0] != '?':
            val = t1.search(query)
        else:
            val = t2.search(query[::-1])
        answer.append(val)
    return answer


class Node(object):
    def __init__(self, length = None):
        self.total_children = {}
        if length != None:
            self.total_children[length] = 1
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, s):
        curr_node = self.head
        if len(s) not in curr_node.total_children:
            curr_node.total_children[len(s)] = 1
        else:
            count = curr_node.total_children[len(s)]
            curr_node.total_children[len(s)] = count + 1

        for i in range(0, len(s)):
            suffix_length = len(s) - i - 1
            if s[i] not in curr_node.children:
                curr_node.children[s[i]] = Node(suffix_length)
                curr_node = curr_node.children[s[i]]
            else:
                curr_node = curr_node.children[s[i]]
                if suffix_length not in curr_node.total_children:
                    curr_node.total_children[suffix_length] = 1
                else:
                    count = curr_node.total_children[suffix_length]
                    curr_node.total_children[suffix_length] = count + 1

    def get_count_prefix(self, prefix, count_wildcard):
        curr_node = self.head
        for c in prefix:
            if c not in curr_node.children:
                return 0
            curr_node = curr_node.children[c]

        if count_wildcard not in curr_node.total_children:
            return 0
        else:
            return curr_node.total_children[count_wildcard]


def solution(words, queries):
    answer = []

    # Make trie
    forward_trie = Trie()
    reverse_trie = Trie()
    for word in words:
        forward_trie.insert(word)
        reverse_trie.insert(word[::-1])

    for query in queries:
        if query[-1] == '?':
            count_wildcard = len(query) - query.find('?')
            answer.append(forward_trie.get_count_prefix(query[:-count_wildcard], count_wildcard))
        else:
            count_wildcard = query.rfind('?') + 1
            answer.append(reverse_trie.get_count_prefix(query[count_wildcard:][::-1], count_wildcard))

    return answer

    
# 오답
# def solution(words, queries):
#     answer = []
#     cache = dict({'start': {}, 'end': {}})
#     for query in queries:
#         info = start_or_end(query)
#         if cache.get(info[2]).get(((info[0], info[1]))):
#             answer.append(len(cache.get(info[2]).get((info[0], info[1]))))
#         else:
            
#             temp = build_cache(info, words)
#             answer.append(len(temp.get((info[0], info[1]))))
#             cache.get(info[2]).update(temp)
#     return answer

# def start_or_end(word):
#     if word.startswith('?'):
#         return (word.replace('?', ''), len(word), 'start')
#     elif word.endswith('?'):
#         return (word.replace('?', ''), len(word), 'end')
    
# def build_cache(info, words):
#     temp = dict()
#     target = [w for w in words if len(w) == info[1]]
#     if info[2] == 'start':
#         for i in range(0, len(info[0])+1):
#             token = info[0][:i]
#             temp[(token, info[1])] = [word for word in target if word.endswith(token)]
#         return temp
#     else:
#         for i in range(0, len(info[0])+1):
#             token = info[0][:i]
#             temp[(token, info[1])] = [word for word in target if word.startswith(token)]
#         return temp

if __name__ == '__main__':
    solutionx(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])