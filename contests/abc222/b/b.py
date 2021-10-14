import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3 22
6 22 37

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from bisect import bisect_left

n , p = map(int,input().split())
A = list(map(int,input().split()))

A = sorted(A)
idx = bisect_left(A,p)
print(idx)
