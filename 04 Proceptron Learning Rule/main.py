# Theory and Examples
# Training Multiple-Neuron Perceptrons

from utils import *


def mul_neu_per_step(w, b, p, t):
    a = hard_lim(np.dot(w, p) + b)
    e = t - a
    w_new = w + np.array(p) * e
    b_new = b + e
    return w_new, b_new


def mul_neu_per(w, b, p, t):
    w_new = w
    b_new = b
    for i in range(len(p)):
        w_new, b_new = mul_neu_per_step(w_new, b_new, p[i], t[i])
    if (w_new == w).all():
        return w_new, b_new
    return mul_neu_per(w_new, b_new, p, t)


w, b = mul_neu_per([0.5, -1, -0.5],
                   0.5,
                   [[1, -1, -1], [1, 1, -1]],
                   [0, 1])
print(w)
print(b)
