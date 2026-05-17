# 辞書：名前と値のペアで管理するデータ
person = {
    "name": "iviv",
    "age": 20,
    "height": 1.75
}

print(person)               # 辞書全体
print(person["name"])       # 名前で取得
print(person["age"])        # 年齢を取得

# 辞書の操作
person["weight"] = 60       # 新しいキーを追加
print(person)

person["age"] = 21          # 値を更新
print(person["age"])


# 条件分岐
age = 20

if age >= 18:
    print("成人です")
else:
    print("未成年です")

# 複数条件
score = 75

if score >= 90:
    print("優")
elif score >= 70:
    print("良")
elif score >= 50:
    print("可")
else:
    print("不可")