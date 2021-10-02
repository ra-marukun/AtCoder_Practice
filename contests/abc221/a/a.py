import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
5 5

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
a, b = map(int, input().split())
ans = 32**(a-b)
print(ans)
