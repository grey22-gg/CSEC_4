n = int(input())
a = 0
for i in range(n):
    P,V,T = map(int, input().split())
    if P and V or P and T or V and T == 1:
        a += 1

print(a)
