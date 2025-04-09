N, M = map(int, input().split())
map = [ list(map(int, input().split())) for _ in range(N)]

maxv = 0
rst = 0

for i in range(N-1):
    for j in range(N-1):
        rst = map[j][i] + map[j+1][i] + map[j][i+1] + map[j+1][i+1]
        # print(rst)
        maxv = max(rst, maxv)

print(maxv)