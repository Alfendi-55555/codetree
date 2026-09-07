n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def evennanu(n,arr):
    new_arr = []
    for i in range(0,n):
        if arr[i]%2 == 0:
            new_arr.append(int(arr[i]/2))
        else:
            new_arr.append(arr[i])
        
    return new_arr

for i in evennanu(n,arr):
    print(i,end = ' ')