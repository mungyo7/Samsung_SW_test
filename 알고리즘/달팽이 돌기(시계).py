
N=5

tdi = [-1,0,1,0]
tdj = [0,1,0,-1]

mx_cnt,cnt,flag = 1,0,0
M=(N+1)//2
ti,tj,td=M,M,0

tarr = [[0]*(N+2) for _ in range(N+2)]

for k in range(1,22):
    cnt+=1
    tarr[ti][tj]=k
    ti,tj=ti+tdi[td],tj+tdj[td]
    if cnt == mx_cnt:
        cnt=0
        td=(td+1)%4
        if flag ==0:
            flag=1
        else:
            flag=0
            mx_cnt+=1

for i in tarr:
    print(i)