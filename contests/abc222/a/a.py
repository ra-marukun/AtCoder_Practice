import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
7777

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
print('{0:04d}'.format(n))
