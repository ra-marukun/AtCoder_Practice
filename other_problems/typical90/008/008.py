import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
10
attcordeer

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import sys
n = int(input())
s= input()

mod = 10**9 + 7

#最初と最後をカット
s = s[s.find('a'):]
s = s[:s.rfind('r')+1]

moji = 'atcoder'
new_s = ''
hozon = 1
for si in s:
    if si in moji:
        if si == 'a':
            new_s += 'a'
        if si == 't':
            hozon = max(2,hozon)
            new_s += 't'
        elif (si == 'c')&(hozon>=2):
            hozon = max(3,hozon)
            new_s += 'c'
        elif (si == 'o')&(hozon>=3):
            hozon = max(4,hozon)
            new_s += 'o'
        elif (si == 'd')&(hozon>=4):
            hozon = max(5,hozon)
            new_s += 'd'
        elif (si == 'e')&(hozon>=5):
            hozon = max(6,hozon)
            new_s += 'e'
        elif (si == 'r')&(hozon>=6):
            hozon = 7
            new_s += 'r'
if hozon < 6:
    print('0')
    sys.exit()

s= ''
hozon = 6
for si in new_s[::-1]:
    if si == 'r':
        s += 'r'
    elif si=='e':
        hozon = min(5,hozon)
        s += 'e'
    elif (si=='d')&(hozon<=5):
        hozon = min(4,hozon)
        s += 'd'
    elif (si=='o')&(hozon<=4):
        hozon = min(3,hozon)
        s += 'o'
    elif (si=='c')&(hozon<=3):
        hozon = min(2,hozon)
        s += 'c'
    elif (si=='t')&(hozon<=2):
        hozon = min(1,hozon)
        s += 't'
    elif (si=='a')&(hozon<=1):
        hozon = 0
        s += 'a'
S = s[::-1]

dp = [[0] * 8 for _ in range(len(S)+1)]
dp[0][0] = 1

if len(S)==7:
    print('1')
    sys.exit()

for i in range(len(S)):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if (S[i] == 'a')&(j == 0): dp[i+1][j+1] += dp[i][j]
        if (S[i] == 't')&(j == 1): dp[i+1][j+1] += dp[i][j]
        if (S[i] == 'c')&(j == 2): dp[i+1][j+1] += dp[i][j]
        if (S[i] == 'o')&(j == 3): dp[i+1][j+1] += dp[i][j]
        if (S[i] == 'd')&(j == 4): dp[i+1][j+1] += dp[i][j]
        if (S[i] == 'e')&(j == 5): dp[i+1][j+1] += dp[i][j]
        if (S[i] == 'r')&(j == 6): dp[i+1][j+1] += dp[i][j]
    for  k in range(8): dp[i+1][j] %= mod

print(dp[len(S)][7])