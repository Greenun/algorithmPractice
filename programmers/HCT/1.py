def solution(n, delivery):
    deliver_map = dict()
    delivered, not_delivered = list(), list()
    for d in delivery:
        if d[2] == 1:
            delivered.append(d)
        else:
            not_delivered.append(d)
    for d in delivered:
        item_1, item_2, _ = d
        deliver_map[item_1] = "O"
        deliver_map[item_2] = "O"
    
    for nd in not_delivered:
        item_1, item_2, _ = nd
        stock_1 = deliver_map.get(item_1)
        stock_2 = deliver_map.get(item_2)
        if stock_1 == "O":
            deliver_map[item_2] = "X"
        elif stock_2 == "O":
            deliver_map[item_1] = "X"
    result = ""
    for i in range(1, n+1):
        r = deliver_map.get(i)
        if r:
            result += r
        else:
            result += "?"
    return result