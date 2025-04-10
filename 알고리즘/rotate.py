arr = [[1, 2, 3, 4,5], [6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for i in arr:
    print(i)
print()
## zip

# # 시계 방향 90 (= 반시계 방향 270)
# arr_90 = list(map(list,zip(*arr[::-1])))
# for i in arr_90:
#     print(i)
# print()
#
# # 시계 방향 180 (= 반시계 방향 180)
# arr_180 = [arr2[::-1] for arr2 in arr[::-1]]
# for i in arr_180:
#     print(i)
# print()
#
# # 시계 방향 270 (= 반시계 방향 90)
# arr_270 = list(map(list, zip(*arr)))[::-1]
# for i in arr_270:
#     print(i)

def rotate(arr, si, sj):
    narr = [x[:] for x in arr]
    for i in range(5): # 돌리는 가로세로개수 N
        for j in range(5):
            narr[si+i][sj+j]=arr[si+5-j-1][sj+i] # si+N-j-1, sj+i
    return narr

arr_new = rotate(arr,0,0) # si sj : 왼쪽 위 모서리 좌표
for i in arr_new:
    print(i)