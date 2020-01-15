# 딥러닝 책에 있는 논리게이트 코드입니다.
# 퍼셉트론 구현
# 퍼셉트론 : 다수의 신호를 입력으로 받아 하나의 신호를 출력.

import numpy as np

# AND Gate

def ANDGate(A1, A2):
    A = np.array([A1, A2])
    y = np.array([0.5, 0.5])
    k = -0.8
    t = np.sum(A*y) + k
    if t <= 0:
        return 0
    else:
        return 1

# NAND Gate

def NANDGate(N1, N2):
    N = np.array([N1, N2])
    y = np.array([-0.5, -0.5])
    k = 0.8
    t = np.sum(N * y) + k
    if t <= 0:
        return 0
    else:
        return 1

# OR Gate

def ORGate(O1, O2):
    O = np.array([O1, O2])
    y = np.array([0.5, 0.5])
    k = -0.2
    t = np.sum(O * y) + k
    if t <= 0:
        return 0
    else:
        return 1

# XOR Gate

def XOR(Xo1, Xo2):
    s1 = NAND(Xo1, Xo2)
    s2 = OR(Xo1, Xo2)
    result = AND(s1, s2)
    return result

