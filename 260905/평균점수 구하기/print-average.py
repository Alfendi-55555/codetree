scores = list(map(float,input().split()))

total = 0
for i in scores:
    total += i

print(round(total/8,1))