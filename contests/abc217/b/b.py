import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
AGC
ABC
ARC

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
s1 = input()
s2 = input()
s3 = input()

s_list = ['ARC', 'AGC', 'AHC', 'ABC']
s_list.remove(s1)
s_list.remove(s2)
s_list.remove(s3)

print(s_list[0])