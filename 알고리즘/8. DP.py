"""
Dynamic Programming

이전의 값을 재활용

점화식 구하기!

https://www.acmicpc.net/problem/11726
"""

n = int(input())
rs = [0,1,2]

for i in range(3,n+1):
    rs.append(rs[i-1]+rs[i-2] % 10007)

print(rs[n])