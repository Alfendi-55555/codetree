n, m = map(int, input().split())

# Please write your code here.

def lcm(n,m):
    for i in range(2,n*m+1):
        if i%n == 0 and i%m == 0:
            n = i
            break

    print(n)

lcm(n,m)