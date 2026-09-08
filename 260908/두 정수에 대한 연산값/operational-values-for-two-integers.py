a, b = map(int, input().split())

# Please write your code here.

if a>b:
    a += 25
    b *= 2
else:
    a*=2
    b+=25

print(f'{a} {b}')