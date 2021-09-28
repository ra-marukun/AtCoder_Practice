import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3
3 5 2
27

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from bisect import bisect_right

n = int(input())
A = list(map(int, input().split()))
x = int(input())

def np_x_zeta(x, initial=None):
    if isinstance(x[0], list):
        for i in range(len(x)):
            np_x_zeta(x[i], initial=initial)
        if initial is not None:
            x.insert(0, [initial] * len(x[0]))
        for j in range(len(x[0])):
            for i in range(1, len(x)):
                x[i][j] += x[i - 1][j]
    else:
        if initial is not None:
            x.insert(0, initial)
        for i in range(1, len(x)):
            x[i] += x[i - 1]

ans = 0
Asum = A.copy()
np_x_zeta(Asum)
i = x//Asum[-1]
res = x - Asum[-1]*i
ans += i*n

idx = bisect_right(Asum, res)
ans += idx+1
print(ans)
