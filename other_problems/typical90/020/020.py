import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
8 3 2

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
a,b,c = map(int, input().split())

if a < c ** b:
    print('Yes')
else:
    print('No')