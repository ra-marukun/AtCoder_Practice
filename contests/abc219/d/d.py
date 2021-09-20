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
n = int(input())
x,y = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
A, B = [list(i) for i in zip(*ab)]

A_sum = sum(A)
B_sum = sum(B)

if (x>A_sum)|(y>B_sum):
    print(-1)
    exit()

dp = [[[float('inf')]*(y+1) for _ in range(x+1)]for _ in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(x+1):
        for k in range(y+1):
            dp[i+1][min(j+A[i],x)][min(k+B[i],y)] = min(dp[i][j][k]+1, dp[i+1][min(j+A[i],x)][min(k+B[i],y)])
            dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])

ans = dp[n][x][y]
if ans > 1000:
    print(-1)
else:
    print(int(ans))
