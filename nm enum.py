#Перебрать все n-значные числа в m-ричной системе счисления

def rec(i):
    if i == n:
        print(''.join(ans))
        return
    for j in range(m):
        ans[i] = str(j)
        rec(i + 1)


n, m = map(int, input().split())
ans = [0] * n
rec(0)
