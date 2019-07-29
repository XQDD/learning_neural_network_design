from utils import *

# Theory and Example
# Perceptron
print("思路：取两向量所在平面a的中线l，分界面b即垂直平面a并过中线l的平面")


# Hamming Network
def hamming1(w, p, b):
    return pure_lin(np.dot(w, p) + b)


def hamming2(a):
    """
    递归直到收敛（输入和输出相同）
    :param a:
    :return:
    """
    length = a.size
    r = range(length)
    sigmod = -(1 / (length - 1) - 0.1)
    w = np.ones((length, length))
    for i in r:
        for j in r:
            if i != j:
                w[i][j] = sigmod
    a_r = pos_lin(np.dot(w, a))
    for i in r:
        if a_r[i] != a[i]:
            return hamming2(a_r)
    return a_r


w = [[1, -1, -1], [1, 1, -1]]
b = [3, 3]
p = [-1, -1, -1]
a2 = hamming1(w, p, b)
print(a2)
print(hamming2(a2))

# Hopfield Network
# 一头雾水，可能后面会讲到参数如何得到的吧


# Exercises
# 待补
