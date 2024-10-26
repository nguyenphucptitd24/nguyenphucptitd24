t = int(input())
for i in range(t):
    n = int(input())
    s = n[::-1]
    if s == n:
        print ("YES")
    else:
        print ("NO")