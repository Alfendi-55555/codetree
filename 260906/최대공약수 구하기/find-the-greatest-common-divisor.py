n, m = map(int, input().split())

# Please write your code here.

def choi(a,b):
    n = 0
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            n = i

    print(n)

choi(n,m)