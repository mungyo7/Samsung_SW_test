"""
4 4
1 3 3 3
3 1 0 3 1 0 2 2
0 0 0 0
0 0 0 0
0 0 1 1
1 0 0 0

6 4
3 1 1 2
3 5 1 4 0 4 1 3
0 0 0 0 1 0
0 1 0 0 1 1
1 1 0 0 0 0
0 0 1 0 1 1
0 0 0 0 0 0
0 0 0 0 1 1

9 3
3 1 1 2
4 2 4 4 6 6
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""
import sys
sys.stdin=open("input.txt","r")

N, M = map(int, input().split()) # N : 마을의 크기, M : 전사의 수
smi, smj, emi, emj = map(int, input().split()) # 메두사 시작, 끝 좌표
men = list(map(int,input().split()))
arr = [ list(map(int,input().split())) for _ in range(N) ]

men_list=[] # 전사들 초기 위치 좌표 리스트
for i in range(len(men)//2):
    men_list.append((men[2*i],men[2*i+1]))
print(men_list)
def get_route(arr,smi,smj,emi,emj):
    q=[]
    v=[[0]*N for _ in range(N)]
    route=[]
    q.append((smi,smj))
    while q:
        cmi, cmj = q.pop(0)
        if (cmi, cmj) == (emi,emj):
            break
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우
            nmi, nmj = cmi + di, cmj + dj
            if 0<=nmi<N and 0<=nmj<N and v[nmi][nmj]==0:
                if arr[nmi][nmj]==0:
                    v[nmi][nmj] = cmi, cmj
                    q.append((nmi,nmj))
    ti, tj = v[emi][emj]
    while (ti,tj) != (smi,smj):
        route.append((ti,tj))
        ti, tj = v[ti][tj]

    return route[::-1]

# [1] 메두사 이동 -> 상하좌우 방향 우선순위
m_route_list = get_route(arr,smi,smj,emi,emj) # m_route_list : 메두사 이동 경로 좌표@@

# print(m_route_list)

# [2] 메두사 시선
"""
시선 arr 새로 만들어서 활성화 : 1, 가려진곳: 2, 상관없는 곳 :0
1. 시선 방향으로 일직선 탐색하면서 1표시 -> 전사 만나면 거기부터는 2표시 -> 범위 벗어나면 끝
    - 2표시 된곳 만나면 종료
2. 한칸씩 왼쪽 대각선 이동 -> 해당 줄 확인
    - 전사 있으면 전사 좌표 저장 -> 거기부터 해당 줄 2 표시
    - 전사 좌표에서 대각선으로 한칸씩 이동하며 해당 좌표부터 아래로 쭉 2 표시

8 방향 좌표 di dj 만들기

상 하 좌 우 우선순위
"""
# 상 상우 우 우하 하 하좌 좌 좌상
"""
7 0 1 
6   2
5 4 3
"""
dr_i = [-1,-1,0,1,1,1,0,-1]
dr_j = [0,1,1,1,0,-1,-1,-1]
marr = [[0]*N for _ in range(N)]
for (x,y) in men_list:
    marr[x][y] += 1
print("\n[marr]")
for i in marr:
    print(i)



# print("\n[sight_arr]")
# for i in sight_arr:
#     print(i)

flag = 0 # 기본은 0, 전사 만나면 1로 바뀜
# m_route_list=[(0,4)]
for mi, mj in m_route_list: # (mi,mj) 현재 메두사 좌표
    max_cnt = 0
    max_list=[]
    for idx in (0,4,6,2): # 상 하 좌 우
        cnt=0
        di,dj = dr_i[idx], dr_j[idx]
        nmi, nmj = mi+di, mj+dj
        mx_stone = 0
        sight_arr = [[0] * N for _ in range(N)]
        ti, tj = 0,0
        nmarr=[x[:] for x in marr]
        while (0<=nmi<N and 0<=nmj<N):
            if marr[nmi][nmj] > 0 and flag==0: # 전사 만나면 flag 1로 바꿈
                flag = 1
                mx_stone += 1


            if flag == 0: # 아직 전사 안만남
                sight_arr[nmi][nmj] = 1
                nmi = nmi+di
                nmj = nmj+dj
            else: # 전사 뒤쪽
                if marr[nmi][nmj] > 0:
                    sight_arr[nmi][nmj] = 1
                    nmarr[nmi][nmj] -= 1
                else:
                    sight_arr[nmi][nmj] = 2
                nmi = nmi + di
                nmj = nmj + dj
            # print('d')
        flag = 0

        # print(f'\n(mi,mj) : ({mi},{mj}) dr : {di},{dj}, mx_stone : {mx_stone}')
        # print("[sight_arr]")
        # for i in sight_arr:
        #     print(i)

        for idx2 in ((idx+1)%8, (idx-1)%8): # 상 하 좌 우
            di2, dj2 = dr_i[idx2], dr_j[idx2] # 대각선 이동 방향
            tlist = [] # 시야의 전사 원점 좌표
            for mul in range(1,N+1):
                nmi, nmj = mi + di2*mul, mj + dj2*mul # 메두사 대각선 좌표
                flag2 = 0
                flag = 0
                while (0 <= nmi < N and 0 <= nmj < N):
                    if marr[nmi][nmj] > 0 and flag == 0:  # 전사 만나면 flag 1로 바꿈
                        flag = 1
                        mx_stone += 1
                        ti, tj = nmi, nmj  # 대각선 원점

                        while (0 <= ti < N and 0 <= tj < N):
                            tlist.append((ti,tj))
                            ti, tj = ti + di2, tj + dj2  # 메두사 대각선 좌표

                    if (nmi, nmj) in tlist: # 대각선 라인에 있으면 flag 1로 바꿈
                        flag = 1

                    if flag == 0:  # 아직 전사 안만남 아무것도 없으면 기존 방향 일자 탐색
                        sight_arr[nmi][nmj] = 1
                        nmi = nmi + di
                        nmj = nmj + dj
                    elif flag == 1 and flag2==0:  # 시선 라인의 첫 전사
                        if marr[nmi][nmj] > 0: # 전사 뒤쪽은 전사 있어도 2표시
                            sight_arr[nmi][nmj] = 1
                            nmarr[nmi][nmj]-=1
                            flag2=1 #flag2가 1이면 무조건 2
                        else:
                            sight_arr[nmi][nmj] = 2
                        nmi = nmi + di
                        nmj = nmj + dj
                    else:
                        sight_arr[nmi][nmj] = 2
                        nmi = nmi + di
                        nmj = nmj + dj
                    # print('d')
            flag = 0
        if mx_stone>max_cnt:
            max_cnt=mx_stone
            max_list.append((di,dj,mx_stone))


        print(f'\n(mi,mj) : ({mi},{mj}) dr : {di},{dj}, mx_stone : {mx_stone}, mx_cnt : {max_cnt}')
        print(tlist)
        print("[sight_arr]")
        for i in sight_arr:
            print(i)
        print("[nmarr]")
        for i in nmarr:
            print(i)
    print(f'max_cnt : {max_cnt}')