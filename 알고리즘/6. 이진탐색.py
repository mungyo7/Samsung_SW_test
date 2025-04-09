"""
정렬되어있을 떄 숫자를 찾을 떄 편함

N개의 수를 정렬 -> O(N*longN)

경우의수가 2억보다 작아야함 -> 파이썬


https://www.acmicpc.net/problem/1920
"""
# 외우기!!!!
# def search(st, en, target): 시작 index, 끝 inde, 찾으려는 숫자
#     if st==en:
#         #
#         return
    
#     mid = (st+en)//2
#     if nums[mid] < target:
#         search(mid+1,en,target)
#     else:
#         search(st,mid,target)


M=int(input())
nums=list(map(int,input().split()))
N=int(input())
target_list=list(map(int,input().split()))

nums.sort()

def search(st, en, target):
    if st==en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    
    mid = (st+en)//2

    if nums[mid] < target:
        search(mid+1,en,target)
    else:
        search(st,mid,target)

for i in target_list:
    search(0,N-1,i)