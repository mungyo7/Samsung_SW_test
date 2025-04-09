"""
한 노드에서 다른 모든 노드까지 가는데 최소비용

https://www.acmicpc.net/problem/1753

다익스트라 코드는 외우기!!!!!!!!@!@!@!@!@!@!@!
"""
import heapq

V, E = map(int, input().split())
K = int(input())
edge = [ [] for _ in range(V+1)]
dist = [10000] * (V+1)

for i in range(E):
    u,v,w = map(int,input().split())
    edge[u].append([w,v])


dist[K] = 0

heap = [[0,K]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv],nv])

for i in range(1, V+1):
    if dist[i] == 10000: print('INF')
    else: print(dist[i])