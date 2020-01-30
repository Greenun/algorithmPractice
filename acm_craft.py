import sys

if __name__ == '__main__':
	num_case = int(sys.stdin.readline())
	nums = sys.stdin.readline().replace("\n", "").split(' ')
	
	num_build = int(nums[0])
	num_route = int(nums[1])

	build_times = sys.stdin.readline().replace("\n", "").split(' ')
	techs = list()
	for i in range(0, num_route):
		tech = sys.stdin.readline().replace("\n", "").split(' ')
		techs.append(tech)

	final_build = int(sys.stdin.readline())

	total_time = int(build_times[final_build - 1])#last one
	'''
	마지막 건물로부터 역으로 추적 -- 필요한 것들 중 가장 느린 것..?
	처음 건물부터 시작 -- 테이블 --> X
	1 - 2 - 4
		  - 5 - 7
	  - 3 - 6 - 7 - 8
	'''

	


	