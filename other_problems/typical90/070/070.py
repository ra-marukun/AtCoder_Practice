import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4
1000000000 1000000000
-1000000000 1000000000
-1000000000 -1000000000
1000000000 -1000000000

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import statistics

n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
X,Y = [list(i) for i in zip(*xy)]

X_p = statistics.median(X)
Y_p = statistics.median(Y)

ans = 0
for i in range(n):
    ans += abs(X_p-X[i])
    ans += abs(Y_p-Y[i])

print(int(ans))