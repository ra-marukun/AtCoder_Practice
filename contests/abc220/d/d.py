import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
5
0 1 2 3 4

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
A = list(map(int, input().split()))

mod = 998244353

dp = [[0]*10 for _ in range(n)]
dp[0][A[0]] = 1
for i in range(1,n):
    num = A[i]
    for j in range(0,10):
        tasu = (num + j) % 10
        kakeru = (num * j) % 10
        dp[i][tasu] += dp[i-1][j]
        dp[i][tasu] %= mod
        dp[i][kakeru] += dp[i-1][j]
        dp[i][kakeru] %= mod
for i in range(0,10):
    print(dp[n-1][i])