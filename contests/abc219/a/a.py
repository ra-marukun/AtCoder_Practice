import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
97

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
x = int(input())

if x<40:
    print(40-x)
elif x<70:
    print(70-x)
elif x<90:
    print(90-x)
else:
    print('expert')
