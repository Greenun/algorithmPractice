def solution(words, queries):
    word_map = Trie()
    reversed_word_map = Trie()
    for word in words:
        word_map.insert(word)
        reversed_word_map.insert(word[::-1])
    result = list()
    for query in queries:
        if query.startswith('?'):
            result.append(reversed_word_map.search(query[::-1]))
        elif query.endswith('?'):
            result.append(word_map.search(query))
    
    return result

class Node(object):
    def __init__(self, value, end=False):
        self.value = value
        self.children = list()
        self.end = end

    def add_child(self, node):
        self.children.append(node)
        
class Trie(object):
    def __init__(self):
        self.root = Node('')
    
    def insert(self, string):
        current = self.root
        for i in range(len(string)):
            if not current.children:
                new_node = Node(string[i]) if not i == len(string)-1 else Node(string[i], True)
                current.add_child(new_node)
                current = new_node
            else:
                for child in current.children:
                    if child.value == string[i]:
                        if i == len(string) - 1:
                        	child.end = True
                        current = child
                        break
                    else:
                    	if current.children[-1] == child:
	                        new_node = Node(string[i]) if not i == len(string)-1 else Node(string[i], True)
	                        current.add_child(new_node)
	                        current = new_node

    def search(self, string):
    	current = self.root
    	for i in range(len(string)):
    		if string[i] == '?':
    			break
    		for child in current.children:
    			if child.value == string[i]:
    				current = child
    				break
    			# else:
    			# 	return 0
    	# count leaf nodes
    	it = string.count('?')
    	queue = list(current.children)
    	for i in range(it-1):
    		temp = list()
    		while queue:
    			current = queue.pop(0)
    			temp += current.children
    		queue += temp
    	result = list()
    	for q in queue:
    		if q.end:
    			result.append(q)
    	return len(result)

    def travel(self):
    	current = self.root
    	stack = list(current.children)
    	while stack:
    		current = stack.pop()
    		print(current.value, current.end)
    		for child in current.children:
    			stack.append(child)

    def queue_travel(self):
   		current = self.root
   		queue = list(current.children)
   		while queue:
   			current = queue.pop(0)
   			print(current.value)
   			for child in current.children:
   				queue.append(child)

if __name__ == '__main__':
	# t = Trie()
	# t.insert("what")
	# t.insert('wac')
	# t.insert('abc')
	# t.travel()
	# for x in ["frodo", "front", "frost", "frozen", "frame", "kakao"]:
	# 	t.insert(x)
	# t.travel()
	# print(t.search('fro??'))
	# print(t.search('fr???'))
	# print(t.search('fro???'))
	# print(t.search('pro??'))

	# print('-----')
	# t.queue_travel()

	# x = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
	# print(x)
	y = solution(["fucking", "shiting", "shit", "fuckyou"], ['fu????', "sh??", "sh?????", "???????", "????ing"])
	print(y)