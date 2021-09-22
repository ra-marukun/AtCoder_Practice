import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
2
1 1 3 2
2 1 4 2

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング

import sys
from collections import Counter

n = int(input())
xy = [map(int, sys.stdin.readline().split()) for _ in range(n)]
Lx, Ly, Rx, Ry = [list(i) for i in zip(*xy)]
 
size = 1000
d = [[0]*size for _ in range(size)]
 
for i in range(n):
    lx = Lx[i]
    ly = Ly[i]
    rx = Rx[i]
    ry = Ry[i]
 
    d[lx][ly] += 1
    if ry<=size-1:
        d[lx][ry] -= 1
    if rx<=size-1:
        d[rx][ly] -= 1
    if (rx<=size-1)&(ry<=size-1):
        d[rx][ry] += 1
 
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
 
 
np_x_zeta(d)
_is_array_like = lambda a: isinstance(a, tuple) or isinstance(a, list)
np_shape = lambda a: (len(a), *np_shape(a[0])) if _is_array_like(a) else ()
np_ndim = lambda a: len(np_shape(a))
# 変形
np_flatten = lambda a: np_flatten([a for a in a for a in a]) if np_ndim(a) > 1 else a if np_ndim(a) == 1 else [a]

d = np_flatten(d)
ans = Counter(d)
for i in range(1,n+1):
    print(ans[i])
