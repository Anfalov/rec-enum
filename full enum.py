def rec(i):
    if i == n:
        print(*ans)
        return
    ans[i] = 0
    rec(i + 1)
    ans[i] = 1
    rec(i + 1)


n = int(input())
a = ['Ivan', 'Petr', 'Egor']
ans = [0] * n
rec(0)
