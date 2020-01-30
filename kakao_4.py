# 예시
def count_leaf(tmp_trie, depth):
    space = [(tmp_trie, k, depth) for k in tmp_trie.keys()]

    cnt = 0
    while len(space) > 0:
        tmp_trie, k, depth = space[0]
        space = space[1:]

        if depth == 0 and k == '@@@':
            cnt += 1
            #print(tmp_trie)
            continue

        if depth > 0 and k != '@@@':
            space.extend([(tmp_trie[k], new_k, depth-1) for new_k in tmp_trie[k].keys() if type(tmp_trie)])

    return cnt

def solution(words, queries):
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
# 오답
def solution(words, queries):
    answer = []
    cache = dict({'start': {}, 'end': {}})
    for query in queries:
        info = start_or_end(query)
        if cache.get(info[2]).get(((info[0], info[1]))):
            answer.append(len(cache.get(info[2]).get((info[0], info[1]))))
        else:
            
            temp = build_cache(info, words)
            answer.append(len(temp.get((info[0], info[1]))))
            cache.get(info[2]).update(temp)
    return answer

def start_or_end(word):
    if word.startswith('?'):
        return (word.replace('?', ''), len(word), 'start')
    elif word.endswith('?'):
        return (word.replace('?', ''), len(word), 'end')
    
def build_cache(info, words):
    temp = dict()
    target = [w for w in words if len(w) == info[1]]
    if info[2] == 'start':
        for i in range(0, len(info[0])+1):
            token = info[0][:i]
            temp[(token, info[1])] = [word for word in target if word.endswith(token)]
        return temp
    else:
        for i in range(0, len(info[0])+1):
            token = info[0][:i]
            temp[(token, info[1])] = [word for word in target if word.startswith(token)]
        return temp