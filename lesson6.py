# ファイルに書き込む
with open("test.txt", "w") as f:
    f.write("1行目：こんにちは\n")
    f.write("2行目：Pythonの学習中\n")
    f.write("3行目：ファイル操作の練習\n")

print("書き込み完了")

# ファイルを読み込む
with open("test.txt", "r") as f:
    content = f.read()

print(content)

# 1行ずつ読み込む
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())