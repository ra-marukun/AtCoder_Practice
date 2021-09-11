import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
5
#####
##..#
#..##
#####
.....
#####
#..##
##..#
#####
.....

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import numpy as np

n = int(input())

def change(s):
    if s == '#':
        return 1
    else:
        return 0
    

S = [input() for l in range(n)]
T = [input() for l in range(n)]
S = [list(map(change, s)) for s in S]
T = [list(map(change, t)) for t in T]

S = np.array(S)
T = np.array(T)
T_dict = np.array(list(zip(*np.where(T == 1))))

def heikou(C_dict):
    if len(C_dict) != len(T_dict):
        return False
    else:
        shift = T_dict[0] - C_dict[0]
        for i in range(1,len(T_dict)):
            if np.any(T_dict[i] !=  C_dict[i] + shift):
                return False
        return True

for rot in range(4):
    C = np.rot90(S, rot).copy()
    C_dict = np.array(list(zip(*np.where(C == 1))))
    if heikou(C_dict):
        print('Yes')
        break
    elif rot == 3:
        print('No')