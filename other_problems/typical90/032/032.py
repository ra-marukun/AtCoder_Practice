import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
10
1 10 100 1 10 100 1 10 100 2
10 1 100 1 10 100 1 10 100 2
100 10 1 1 10 100 1 10 100 2
1 10 100 1 10 100 1 10 100 2
10 1 100 1 10 100 1 10 100 2
100 10 1 1 10 100 1 10 100 2
1 10 100 1 10 100 1 10 100 5
10 1 100 1 10 100 1 10 100 6
100 10 1 1 10 100 1 10 100 1
100 10 1 1 10 100 1 10 100 1
40
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6
1 2
1 5
2 4
3 6

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from itertools import permutations

n = int(input())
#リスト内包表記
#上から順にlistを読み込んでlistに格納していく。
A = [list(map(int, input().split())) for l in range(n)]

m = int(input())

XY = [''] * m
YX = XY.copy()

if not (m==0):
    xy = [map(int, input().split()) for _ in range(m)]
    X, Y = [list(i) for i in zip(*xy)]

    for i in range(m):
        x_ = str(X[i]-1)
        y_ = str(Y[i]-1)
        XY[i] = x_ + y_
        YX[i] = y_ + x_

def calc_min(run):
    sum = 0
    for i,r in enumerate(run):
        sum += A[r][i]
    return sum

runs = list(permutations(range(n)))

ans = 10009
for run in runs:
    run_str = ''.join(map(str,run))
    for xy, yx in zip(XY, YX):
        if (xy in run_str) | (yx in run_str):
            break
    else:
        minute = calc_min(run)
        if minute <= ans:
            ans = minute
    continue

if ans>=10009:
    print('-1')
else:
    print(ans)