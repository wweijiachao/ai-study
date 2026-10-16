import numpy as np


def version1():
    # 每一行是一个学生
    # 第1列：每天学习小时数
    # 第2列：每天做题数量（单位：10题）
    X = np.array(
        [
            [1, 2],
            [2, 1],
            [2, 4],
            [3, 3],
            [4, 5],
            [5, 4],
            [5, 7],
            [6, 6],
            [7, 8],
            [8, 9],
        ],
        dtype=float,
    )

    y = np.array([52, 54, 60, 62, 70, 73, 78, 82, 89, 94], dtype=float)

    w = np.zeros(2)
    b = 0
    alpha = 0.015
    loss = 0

    epochs = 500

    for epoch in range(epochs):
        loss = 0
        dw = np.zeros(2)
        db = 0
        for i in range(len(X)):
            yh = w[0] * X[i][0] + w[1] * X[i][1] + b
            error = yh - y[i]
            loss += error**2 / (2 * len(X))

            dw[0] += error * X[i][0] / len(X)
            dw[1] += error * X[i][1] / len(X)
            db += error / len(X)

        w -= alpha * dw
        b -= alpha * db

        if epoch % 50 == 0:
            print(f"epoch={epoch}, w={w}, b={b}, loss={loss:.2f}")

    # 预测新数据
    new_student = np.array([6, 8])
    new_y = new_student @ w + b
    print(new_y)


def version2_np():
    # 每一行是一个学生
    # 第1列：每天学习小时数
    # 第2列：每天做题数量（单位：10题）
    X = np.array(
        [
            [1, 2],
            [2, 1],
            [2, 4],
            [3, 3],
            [4, 5],
            [5, 4],
            [5, 7],
            [6, 6],
            [7, 8],
            [8, 9],
        ],
        dtype=float,
    )

    y = np.array([52, 54, 60, 62, 70, 73, 78, 82, 89, 94], dtype=float)

    w = np.zeros(2)
    b = 0
    alpha = 0.015
    loss = 0

    epochs = 500

    for epoch in range(epochs):
        yh = X @ w + b
        error = yh - y
        loss = np.sum(error ** 2) / (2 * len(X))

        dw = X.T @ error / len(X)
        db = np.mean(error)

        w -= alpha * dw
        b -= alpha * db

        if epoch % 50 == 0:
            print(f"epoch={epoch}, w={w}, b={b}, loss={loss:.2f}")

    # 预测新数据
    new_student = np.array([6, 8])
    new_y = new_student @ w + b
    print(new_y)


version1()
print('------------')
version2_np()