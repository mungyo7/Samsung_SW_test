arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

print("기존")
for i in range(len(arr)):
    print(arr[i])


def gravity(): #맨 위줄부터 1칸 아래랑 비교하면서 하강, 위에거도 함께 하강처리
    n = len(arr) #세로 길이 5
    m = len(arr[0]) #가로 길이 3
    for i in range(n - 1):
        for j in range(m):
            p = i
            # 현재칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야함
            while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0: #현재칸이 범위 안, 현재칸 1, 아래칸 0이면
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j] #현재칸이랑 아래칸 위치 바꿈(아래로 1칸 하강)
                p -= 1 


gravity()

print("변화")
for i in range(len(arr)):
    print(arr[i])
    
# =====
# 기존
# [0, 1, 0]
# [1, 0, 1]
# [0, 1, 0]
# [0, 0, 1]
# [0, 1, 0]
# 변화
# [0, 0, 0]
# [0, 0, 0]
# [0, 1, 0]
# [0, 1, 1]
# [1, 1, 1]