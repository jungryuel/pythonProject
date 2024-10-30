from itertools import combinations
# 조합 순열 라이브러리 itertools

while True:
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]
	if k == 0:
		break

# 아래와 같이 combinations를 선언해주고 사용
	for comb in combinations(arr, 6): # (arr는 배열 , 6은 뽑을 갯수를 의미 배열 내에서 6개의 조합을 찾아내 리턴)
		for u in comb:
			print(u, end=' ')
		print()
	print()