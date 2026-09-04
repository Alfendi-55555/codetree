num = int(input())
scores = list(map(float,input().split()))
total = 0

for i in scores:
    total += i

avg = round(total/num,1)
print(avg)

if avg >= 4.0:
    print("Perfect")
elif avg >=3.0:
    print("Good")
else:
    print("Poor")