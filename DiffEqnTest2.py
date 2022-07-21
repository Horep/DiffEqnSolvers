import mpmath as mp
from mpmath import mpf as mpf

k = 2
y_0 = mpf('10')
f = mp.odefun(lambda x, y: (y ** k) * mp.exp(-(x * y)), mpf('0'), y_0)
mp.plot(f, [0, 1000])
