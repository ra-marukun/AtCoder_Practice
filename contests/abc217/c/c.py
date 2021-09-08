import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
5
5 3 2 4 1

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
P = list(map(int, input().split()))

q = ['']*n

for i,p in enumerate(P):
    q[p-1] = str(i+1)

print(' '.join(q))