import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
11 18
23 92 85 34 21 63 12 9 81 44 96
3 10 0
3 5 0
1 3 4
2 0 0
1 4 11
3 11 0
1 3 5
2 0 0
2 0 0
3 9 0
2 0 0
3 6 0
3 10 0
1 6 11
2 0 0
3 10 0
3 4 0
3 5 0

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import sys

n, q = map(int, input().split())
A = list(map(int, input().split()))

TXY = [map(int, sys.stdin.readline().split()) for _ in range(q)]
T, X, Y = [list(i) for i in zip(*TXY)]

rot = 0
for t,x,y in zip(T,X,Y):
    idx1 = (x-1 - rot)%n
    idx2 = (y-1 - rot)%n
    if t == 1:
        A[idx1], A[idx2] = A[idx2], A[idx1]
    if t == 2:
        rot += 1
    if t == 3:
        print(A[idx1])