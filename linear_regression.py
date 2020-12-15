# linear regression, use numpy for matrix operations like inv, transpose, mul
# 2D array initialization and update
import numpy as np

if __name__ == '__main__':
    arr = input().split()
    m = int(arr[0])
    n = int(arr[1])
    X = []
    Y = []
    for _ in range(n):
        arr1 = [float(i) for i in input().split()]
        row = [1.0]
        for i in range(m):
            row.append(arr1[i])
        X.append(row)
        Y.append(arr1[m])
    t_n = int(input())
    # test_inp = [float(i) for i in input().split()]
    test = []
    for _ in range(t_n):
        test.append([1.0] + [float(i) for i in input().split()])
    X = np.array(X)
    Y = np.array(Y)
    X_T = X.T
    X_inv = np.linalg.inv(np.dot(X_T, X))
    B = np.dot(np.dot(X_inv, X_T), Y)

    test = np.array(test)

    ans = test.dot(B)
    for val in ans:
        print(round(val, 2))
