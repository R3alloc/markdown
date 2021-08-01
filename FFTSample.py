import math
import numpy as np
from matplotlib import pyplot as plt 

src_sig = np.zeros([40,40])

# 源信号 扩展了40份，每一份都是一样的
for N in range(0, 40):
    n = np.arange(0, 40, 1)
    # src_sig[N*40 : N*40 + 40] = np.cos(2*math.pi * 2*n / 40 + math.pi/3)
    src_sig[N, 0:40] = np.cos(2*math.pi * 2*n / 40 + math.pi/3)
    # src_sig[N, 0:39] = np.cos(2*math.pi * 2*n / 40 + math.pi/3)

# 40个sin basis
sin_basis = np.zeros([40, 40])
for N in range(0, 40):
    n = np.arange(0, 40, 1)
    # sin_basis[N*40 : N*40 + 40] = np.sin(2*math.pi * N*n / 40)
    sin_basis[N, 0:40] = np.sin(2*math.pi * N*n / 40)

X_mat_sin = src_sig * sin_basis
X_sin=X_mat_sin.sum(axis=1) # 需要指定按行求和，否则默认按列求和
maxX_sin=max(X_sin)
plt.stem(X_sin)

cos_basis = np.zeros([40, 40])
for N in range(0, 40):
    n = np.arange(0, 40, 1)
    # cos_basis[N*40 : N*40 + 40] = np.cos(2*math.pi * N*n / 40)
    cos_basis[N, 0:40] = np.cos(2*math.pi * N*n / 40)

X_mat_cos = src_sig * cos_basis
X_cos=X_mat_cos.sum(axis=1) # 需要指定按行求和，否则默认按列求和
maxX_cos=max(X_cos)
plt.stem(X_cos)

# 这个也就是X_cos[2] + j*X_sin[2] 
cmpl = maxX_cos + 1j * maxX_sin
mag = np.sqrt(maxX_cos**2 + maxX_sin**2)
phase = np.arctan(maxX_sin/maxX_cos)    # 也就是pi/3