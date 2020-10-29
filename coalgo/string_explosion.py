import sys

def solution(origin, explode):
	stack = list()
	length = len(explode)
	s_len = 0
	for o in origin:
		if s_len >= length:
			if all([stack[j] == explode[j] for j in range(-1, -1*length-1, -1)]):
				for _ in range(length):
					stack.pop()
				s_len -= length
		stack.append(o)
		s_len += 1
	if s_len >= length:
		if all([stack[j] == explode[j] for j in range(-1, -1*length-1, -1)]):
			stack = stack[:-1*length]
			s_len -= length
	if not stack:
		return "FRULA"
	return ''.join(stack)

if __name__ == '__main__':
	origin = sys.stdin.readline().replace("\n", "")
	explode = sys.stdin.readline().replace("\n", "")
	print(solution(origin, explode))