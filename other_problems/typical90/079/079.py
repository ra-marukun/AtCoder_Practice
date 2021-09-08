import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 1 0
0 0 0

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

A = np.array(A)
B = np.array(B)

#Cをゼロ行列Zにすることを目指す
C = B-A
Z = np.zeros_like(C)

ans = 0
for i in range(h-1):
    for j in range(w-1):
        dif = Z[i,j] - C[i,j]
        C[i:i+2,j:j+2] += dif
        ans += abs(dif)
if np.allclose(C, Z):
    print('Yes')
    print(ans)
else:
    print('No')