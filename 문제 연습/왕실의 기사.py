import sys

from PIL.Image import radial_gradient

sys.stdin=open("input.txt","r")

"""
L : 체스판 크기
N : 기사 개수
Q : 왕의 명령 개수(턴 수)

- L*L 체스판 
    0: 빈칸
    1 : 함정
    2 : 벽
    
- 기사
    (r,c) : 기사 처음 위치
    h, w : 직사각형 세로 가로
    k : 초기 체력
    기사 처음 위치는 서로 겹치치 않고, 벽과 겹치지 않음
    
-왕의 명령
    (i,d) : i번째 기사 방향 d로 한칸 움직여라
    1<=i<=N
    이미 사라진 기사 번호가 명령으로 주어질 수 있음
    d : 상 우 하  좌
        0  1  2  3
    
- 출력 : Q개의 명령이 진행된 후 생존한 기사들이 총 받은 데미지의 합
=============================================================
chess_arr : 체스판
unit_arr : 기사들 위치 판

"""
INF = 9
L,N,Q = map(int,input().split())
chess_arr = [[INF]*(L+2)]+[[INF]+list(map(int,input().split()))+[INF] for _ in range(L)]+[[INF]*(L+2)]
unit_data = {}
unit_arr = [[0]*(L+2) for _ in range(L+2)]
unit_health = [-9999]*(N+1) # 기사들 체력

for i in range(1,N+1): # 초기 기사 위치 arr 만들기
    r,c,h,w,k = map(int,input().split())
    for x in range(r,r+h):
        for y in range(c,c+w):
            unit_arr[x][y]=i
    unit_data[i] = (r,c,h,w)
    unit_health[i] = k
unit_health_initial = unit_health[:]
order_data=[]
for j in range(1,Q+1):
    i,d = map(int,input().split())
    order_data.append((i,d))

# print(L,N,Q)
# print("[chess_arr]")
# for i in chess_arr:
#     print(i)

# print(unit_data)
# print("[unit_arr]")
# for i in unit_arr:
#     print(i)
# print(order_data)
# print(unit_health)

"""
[1] 명령에 따라 기사 이동

def check_next_blank() : 기사 번호, 방향 넣으면 이동한곳이 모두 빈칸인지 확인 후 0,1 반환

[1-1] 다음 칸 빈칸이라 바로 이동하고 끝
dr따라 한칸 이동한 좌표가 벽이아니고(arr값이 0또는 1이고), unit_arr의 다음 좌표가 모두 0또는 자신의 번호이면 -> 이동

if unit_arr[ni][nj] == 0 or unit_arr[ni][nj]==i:    # 다음칸이 빈칸이거나 자기자신의 위치였다면(이동 가능)

[1-2] 기사 붙어있어서 모두 함께 한칸 이동
dr따라 한칸 이동한 좌표가 벽이아니고(arr값이 0또는 1이고), unit_arr의 다음 좌표 중 하나라도 자신의 번호가 아닌 다른 양수면 
-> 해당 번호 리스트에 저장 -> 리스트의 번호에서 다시 확인, , 또 겹치면 또 리스트넣고 확인 -> 최종 check_next_blank 값이 모두 1이면 모두 이동


[1-2] 벽에 막혀서 이동 x
계속 확인하다가 다음 좌표가 하나라도 벽이있으면 이동 x

[2] 이동 후 함정 위치 확인 후 체력 업데이트

[3] 모든 턴 끝나면 체력이 0보다 큰 기사의 처음 체력과의 차이값 비교 후 더하기

"""

di = [-1,0,1,0]
dj = [0,1,0,-1]
for i,d in order_data: # 턴 수만큼 반복 // 기사번호 i 를 d 방향으로 한칸 이동
    overlap_list=[]
    overlap_list_final=[]
    overlap_list.append(i)
    next_wall = False

    while overlap_list:
        i = overlap_list.pop(0)
        overlap_list_final.append(i)
        for x in range(1,L+1):
            for y in range(1,L+1):
                if unit_arr[x][y] == i:
                    ci, cj = x, y
                    ni, nj = ci+di[d], cj+dj[d]
                    if chess_arr[ni][nj] != INF and chess_arr[ni][nj] != 2: # 체스판에서 다음 칸이 벽이나 범위 밖이 아니면
                        if unit_arr[ni][nj] != 0 and  unit_arr[ni][nj] != i:    # 다음칸이 다른 기사와 겹칠 때
                            overlap_list.append(unit_arr[ni][nj])               # 겹치는 기사 리스트에 넣음
                                                               
                    else: # 다음 칸 벽
                        next_wall=True
                        break
    # print(overlap_list_final)
    narr = [x[:] for x in unit_arr]
    if next_wall == False: # 이동경로에 벽이 없으면 이동 후 체력 업데이트
        for x in range(1,L+1):
            for y in range(1,L+1):
                if unit_arr[x][y] in overlap_list_final:
                    ni, nj = x + di[d], y + dj[d]
                    if 1<=ni<=L and 1<=nj<=L:
                        narr[x][y]=0

        for x in range(1,L+1):
            for y in range(1,L+1):
                if unit_arr[x][y] in overlap_list_final:
                    ni, nj = x + di[d], y + dj[d]
                    if 1 <= ni <= L and 1 <= nj <= L:
                        narr[ni][nj]=unit_arr[x][y]
                        if chess_arr[ni][nj] == 1 and (unit_arr[x][y] in overlap_list_final[1:]):
                            unit_health[unit_arr[x][y]] -=1
        for x in range(1,L+1):
            for y in range(1,L+1):
                if unit_health[narr[x][y]] <= 0:
                    narr[x][y] = 0
    # for i in narr:
    #     print(i)
    # print(f'health : {unit_health}')
    unit_arr=narr

# print(unit_health_initial)
answer =0
for i in range(1,N+1):
    if unit_health[i] > 0:
        # print(unit_health_initial[i],unit_health[i])
        answer += (unit_health_initial[i]-unit_health[i])

print(answer)


                    