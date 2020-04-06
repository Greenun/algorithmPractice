def solution(snapshots, transactions):
    from collections import defaultdict
    transaction_map = dict()
    snapshots_map = defaultdict(int)
    for snapshot in snapshots:
        dest, budget = snapshot
        snapshots_map[dest] = int(budget)
    for transaction in transactions:
        idx, action, dest, value = transaction
        if transaction_map.get(idx):
            continue
        transaction_map[idx] = (action, dest, value)
    
    for action, dest, value in transaction_map.values():
        if action == "SAVE":
            snapshots_map[dest] += int(value)
        else:
            snapshots_map[dest] -= int(value)
    
    return [[x, str(snapshots_map[x])] for x in snapshots_map]