n, m = map(int, input().split())

# Please write your code here.

def swap(a,b):
    temp = b
    b = a
    a = temp
    print(a,b)

swap(n,m)