import numpy as np
import matplotlib.pyplot as plt


# x_train = np.array([[1, 1], [2, 2.5], [3, 1.2], [5.5, 6.3], [6, 9], [7, 6]])
# y_train = np.array(['red', 'red', 'red', 'blue', 'blue', 'blue'])
# x_test = [3, 3.5]


def plot(x_train, y_train, x_test):
    plt.figure()
    plt.scatter(x_train[:, 0], x_train[:, 1], s=170, color=y_train[:])
    plt.scatter(x_test[0], x_test[1], s=170, color='green')
    plt.show()


def dist(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


def nnc(x_train, y_train, x_test):
    num = len(x_train)
    distance = np.zeros(num)
    for i in range(num):
        distance[i] = dist(x_train[i], x_test)
    min_index = np.argmin(distance)
    return y_train[min_index]
