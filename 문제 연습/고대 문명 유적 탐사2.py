"""
5*5 격자에서 3*3 항상 회전시켜야함
1. 유물 1차 가치 최대화
2. 회전한 각도 가장 작은거
3. 회전 중심 좌표의 열 가장 작은거, 행 가장작은거

조각 3개이상 연결 -> 유물 되어 사라짐 총 개수가 유물 가치

벽면 : 1~7 사이의 숫자 M개
- 새로운 조각
1. 열 번호가 작은 거 -> 행 번호 큰거

업데이트 된거에서 또 유물 생성 후 삭제 -> 업데이트 반복

K : 탐사 반복 횟수 1-10
M : 벽면의 유물 조각의 개수 10-300

구현 순서
1. 맵 만들기
2. 중심좌표 9개 순회하면서 각각의 유물 가치 계산
3. 가장 큰 유물 가치의 경우 구하고 같으면 우선순위에 따라 중심 좌표 및 유물 찾기
4. 유물 없애면서 total에 추가하고, 벽에서 왼쪽 아래부터 채워넣기
5. 업데이트 된 맵에서 다시 유물 확인 후 total 업데이트

2 20
7 6 7 6 7
6 7 6 7 6
6 7 1 5 4
7 6 3 2 1
5 4 3 2 7
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3

"""

K, M = map(int, input().split())
arr = [ list(map(int,input().split())) for _ in range (5)]
lst = list(map(int, input().split()))
ans=[]

def rotate(arr, si, sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si+3-j-1][sj+i]
    return narr

def bfs(arr, v, si, sj, clr):
    q=[]
    sset = set()
    cnt = 0

    q.append((si,sj))
    sset.add((si,sj))
    v[si][sj] = 1
    cnt+=1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0,-1),(0,1),(1,0),(-1,0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and arr[ni][nj]==arr[ci][cj]:
                v[ni][nj]=1
                q.append((ni,nj))
                sset.add((ni,nj))
                cnt+=1

    if cnt >=3:
        if clr ==1:
            for i,j in sset:
                arr[i][j]=0
        return cnt
    else:
        return 0


def count_clear(arr, clr):
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                temp = bfs(arr, v, i, j, clr)
                cnt += temp
    return cnt

for _ in range(K):
    max_total = 0
    max_arr = []
    for rot in range(1,4):
        for j in range(3):
            for i in range(3):
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, i, j)

                t = count_clear(narr, 0) # clear까지
                if t > max_total:
                    max_arr = narr
                    max_total = t

    # 이제 최대 유물 값 구했음, 최대일 때의 max_arr 구했음
    if max_total == 0:
        break

    cnt = 0
    arr = max_arr


    while True:
        t = count_clear(arr, 1)
        if t==0:
            break
        cnt += t
        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)

    ans.append(cnt)

print(*ans)