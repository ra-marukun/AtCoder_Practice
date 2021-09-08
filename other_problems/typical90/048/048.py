import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
10 12
987753612 748826789
36950727 36005047
961239509 808587458
905633062 623962559
940964276 685396947
959540552 928301562
60467784 37828572
953685176 482123245
87983282 66762644
912605260 709048491

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np

n, k = map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
A, B = [list(i) for i in zip(*xy)]

A = np.array(A, dtype = np.int64)
B = np.array(B, dtype = np.int64)

A = A - B

C  = np.append(B ,A)
C = sorted(C)

ans = np.sum(C[2*n -k:])
print(ans)