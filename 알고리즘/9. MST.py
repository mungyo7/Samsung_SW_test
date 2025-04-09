"""
Minimum Spanning Tree

모든 노드가 연결된 트리

MST:최소의 비용으로 모든 노드가 연결된 트리

1. 전체 간선 중 작은것부터 연결
2. 현재 연결된 트리에 이어진 간선중 가장 작은것을 추가
    -heap 사용


https://www.acmicpc.net/problem/1197

최소스패닝 기본문제 -> 외우기!@@@@@@@@@@@@@@@@@@@
O(E*logE)
"""
import heapq

V, E = map(int, input().split())
edge = [ [] for _ in range(V+1)]
chk = [False] * (V+1)
rs=0

for i in range(E):
    a,b,c = map(int,input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])


heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)


