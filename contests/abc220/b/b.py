import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
7
123 456

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
k = int(input())
a, b = map(str, input().split())
a, b = int(a,k), int(b,k)
print(a*b)