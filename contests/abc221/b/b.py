import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
abcdefffgff
abcdeffgfff

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import sys

s = input()
t = input()

if s == t:
    print('Yes')
    sys.exit()

list_s = []
list_t = []
list_i = []
for i in range(len(s)):
    s0 = s[i]
    t0 = t[i]
    if not s0 == t0:
        list_s.append(s0)
        list_t.append(t0)
        list_i.append(i)


if len(list_s)>=3:
    print('No')
    sys.exit()
else:
    if list_s == list_t[::-1]:
        if list_i[1] - list_i[0] == 1:
            print('Yes')
        else:
            print('No')
    else:
        print('No')