num = int(input())

nums = list(map(int,input().split()))

even =[]

for i in nums:
    if i%2 == 0:
        even.append(i)

for i in range(len(even)-1,-1,-1):
    print(even[i],end=' ')