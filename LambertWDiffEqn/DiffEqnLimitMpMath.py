import mpmath as mp
from mpmath import mpf
mp.mp.dps = 20


def ReturnDiffSolution(y_0):
    y_0 = mpf(str(y_0))
    p = mp.odefun(lambda x, y: y*mp.sin(x*y)*mp.exp(-x*y), mpf('0'), y_0)
    return p


def L(y_0):
    y_0 = mpf(str(y_0))
    f = mp.odefun(lambda x, y: y*mp.sin(x*y)*mp.exp(-x*y), mpf('0'), y_0)
    L = mp.limit(f, mp.inf, method="shanks")
    return L


def L_a(y_0):
    y_0 = mpf(str(y_0))
    return mpf('1') / (mpf('2') * mp.lambertw(mpf('1')/(mpf('2')*y_0)))


def ReturnApproxSolution(y_0):
    y_0 = mpf(str(y_0))
    L = L_a(y_0)

    def A(x):
        return (L
                * mp.exp(-mp.exp(-L*x)*mp.sin(L*x + mp.pi/4)
                         / (mp.sqrt(2)*L))
                )
    return A


def PlotActualVSApprox(y_0):
    y_0 = mpf(str(y_0))
    t = ReturnDiffSolution(y_0)
    t_a = ReturnApproxSolution(y_0)
    place = L(y_0)
    print(f"L = {place}")
    print(f"L_a = {L_a(y_0)}")
    mp.plot([t, t_a, lambda x: place], [0, 2])
