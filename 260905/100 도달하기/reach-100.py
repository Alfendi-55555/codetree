n = int(input())

nums=[1,n]

total = 0

for i in range(1,100):
    nums.append(nums[i]+nums[i-1])
    if nums[i]+nums[i-1] > 100:
        break

for i in range(len(nums)):
    print(nums[i],end=' ')