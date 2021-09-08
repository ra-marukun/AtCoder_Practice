import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np
import sys

n, q = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * q
R = [0] * q
V = [0] * q

A = np.array(A)
B = np.diff(A)

huben = [0]*(q+1)
huben[0] = np.sum(abs(B))

for i in range(q):
    #上から順番に代入していく
    L[i], R[i], V[i] = map(int, sys.stdin.readline().split())

for i,(l, r, v) in enumerate(zip(L, R, V)):
    hubenL = 0
    hubenR = 0
    if not(l==1):
        Bnew = B[l-2]+v
        hubenL = abs(Bnew) - abs(B[l-2])
        B[l-2] = Bnew
    if not(r==n):
        Bnew = B[r-1] - v
        hubenR = abs(Bnew) - abs(B[r-1])
        B[r-1] = Bnew
    huben[i+1] = huben[i] + hubenL + hubenR
    print(huben[i+1])