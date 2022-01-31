#Перебрать все сочетания из n по k эл-в с помощью перехода к след. сочетанию
#0123
#012
#013
#023
#123


def next_combination(ans):
    for i in range(k - 1, -1, -1): #for (int i = k - 1; i >= 0; i--)
        if ans[i] <= n - k + i:
            ans[i] += 1
            for j in range(i + 1, k):
                ans[j] = ans[j - 1] + 1
            return True
    return False


n, k = map(int, input().split())
ans = [i for i in range(1, k + 1)]
print(*ans)
while next_combination(ans):
    print(*ans)