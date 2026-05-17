import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

# 1. データの準備
transform = transforms.Compose([
    transforms.ToTensor(),               # 画像をテンソルに変換
    transforms.Normalize((0.5,), (0.5,)) # 値を-1〜1に正規化
])

# 訓練データ
train_data = torchvision.datasets.MNIST(
    root = "./data", train = True,
    download = True, transform = transform
)

# テストデータ
test_data = torchvision.datasets.MNIST(
    root = "./data", train = False,
    download = True, transform = transform
)

# DataLoader：データをミニバッチに分割する
train_loader = torch.utils.data.DataLoader(
    train_data, batch_size = 64, shuffle = True
)
test_loader = torch.utils.data.DataLoader(
    test_data, batch_size = 64, shuffle = False
)

print(f"訓練データ数：{len(train_data)}")
print(f"テストデータ数：{len(test_data)}")
print(f"画像のサイズ：{train_data[0][0].shape}")

# 2. モデルの定義
class MNISTModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Flatten(),           # 28×28を784次元に変換
            nn.Linear(784, 128),    # 784→128
            nn.ReLU(),              # 活性化関数
            nn.Linear(128, 64),     # 128→64
            nn.ReLU(),              # 活性化関数
            nn.Linear(64, 10)       # 64→10（0〜9の10クラス）
        )

    def forward(self, x):
        return self.layers(x)

# 3. モデル・損失関数・最適化アルゴリズムの定義
model = MNISTModel()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print(model)

# 4. 学習
for epoch in range(5):
    total_loss = 0
    for images, labels in train_loader:
        optimizer.zero_grad()
        output = model(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"epoch {epoch+1}: loss = {avg_loss:.4f}")

# 5. 精度確認
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        output = model(images)
        predicted = torch.argmax(output, dim=1)
        correct += (predicted == labels).sum().item()
        total += labels.size(0)

print(f"\nテスト精度：{100 * correct / total:.2f}%")