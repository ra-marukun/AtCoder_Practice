import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
381453331666495446 746254773042091083

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
l, r = map(int, input().split())

# oldr = 0
# if r == 10**18:
#     oldr = 1
#     r = 10**18 - 1

mod = 10**9 + 7

keta_sum = [0] * 19
for i in range(19):
    keta_sum[i] = ((i+1) % mod) * (((10**i) + (10**(i+1) - 1)) * (10**(i+1) - 10**(i)) //
     2 % mod ) % mod

keta_l = 0
keta_c = 0
keta_r = 0

#l, r の桁数からketa_sumでの所属グループを求める
gl = len(str(l)) - 1
gr = len(str(r)) - 1


if (gr - gl) >= 1:
    for i in range(gl+1, gr+1):
        keta_c += keta_sum[i]
        keta_c = keta_c % mod

keta_l = ((gl+1)%mod) * (( ((l+10**(gl+1)-1) * (10**(gl+1) - l)) //2 )%mod)
keta_r = ((gr+1)%mod) * (( ((r+10**(gr+1)) * (10**(gr+1) - r-1)) //2 )%mod)

keta_l = keta_l % mod
keta_r = keta_r % mod

ans = (keta_l + keta_c - keta_r)%mod
# if oldr==1:
#     ans += 19 * (10**18 % mod)
#     ans = ans % mod

print(ans)
