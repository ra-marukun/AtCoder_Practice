import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
P = list(map(int, input().split()))

s = 'abcdefghijklmnopqrstuvwxyz'

s1 = ''
for p in P:
    s1 += s[p-1]

print(s1)