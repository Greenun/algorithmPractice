def solution(dataSource, tags):
    from collections import defaultdict
    import heapq
    tag_map = defaultdict(list)
    doc_map = defaultdict(int)
    for data in dataSource:
        doc, doc_tags = data[0], data[1:]
        for tag in doc_tags:
            tag_map[tag].append(doc)
    for tag in tags:
        for doc in tag_map[tag]:
            doc_map[doc] += 1
    
    queue = list()
    result = list()
    for docs in doc_map:
        heapq.heappush(queue, (doc_map[docs]*-1, docs))
    top = 10 if len(queue) >= 10 else len(queue)
    
    for _ in range(top):
        _, document = heapq.heappop(queue)
        result.append(document)
    return result