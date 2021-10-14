import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3
2 2 2
2 2 2

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mod = 998244353

dp = [ [0]*(B[n-1]+1) for _ in range(n) ]

csum = [1] * (B[n-1]+1)

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

for i in range(n):
    for j in range(A[i],B[i]+1):
        dp[i][j] = csum[j]%mod
    csum = dp[i]
    np_x_zeta(csum)

print(dp[n-1][B[n-1]]%mod)