a, b, c = map(int, input().split())

# Please write your code here.

def mimi(a,b,c):
    n = a
    if n>b:
        n = b
    if n>c:
        n=c

    return n

print(mimi(a,b,c))