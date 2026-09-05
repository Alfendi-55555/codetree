nums = list(map(int,input().split()))

for i in range(len(nums)):
    if nums[i] == 0:
        break
    if nums[i]%2 == 1:
        print(nums[i]+3,end=' ')
    else:
        print(nums[i]//2,end=' ')