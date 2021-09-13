import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
7
0 1
1 0
2 0
2 1
2 2
3 0
3 2

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
X, Y = [list(i) for i in zip(*xy)]

setX = set(X)
setY = set(Y)
lenX = len(setX)
lenY = len(setY)
xlist = [set() for _ in range(lenX)]

Dx = { v: i for i, v in enumerate(setX) }
Dy = { v: i for i, v in enumerate(setY) }

X = list(map(lambda v: Dx[v], X))
Y = list(map(lambda v: Dy[v], Y))


xlist = {x: set() for x in X}

for i in range(len(X)):
    xlist[X[i]].add(Y[i])

ans = 0
for x_left in range(lenX-1):
    for x_right in range(x_left+1, lenX):
        xl = xlist[x_left]
        xr = xlist[x_right]
        for yl in xl:
            for yr in xr:
                if yl < yr:                
                    if (yr in xl) & (yl in xr):
                        ans += 1
print(ans)