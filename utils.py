import numpy as np
from scipy import stats

def get_stats(X):
    """Return basic statistics: size, mean, and sample standard deviation."""
    n = len(X)
    x = X.mean()
    s = X.std(ddof=1)
    return n, x, s

def degrees_of_freedom(n_v, s_v, n_c, s_c):
    """Compute degrees of freedom for two independent samples."""
    s_v_n_v = s_v**2 / n_v
    s_c_n_c = s_c**2 / n_c
    numerator = (s_v_n_v + s_c_n_c)**2
    denominator = (s_v_n_v**2 / (n_v - 1)) + (s_c_n_c**2 / (n_c - 1))
    return numerator / denominator

def t_value(n_v, x_v, s_v, n_c, x_c, s_c):
    """Compute the t-value for two independent samples."""
    s_v_n_v = s_v**2 / n_v
    s_c_n_c = s_c**2 / n_c
    numerator = x_v - x_c
    denominator = np.sqrt(s_v_n_v + s_c_n_c)
    return numerator / denominator

def p_value(d, t_val):
    """Compute the right-tailed p-value for a t-distribution."""
    t_dist = stats.t(df=d)
    return 1 - t_dist.cdf(t_val)

def make_decision(X_v, X_c, alpha=0.05):
    """Decide whether to reject H0 based on AB test."""
    n_v, x_v, s_v = get_stats(X_v)
    n_c, x_c, s_c = get_stats(X_c)
    d = degrees_of_freedom(n_v, s_v, n_c, s_c)
    t_val = t_value(n_v, x_v, s_v, n_c, x_c, s_c)
    p = p_value(d, t_val)
    return "Reject H0" if p <= alpha else "Do not reject H0"

