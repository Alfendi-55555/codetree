arr = list(map(int,input().split()))


sum = 0
pyung = 0
cnt = 0
for i in arr:
    if i >=250:
        break
    sum += i
    cnt += 1

if sum == 0:
    for i in arr:
        cnt = 10
    
pyung = sum/cnt

print(f"{sum} {pyung:.1f}")