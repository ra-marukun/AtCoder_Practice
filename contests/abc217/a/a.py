import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
a aa

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング

s = list(input().split())

sorted_s = sorted(s)

if s[0] == sorted_s[0]:
    print('Yes')
else:
    print('No')