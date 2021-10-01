import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
from collections import Counter, deque

h, w = map(int, input().split())
P = [ list(map(int, input().split())) for _ in range(h)]

ans = -1
for i in range(1,2**h):
    s = format(i, '0{}b'.format(h))
    l = [j for j, x in enumerate(s[::-1]) if x == '1']
    if len(l) == 0:
        continue
    # if len(l) ==1:
        
    hako = deque()
    for j in range(w):
        for k in l:
            if not P[k][j] == P[l[0]][j]:
                break
            if k == l[-1]:
                hako.append(P[k][j])
        if hako:
            c = Counter(hako)
            now = len(l) * c.most_common(1)[0][1]
            ans = max(ans,now)
print(ans)