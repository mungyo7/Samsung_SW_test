arr = [[1, 2, 3, 4,5,99], [6,7,8,9,10,99],[11,12,13,14,15,99],[16,17,18,19,20,99],[21,22,23,24,25,99]]
for i in arr:
    print(i)
print()

def rotate_90(arr):
    m=len(arr)
    n=len(arr[0])
    result=[[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m-i-1] = arr[i][j]
    
    return result

for _ in range(3):
    arr = rotate_90(arr)
for i in arr:
    print(i)