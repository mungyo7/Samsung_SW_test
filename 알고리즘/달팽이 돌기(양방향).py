N,M,H,K=map(int,input().split())

#상우하좌 이동
tdi=[-1,0,1,0]
tdj=[0,1,0,-1]

#필요한 변수
mx_cnt,cnt,flag,val=1,0,0,1

#중앙좌표
M=(N+1)//2

#시작좌표(중앙), 시작 방향(위쪽)
ti,tj,td=M,M,0

#테두리 감싼 N*N 배열
tarr=[[0]*(N+2) for _ in range(N+2)]

for k in range(1,100):
    cnt+=1
    tarr[ti][tj]=k
    ti,tj=ti+tdi[td], tj+tdj[td]
    
    if (ti,tj) == (1,1):
        mx_cnt,cnt,flag,val=N,1,1,-1
        td=2
    elif (ti,tj) == (M,M):
        mx_cnt,cnt,flag,val=1,0,0,1
        td=0

    if cnt==mx_cnt:
        cnt=0
        td=(td+val)%4
        if flag==0:
            flag=1
        else:
            flag=0
            mx_cnt+=val

