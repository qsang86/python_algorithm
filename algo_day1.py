#what is algorithm?

#sequence search

#문제: 어떤 x가 n개의 수로 구성된 리스트 s에 존재하는가?
#해답: if x exists, index of x. if not, 0

#parameter: int n(>0), List S(1<index<n), 원소 x

#eg) s = [0, 10, 7, 11, 5, 13, 8], n=6, x=5
 #>>>>>>>>>location = 4#/

def seqSearch(len(S)-1, S, x):
	location = 1
	while(location <= n && S[location] !=n):
		location += 1
	if(location > n):
		location = 0
	return location

#List 원소 sum 
#quiz: n개의 원소를 가진 리스트 s 원소의 합
#ans: sum of all elements in List

#Sorting
#exchange sorting
#i번쨰 자리 수와 (i+1) 부터 nth 수 차례대로 비교
#주어진 자리 수가 i보다 작으면 교환

#efficiency of algorithm
#binary search vs sequence search
#if input list is not sorted > seq
#if sorted > binary

#binary search
#for the given S & x, compare x with S[mid]
#if x == S[mid], end. if x < S[mid], left search. 재귀호출
#if x > S[mid], right search

#binary search is more effcient than seq search

#FIBONACCI ALGORITHM
#if use recursive, ineffective siollll
#how to improve??
#>>>>store the already calculated ones into LIST

