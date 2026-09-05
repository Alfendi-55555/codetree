total_pass = 0

num = int(input())

for i in range(num):
    scores = list(map(int,input().split()))
    total = 0

    for i in scores:
        total += i

    avg = total/4

    if avg >= 60:
        print("pass")
        total_pass += 1
    else:
        print("fail")


print(total_pass)