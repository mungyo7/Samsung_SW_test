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
"""

K, M = map(int, input().split())
arr = [ list(map(int,input().split())) for _ in range (5)]
lst = list(map(int, input().split()))
ans=[]

# rotate 함수 외우기@@
def rotate(arr, si, sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j]=arr[si+3-j-1][sj+i]
    # arr_90 = list(map(list,zip(*narr[::-1])))
    return narr

def bfs(arr,v,si,sj,clr):
    q=[]
    sset = set()
    cnt =0

    q.append((si,sj))
    v[si][sj]=1
    sset.add((si,sj))
    cnt+=1

    while q:
        ci,cj=q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0 and arr[ci][cj]==arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = 1
                sset.add((ni,nj))
                cnt+=1
    if cnt>=3:
        if clr == 1:
            for i,j in sset:
                arr[i][j]=0
        return cnt
    else:
        return 0
def count_clear(arr, clr): #clr == 1이면 3개이상의 값 0으로 클리어
    v=[[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                t =bfs(arr,v,i,j,clr)
                cnt += t
    return cnt

#방향 4방향 -> 2,2 부터 반복
for _ in range(K): #k턴 진행, 유물 없으면 즉시 종료
    mx_cnt = 0
    for rot in range(1,4): #회전수
        for sj in range(3): #열
            for si in range(3): #행
                #rot 만큼 90도 시계방향 회전
                narr = [x[:] for x in arr] #copy
                for _ in range(rot): #rot 만큼 회전
                    narr = rotate(narr, si, sj)

                #유물 개수 카운트
                t = count_clear(narr,0)
                if mx_cnt < t:
                    mx_cnt = t
                    marr = narr

    #유물 없으면 즉시 종료
    if mx_cnt == 0:
        break

    #[2] 연쇄획득
    cnt = 0
    arr = marr
    while True:
        t = count_clear(arr, 1)
        if t==0:
            break # 연쇄획득 종료 -> 다음턴으로
        cnt += t # 획득한 유물 개수 누적

        for j in range (5):
            for i in range(4,-1,-1):
                if arr[i][j] == 0:
                    arr[i][j]=lst.pop(0)

    ans.append(cnt) # 이번턴 연쇄획득 개수 추가

print(*ans)