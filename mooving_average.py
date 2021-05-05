import numpy as np


def running_mean(x, N):
    out = np.zeros_like(x, dtype=np.float64)
    dim_len = x.shape[0]
    for i in range(dim_len):
        if N % 2 == 0:
            a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 2
        else:
            a, b = i - (N - 1) // 2, i + (N - 1) // 2 + 1
        a = max(0, a)
        b = min(dim_len, b)
        out[i] = np.mean(x[a:b])
    return out


def stand(a, num=1):
    for i in range(num):
        a = (a - a.mean()) / (a.std())
    return a


def from_csv_to_nparray(path):
    myarray = np.recfromcsv(path, dtype=float)
    data = np.array([None, None])
    for i in range(len(myarray)):
        a = np.hstack((myarray[i][0], myarray[i][1]))
        data = np.vstack((data, a))
    data = np.delete(data, 0, axis=0)
    return data


data = from_csv_to_nparray(r'D:\data\test.csv')
track = data[:, 0]
signal = data[:, 1]
last = None
x = np.array([])
y = np.array([])
y_ones = np.ones(track.shape)
z = np.array([])
scale = track[-1] / len(track)
len_window = 3
while len_window <= track.shape[0]:
    Fi = running_mean(signal, len_window)
    Fost = stand(signal - Fi)
    z = np.hstack((z, Fost))
    x = np.hstack((x, track))
    y = np.hstack((y, y_ones * (-((len_window - 1) * scale) / (2 ** 0.5))))
    len_window += 2
data = np.vstack((x, y, z))
data = data.transpose()
np.savetxt(r'D:\data\result.csv', data, delimiter=",")
