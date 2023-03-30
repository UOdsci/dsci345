import numpy as np

def pretty(x, n):
    """
    Returns a "pretty" set of bin boundaries roughly of size n
    that span x. Use, for instance, like:
      plt.hist(x, bins=pretty(x, 40))
    """
    # see https://github.com/wch/r-source/blob/trunk/src/appl/pretty.c
    h = 1.5
    h5 = .5 + 1.5 * h
    lo = np.nanmin(x)
    up = np.nanmax(x)
    assert lo < up, "All values are the same."
    c = (up - lo) / n
    b = 10 ** np.floor(np.log10(c))
    m = [1, (2+h)/(1+h), (5+2*h5)/(1+h5), (10+5*h)/(1+h), 10]
    k = np.digitize(c/b, m)
    u = b * [1, 2, 5, 10][k - 1]
    ns = np.floor(lo / u + 1e-10)
    nu = np.ceil(up / u - 1e-10)
    return np.arange(ns * u, (nu + 1) * u, u)
