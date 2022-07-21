import mpmath as mp
from mpmath import mpf
mp.mp.dps = 50


def phi_0(x, L):
    return L


def phi_1(x, L):
    return (L
            * mp.exp(-mp.exp(-L*x)*mp.sin(L*x + mp.pi/4)
                     / (mp.sqrt(2)*L))
            )


def phi_2(x, L):
    integral = mp.quad(lambda t: mp.sin(t * phi_1(t, L))
                       * mp.exp(-t * phi_1(t, L)),
                       [x, mp.inf],)
    return L * mp.exp(-integral)


def phi_3(x, L):
    integral = mp.quad(lambda t: mp.sin(t * phi_2(t, L))
                       * mp.exp(-t * phi_2(t, L)),
                       [x, mp.inf])
    return L * mp.exp(-integral)


def FindL(y_0):
    def f(L):
        return y_0 - phi_2(mpf('0'), L)
    return mp.findroot(f, y_0, verbose=True)
