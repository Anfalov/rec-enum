#Перебрать все перестановки длины n из чесел (0..n-1)
#012
#021
#102
#120
#201
#210

def rec(i):
    if i == n:
        print(''.join(ans))
        return
    for j in range(n):
        if not used[j]:
            ans[i] = str(j + 1)
            used[j] = 1
            rec(i + 1)
            used[j] = 0


n = int(input())
used = [0] * n
ans = [0] * n
rec(0)
