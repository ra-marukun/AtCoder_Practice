import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
100 10
1 31
2 41
1 32
2 26
1 1
2 58
1 97
2 93
1 23
2 84

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np

l, q = map(int, input().split())
xy = [map(int, input().split()) for _ in range(q)]
C, X = [list(i) for i in zip(*xy)]

cut_list = ['1'] * (l+1)
cut_list[0], cut_list[-1] = '0', '0'
cut_list = ''.join(cut_list)


for c,x in zip(C,X):
    if c == 1:
        cut_list = cut_list[:x]+'0'+cut_list[x+1:]
    if c == 2:
        len_list = cut_list.split('0')
        len_list = np.array(list(map(len,len_list))[1:-1])
        len_list = len_list+1
        ruiseki = np.cumsum(len_list)
        idx = np.argmax(ruiseki > x,0)

        print(len_list[idx])
