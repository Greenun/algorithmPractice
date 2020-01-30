import sys

class Stack(object):
	def __init__(self):
		self.memory = []
	def push(self, x):
		self.memory.append(x)
	def pop(self, x):


if __name__ = '__main__':
	#stack : 1 2 3 4 5 6 7 8
	'''
	1 2 5 7 8

	4 3 6 8 7 5 2 1

	3 4 5
	1 2 5

	'''
	#4 3 6 8 7 5 2 1
	#1 2 5 3 4