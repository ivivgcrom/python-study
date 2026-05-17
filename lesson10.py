import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 身長から体重を予測する線形回帰モデル

# 1. データを用意する
height = torch.tensor([[155.0], [160.0], [165.0], [170.0], [175.0],
                        [180.0], [185.0], [190.0]])
weight = torch.tensor([[55.0], [58.0], [62.0], [65.0], [68.0],
                        [72.0], [76.0], [80.0]])

# 2. モデルを定義する
model = nn.Linear(1, 1)   # 入力1つ、出力1つの線形モデル
print(f"初期の重み：{model.weight.data}")
print(f"初期のバイアス：{model.bias.data}")

# 3. 損失関数と最適化アルゴリズムを定義する
criterion = nn.MSELoss()          # 平均二乗誤差
optimizer = torch.optim.SGD(model.parameters(), lr=0.000001)

# 4. 学習する
losses = []
for epoch in range(1000):
    optimizer.zero_grad()          # 勾配をリセット
    prediction = model(height)     # 予測
    loss = criterion(prediction, weight)  # 損失を計算
    loss.backward()                # 逆伝播
    optimizer.step()               # パラメータを更新

    if epoch % 100 == 0:
        print(f"epoch {epoch}: loss = {loss.item():.4f}")
    losses.append(loss.item())

# 5. 結果を確認する
print(f"\n学習後の重み：{model.weight.data}")
print(f"学習後のバイアス：{model.bias.data}")

# 6. 予測してみる
test = torch.tensor([[172.0]])
result = model(test)
print(f"\n身長172cmの予測体重：{result.item():.1f}kg")

# 7. 損失の推移をグラフで表示する
plt.plot(losses)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("training loss")
plt.savefig("loss.png")
print("loss.pngを保存しました")