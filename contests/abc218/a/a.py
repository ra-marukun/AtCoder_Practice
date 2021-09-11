import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
3
oooxoox

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
n = int(input())
S = input()


s = S[n-1]

if s == 'o':
    print('Yes')
else:
    print('No')