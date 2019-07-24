import numpy as np


def hard_lim(n):
    n[np.where(n < 0)] = 0
    n[np.where(n >= 0)] = 1
    return n


def hard_lim_s(n):
    n[np.where(n < 0)] = -1
    n[np.where(n >= 0)] = 1
    return n


def pure_lin(n):
    return n


def sat_lin(n):
    n[np.where(n < 0)] = 0
    n[np.where(n > 1)] = 1
    return n


def sat_lin_s(n):
    n[np.where(n < -1)] = -1
    n[np.where(n > 1)] = 1
    return n


def log_sig(n):
    return 1 / (1 + np.exp(-n))


def tan_sig(n):
    return (np.exp(n) - np.exp(-n)) / (np.exp(n) + np.exp(-n))


def pos_lin(n):
    n[np.where(n < 0)] = 0
    return n
