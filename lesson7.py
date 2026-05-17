# Numpy 
import numpy as np

# NumPy配列の作成
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Pythonのリストとの違い
python_list = [1, 2, 3, 4, 5]
print(python_list * 2)   # リストは繰り返しになる
print(arr * 2)            # NumPyは全要素に掛け算される

# 2次元配列（行列）
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(matrix)
print(matrix.shape) # 形状（2行3列）

import numpy as np

# よく使う統計計算
data = np.array([10, 20, 30, 40, 50])
print(np.mean(data))    # 平均
print(np.max(data))     # 最大値
print(np.min(data))     # 最小値
print(np.sum(data))     # 合計

# ゼロ配列・1配列（深層学習でよく使う）
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
print(zeros)
print(ones)

# Pandas
import pandas as pd

# DataFrameの作成（表形式のデータ）
data = {
    "名前": ["iviv", "田中", "鈴木"],
    "年齢": [20, 15, 30],
    "スコア": [85, 42, 90]
}

df = pd.DataFrame(data)
print(df)
print()

# 列を取り出す
print(df["スコア"])
print()

# 条件で絞り込む
print(df[df["スコア"] >= 70])