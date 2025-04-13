a=[(1,2,'R',5),(4,3,'B',3),(1,6,'R',9),(2,5,'G',22)]

a.sort(key=lambda a: (-a[3]))
print(a)