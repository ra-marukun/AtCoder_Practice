import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3 3
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
h, w = map(int, input().split())
