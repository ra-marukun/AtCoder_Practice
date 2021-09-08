import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
6783 125

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import math

n, l = map(int, input().split())

dp = [0]*(n+1)

ans = 0
for i in range(n+1):
    if i < l:
        dp[i] = 1
    else:
        dp[i] = ( dp[i-1] + dp[i-l] ) % (10**9 + 7)

print(dp[n])