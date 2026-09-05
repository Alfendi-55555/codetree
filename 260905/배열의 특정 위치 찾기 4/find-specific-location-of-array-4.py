nums = list(map(int,input().split()))

total = 0
cnt = 0

for i in nums:
    if i == 0:
        break
    if i%2 == 0:
        total += i
        cnt += 1

print(f"{cnt} {total}")