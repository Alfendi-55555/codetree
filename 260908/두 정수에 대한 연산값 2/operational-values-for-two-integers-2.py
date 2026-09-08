a, b = map(int, input().split())

# Please write your code here.


def baggu(a,b):
    if a>b:
        a *= 2
        b += 10
    else:
        a+= 10
        b *= 2
    return a,b

n = baggu(a,b)
print(f"{n[0]} {n[1]}")