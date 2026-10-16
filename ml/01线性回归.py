import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([2, 3, 5, 4, 7, 9, 12, 12, 15])

w, b = 0, 0
alpha = 0.0005
epochs = 301

for epoch in range(epochs):
    yh = w * x + b
    dw, db = 0, 0
    loss = 0
    for i in range(len(x)):
        error = yh[i] - y[i]
        dw += error * x[i] / len(x)
        db += error / len(x)
        loss += error**2 / 2 / len(x)
    w -= alpha * dw
    b -= alpha * db

    if epoch % 30 == 0:
        print(f"w={w:.6f}, b={b:.6f}, loss = {loss:.6f}")
