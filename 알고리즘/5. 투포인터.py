"""
각 원소마다 모든 값을 순회해야할 떄

https://www.acmicpc.net/problem/2559



"""

N, K = map(int, input().split())
nums = list(map(int, input().split()))

sum = 0
maxv = 0 

for i in range(K):
    sum += nums[i]

maxv = sum

for j in range(K,N):
    sum += nums[j]
    sum -= nums[j-K]
    maxv = max(maxv,sum)


print(maxv)