import torch

# テンソルとは深層学習における基本的なデータ構造です
# NumPyの配列に似ていますが、GPU計算ができます

# 1次元テンソル
t1 = torch.tensor([1.0, 2.0, 3.0])
print(t1)
print(t1.dtype)   # データ型
print(t1.shape)   # 形状

# 2次元テンソル（行列）
t2 = torch.tensor([[1.0, 2.0],
                   [3.0, 4.0]])
print(t2)
print(t2.dtype)   # データ型
print(t2.shape)   # 2行2列

# よく使う初期化
zeros = torch.zeros(3, 3)
ones = torch.ones(2, 4)
rand = torch.rand(2, 3)   # 0〜1のランダム値
print(zeros)
print(ones)
print(rand)

# テンソルの計算
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print(a + b)       # 足し算
print(a * b)       # 掛け算（要素ごと）
print(torch.dot(a, b))  # 内積（深層学習でよく使う）

# NumPyとの変換
import numpy as np
numpy_arr = a.detach().numpy()        # テンソル→NumPy
print(numpy_arr)
print(type(numpy_arr))

tensor_from_numpy = torch.from_numpy(numpy_arr)  # NumPy→テンソル
print(tensor_from_numpy)