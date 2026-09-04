arr = list(map(int,input().split()))
newarr = []

for i in range(0,10):
    if arr[i] == 0:
        break
    newarr.append(arr[i])
    
for j in range(len(newarr)-1,-1,-1):
    print(newarr[j],end=' ')