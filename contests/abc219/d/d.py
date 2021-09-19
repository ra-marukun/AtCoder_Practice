import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3
5 6
2 1
3 4
2 3

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np

n = int(input())
x,y = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
A, B = [list(i) for i in zip(*ab)]

A_sum = sum(A)
B_sum = sum(B)

if (x>A_sum)|(y>B_sum):
    print(-1)
    exit()

dp = np.array([[[float('inf')]*(B_sum+1) for _ in range(A_sum+1)]for _ in range(n+1)])
dp[0][0][0] = 0
for i in range(n):
    for j in range(A_sum+1):
        for k in range(B_sum+1):
            pre = dp[i][j][k]
            if (j<A[i])|(k<B[i]):
                dp[i+1][j][k] = pre
            elif (j==A[i])&(k==B[i]):
                dp[i+1][j][k] = 1
            else:
                dp[i+1][j][k] = min(dp[i][j-A[i]][k-B[i]]+1, pre)

kotae = dp[n,x:,y:]
ans = np.min(kotae)
if ans > 1000:
    print(-1)
else:
    print(int(ans))
