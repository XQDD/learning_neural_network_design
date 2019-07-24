import numpy as np


# Transfer functions:
def hard_lim(n):
    a = np.array(n)
    a[a < 0] = 0
    a[a >= 0] = 1
    return a


def hard_lim_s(n):
    a = np.array(n)
    a[a < 0] = -1
    a[a >= 0] = 1
    return a


def pure_lin(n):
    return n


def sat_lin(n):
    a = np.array(n)
    a[a < 0] = 0
    a[a > 1] = 1
    return a


def sat_lin_s(n):
    a = np.array(n)
    a[a < -1] = -1
    a[a > 1] = 1
    return a


def log_sig(n):
    return 1 / (1 + np.exp(-n))


def tan_sig(n):
    return (np.exp(n) - np.exp(-n)) / (np.exp(n) + np.exp(-n))


def pos_lin(n):
    a = np.array(n)
    a[a < 0] = 0
    return a
