from utils import *
from decimal import Decimal
import matplotlib.pyplot as plt

# Solved Problems
print("\n---P2.1---")
p = Decimal("2.0")
w = Decimal("2.3")
b = -3
n = w * p + b
print(n)

print("\n---P2.2---")
print(hard_lim(n))
print(pure_lin(n))
print(log_sig(n))

print("\n---P2.3---")
p = np.array([-5, 6]).T
w = np.array([3, 2])
b = 1.2

n = np.dot(w, p) + b
print(n)
print(hard_lim_s(n))
print(sat_lin(n))
print(tan_sig(n))

print("\n---P2.4---")

print("1. 2(Two output)")
print("2. 6")
print("3. Log-Sigmoid")
print("4. Not information enough")

# Exercises
print("\n---E2.1---")
print("1. (1) Linear, (2) Positive Linear")
print(
    """2. (1) Hard Limit, (2) Symmetrical Hard Limit, (3) Linear, (4) Saturating Linear, 
    (5) Symmetrical Saturating Linear, (6) Positive Linear """)
print(
    """3. (1) Linear, (2) Saturating Linear, (3) Symmetrical Saturating Linear, (4) Positive Linear, (5) Log-Sigmoid, 
    (6) Hyperbolic Tangent Sigmoid""")
print("4. (1) Symmetrical Hard Limit, (2) Linear, (3) Symmetric Saturating Linear""")

print("\n---E2.2---")
# input  <3,>=3
# output -1,1
print("1. Symmetrical Hard Limit")
print("2. Bias is -3, and idk")
x = np.arange(-10, 10, step=0.1)
p = x
w = 1
bias = 3
y = hard_lim_s(w * p - 3)
# x axis, y aways 0
plt.plot(x, np.zeros(200), label="X Axis")
# y axis, x aways 0
plt.plot(np.zeros(40), np.arange(-2, 2, step=0.1), label="Y Axis")
plt.plot(x, y, label="Data")
plt.title("E2.2 3. Diagram")
plt.legend()
plt.show()

print("\n---E2.3---")
p = np.array([-5, 7]).T
w = np.array([3, 2])
t = np.dot(w, p)
print(t)
# input -1+b
# output 0.5
print("1. No")
print("2. Yes, 1.5")
print(pure_lin(t + 1.5))
print("3. Yes, 1")
print(log_sig(t + 1))
print("4. No")

print("\n---E2.4---")
print("1. S1(Not Enough Info) for Layer1 and 6 for Layer2")
print("2. S1x4 for Layer1 and 6xS1 for Layer2")
print("""3. (1) Linear, (2) Saturating Linear, (3) Symmetric Saturating Linear, (4) Log-Sigmoid, 
(5) Hyperbolic Tangent Sigmoid""")
print("4. (1) Symmetric Saturating Linear, (2) Hyperbolic Tangent Sigmoid")
print("5. Not Enough Info or idk")

print("\n---E2.5---")
p = np.arange(-2, 2, step=0.1)
plt.figure()
plt.title("E2.5")
# plt.plot(p, np.zeros(40), label="X Axis")
# plt.plot(np.zeros(90), np.arange(-2, 7, step=0.1), label="Y Axis")

plt.plot(p, hard_lim(1 * p + 1), label="1.")
plt.legend()
plt.show()

plt.plot(p, hard_lim(-1 * p + 1), label="2.")
plt.legend()
plt.show()

plt.plot(p, pure_lin(2 * p + 3), label="3.")
plt.legend()
plt.show()

plt.plot(p, sat_lin_s(2 * p + 3), label="4.")
plt.legend()
plt.show()

plt.plot(p, pos_lin(-2 * p - 1), label="5.")
plt.legend()
plt.show()

print("\n---E2.6---")
p = np.arange(-3, 3, step=0.1)
plt.figure()
plt.title("E2.6")
# plt.plot(p, np.zeros(60), label="X Axis")
# plt.plot(np.zeros(60), p, label="Y Axis")

w111 = 2
w211 = 1
b11 = 2
b21 = -1
w112 = 1
w122 = -1
b12 = 0

n11 = p * w111 + b11
plt.plot(p, n11, label="1. n11", marker=".")
plt.legend()
plt.show()

a11 = sat_lin(n11)
plt.plot(p, a11, label="2. a11", marker="+")
plt.legend()
plt.show()

n21 = p * w211 + b21
plt.plot(p, n21, label="3. n21", marker=3)
plt.legend()
plt.show()

a21 = sat_lin(n21)
plt.plot(p, a21, label="4. a21", marker="1")
plt.legend()
plt.show()

n12 = w112 * a11 + w122 * a21 + b12
plt.plot(p, n12, label="5. n12")
plt.legend()
plt.show()

a12 = pure_lin(n12)
plt.plot(p, a12, label="6. a12")
plt.legend()
plt.show()
