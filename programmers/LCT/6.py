def solution(directory, command):
    import heapq
    ns_tree = dict()
    ns_tree[""] = dict()
    for d in directory[1:]:
        path = d.split('/')
        current = ns_tree
        for p in path:
            if isinstance(current.get(p), dict):
                current = current[p]
            else:
                current[p] = dict()
    # print(ns_tree)
    for cmd in command:
        # print("zz, ", ns_tree)
        line = cmd.split(' ')
        if line[0] == "mkdir" or line[0] == "rm":
            dest = line[1]
            if line[0] == "mkdir":
                ns_tree = mkdir(ns_tree, dest)
            else:
                ns_tree = rmdir(ns_tree, dest)
        else:
            # cp
            src, dest = line[1:]
            ns_tree = cp(ns_tree, src, dest)
    result = get_path(ns_tree, "", [])
    return result
    
def mkdir(ns_tree, path):
    current = ns_tree
    path = path.split('/')
    for p in path[:-1]:
        current = current[p]
    current[path[-1]] = dict()
    return ns_tree

def rmdir(ns_tree, path):
    current = ns_tree
    path = path.split('/')
    for p in path[:-1]:
        current = current[p]
    current.pop(path[-1])
    return ns_tree

def cp(ns_tree, src, dest):
    from copy import deepcopy
    current = ns_tree
    src = src.split('/')
    if dest == "/":
        dest = [""]
    else:
        dest = dest.split('/')
    for p in src:
        current = current[p]
    copy_dir = deepcopy(current)
    current = ns_tree
    for p in dest:
        current = current[p]
    current[src[-1]] = copy_dir
    return ns_tree

def get_path(ns_tree, parent, result):
    for key in sorted(ns_tree.keys()):
        result.append((parent + "/" + key).replace("//", "/"))
        current = ns_tree[key]
        result = get_path(current, parent + "/" + key, result)
    return result