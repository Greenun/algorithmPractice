# def solution(n):
#     length = 2**n - 1
#     papers = [0]
#     for i in range(2, n+1):
#         base = [0, 1] * (2**(i-2))
#         for idx, p in enumerate(papers):
#             base.insert(2*idx + 1, p)
#         papers = base
#     return papers

def solution(n):
    length = 2**n - 1
    papers = [list() for _ in range(n + 1)]
    papers[1] = [0]    
    for i in range(2, len(papers)):
        print(papers, i)
        temp = list(papers[i - 1])
        print(temp)
        temp[2**(i-2) - 1] = 1
        papers[i] = papers[i - 1] + [0] + papers[i - 2] + temp
    return papers[n]

if __name__ == '__main__':
	print(solution(3))
	print(solution(4))
	# print(solution(5))
	# print(solution(6))
	# [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
	# [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
	# [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1][0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
	# [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]