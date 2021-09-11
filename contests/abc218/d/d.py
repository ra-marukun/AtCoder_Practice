import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
6
0 0
0 1
1 0
1 1
2 0
2 1

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from itertools import combinations

n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
X, Y = [list(i) for i in zip(*xy)]

setX = list(set(X))
xlist = [[] for _ in range(len(setX))]

for i in range(n):
    idx = setX.index(X[i])
    xlist[idx].append(Y[i])

iterlist = [[] for _ in range(len(setX))]
for i,x in enumerate(xlist):
    iterlist[i] = list(combinations(x,2))
print(iterlist)