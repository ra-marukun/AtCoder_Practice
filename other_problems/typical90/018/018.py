import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
5121
312000000 4123 3314
6
123
12
445
4114
42
1233

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import math

t = int(input())
l, x, y = map(int,input().split())
q = int(input())
E = [int(input()) for _ in range(q)]

def position(time):
    theta = - time / t * 2 * math.pi - math.pi / 2
    Y = l/2 * math.cos(theta)
    Z = l/2 * math.sin(theta) + l/2
    return Y, Z

def gyoukaku(Y ,Z):
    dist_ = math.dist((0,Y),(x,y))
    kaku = math.degrees(math.atan(Z/dist_))
    return kaku

for e in E:
    Y, Z = position(e)
    print(gyoukaku(Y, Z))