import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4
1 9 1 9

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np
from bisect import bisect_right

n= int(input())
A = list(map(int, input().split()))

A = np.array(A)
ruiseki = [0] * (2*n + 1)
ruiseki = np.array(ruiseki)
ruiseki[1:n+1] = np.cumsum(A)
size = ruiseki[n]
ruiseki[n+1:2*n+1] = ruiseki[1:n+1] + size

target = size / 10

if not(size % 10 == 0):
    print('No')
else:
    for i in range(1,n + 1):
        temp = ruiseki[i]
        if ruiseki[i+1] - temp > target:
            if i == n:
                print('No')
            continue
        elif (ruiseki[bisect_right(ruiseki, temp+target , i, i+n) - 1] - temp) == target:
            print('Yes')
            break
        elif i == n:
            print('No')