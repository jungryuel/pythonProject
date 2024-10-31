from itertools import combinations
# 조합 라이브러리 사용

vows = ['a', 'e', 'i', 'o', 'u']

def is_possible(word):
	global length, list, characters #전역변수 선언

	vow = 0
	for w in word:
		vow += (w in vows)
	con = length - vow

	return (vow >= 1 and con >= 2)

length, list = map(int, input().split())
arr = input().split()

arr.sort()

for word in combinations(arr, length):
	if is_possible(word):
		print(''.join(word))