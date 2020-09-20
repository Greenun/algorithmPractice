def solution(n):
    # 으아 너무 구리다...
    matrix = [[] for _ in range(n)]
    whole = (n*(n+1))//2
    start = 1
    cycle = 0
    temp = n
    while whole >= start:
        if whole == start:
            matrix[2*cycle].insert(cycle, start)
            break
        # temp
        # print(start, matrix, "--1")
        for i in range(2*cycle, n - cycle - 1):
            matrix[i].insert(cycle, start+i - 2*cycle)
        start += n - 3*cycle - 1 
        
        # print(start, matrix, "--2")
        for i in range(0, temp):
            matrix[-1 - cycle].insert(cycle+i, start+i)
        start += temp
        
        # print(start, matrix, "--3")
        for i in range(len(matrix)-2-cycle, 2*cycle, -1):
            matrix[i].insert(len(matrix[i])-cycle, start + len(matrix)-2-cycle - i)
        start += len(matrix)-2-3*cycle # temp - 2 - cycle
        
        cycle += 1
        # whole -= start
        temp -= 3
    #     print(start, matrix)
    # print(start, matrix)
    result = list()
    for line in matrix:
        result.extend(line)
    return result
