A = input()

# Please write your code here.

def dif_char(n):
    char = []
    for i in range(len(n)):
        char.append(n[i])
    char_set = set(char)
    if len(char_set) <= 1:
        print('No')
    else:
        print('Yes')

dif_char(A)