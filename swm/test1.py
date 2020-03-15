# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n = int(sys.stdin.readline().replace('\n', ''))
remainder = n % 2 
quotient = n // 2
if remainder:
	number_str = '7'
else:
	number_str = '1'
for _ in range(1, quotient):
	number_str += '1'
print(int(number_str))
