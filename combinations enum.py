#Перебрать все сочетания из n по k эл-в
#012
#n = 3, k = 2
#01
#02
#12

def rec(i, st):
    if i == k:
        print(' '.join(ans))
        return
    if n - st < k - i:
        return
    for j in range(st, n):
        ans[i] = str(j + 1)
        rec(i + 1, j + 1)


n, k = map(int, input().split())
ans = [0] * k
rec(0, 0)