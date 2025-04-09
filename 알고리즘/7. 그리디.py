"""
현재 차례의 최고의 답을 찾는 문제


https://www.acmicpc.net/problem/11047
"""

N, K = map(int, input().split())

coins = [ int(input()) for _ in range(N)]

coins.reverse()
cnt =0 

for i in coins:
    cnt += K // i
    K = K % i

print(cnt)