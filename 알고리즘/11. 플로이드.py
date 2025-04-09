"""
모든 노드에서 다른 모든 노드까지 가는데 최소비용

다익스트라 : 한노드 -> 다른 모든 노드

https://www.acmicpc.net/problem/11404
"""

import sys
INF = sys.maxsize

n=int(input())
m=int(input())
rs=[[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    rs[i][i] = 0

for i in range(m):
    a,b,c = map(int, input().split())
    rs[a][b] = min(rs[a][b], c)

# j -> k -> i
for k in range(1,n+1): #거치는 값
    for j in range(1,n+1): #시작
        for i in range(1,n+1): #도착
            if rs[j][i] > rs[j][k] + rs[k][i]:
                rs[j][i] = rs[j][k] + rs[k][i]

for j in range(1,n+1): #시작
    for i in range(1,n+1): #도착
        if rs[j][i] == INF: print(0, end=' ')
        else: print(rs[j][i], end=' ')
    print()