import numpy as np

"""
假设要预测二手车价格。每辆车有 3 个特征：
- x1: 车龄, 单位“年”
- x2: 行驶里程, 单位“万公里”
- x3: 发动机排量, 单位“L”
- y: 价格, 单位“万元”
"""

X = np.array([
    [1,  1.2, 2.0],
    [2,  2.5, 1.5],
    [3,  3.0, 2.0],
    [4,  5.5, 1.5],
    [5,  6.0, 2.0],
    [6,  8.0, 1.5],
    [7,  9.5, 2.0],
    [8, 11.0, 1.5],
    [9, 12.5, 2.0],
    [10, 15.0, 1.5],
], dtype=float)

y = np.array([
    22.5, 18.3, 18.0, 13.2, 14.5,
    9.8, 11.0, 6.5, 7.2, 3.8
], dtype=float)

w = np.zeros(3)
b = 0
epochs = 100001
alpha = .017314

for epoch in range(epochs):
    yh = X @ w + b
    error = yh - y
    loss = np.sum(error ** 2) / (2 * len(X))
    dw = X.T @ error / len(X)
    db = np.mean(error)

    w -= alpha * dw
    b -= alpha * db

    if epoch % 50 == 0:
        print(f"epoch:{epoch}, w={w}, b={b}, loss={loss:.6f}")


new_car = np.array([4, 4.0, 2.0])
new_value = new_car @ w + b

print(new_value)