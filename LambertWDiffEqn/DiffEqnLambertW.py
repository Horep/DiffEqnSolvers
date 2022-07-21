import mpmath as mp

mp.mp.dps = 50
y_0 = mp.mpf(mp.catalan)

L = mp.mpf('1') / (mp.mpf('2') * mp.lambertw(mp.mpf('1')/(mp.mpf('2')*y_0)))
L_0 = y_0 + mp.mpf('1/2') - mp.mpf('1')/(mp.mpf('8')*y_0)
print(L)
print(L_0)
