nums = list(map(int,input().split()))

total = 0

for i in range(10):
    if i+1 == 3 or i+1 == 5 or i+1 == 10:
        total += nums[i]


print(total)