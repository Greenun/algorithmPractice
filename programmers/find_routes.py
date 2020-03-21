def solution(nodeinfo):
    import heapq
    # python recursion limit.. set
    import sys
    sys.setrecursionlimit(10**6)
    node_info = list()
    for i, ni in enumerate(nodeinfo):
        heapq.heappush(node_info, (-1*ni[1], (i + 1, ni)))
    _, (idx, rn_info) = heapq.heappop(node_info)
    root = Node(rn_info[0], rn_info[1], idx)
    for _ in range(len(node_info)):
        _, (idx, n_info) = heapq.heappop(node_info)
        new_node = Node(n_info[0], n_info[1], idx)
        push(root, new_node)
    
    post_result, pre_result = list(), list()
    preorder(root, pre_result)
    postorder(root, post_result)
    return [pre_result, post_result]

class Node(object):
    def __init__(self, x, y, i):
        self.point = (x, y)
        self.number = i
        self.left = None
        self.right = None

def push(root, node):
    current = root
    nx, ny = node.point
    while current:
        cx, cy = current.point
        if cx > nx:
            if not current.left:
                current.left = node
                return
            current = current.left
        else:
            if not current.right:
                current.right = node
                return
            current = current.right
    
def preorder(node, result):
    if not node:
        return
    result.append(node.number)
    preorder(node.left, result)
    preorder(node.right, result)

def postorder(node, result):
    if not node:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.number)