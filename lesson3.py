# for文：リストの要素を1つずつ処理
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# range()で回数を指定して繰り返す
for i in range(5):
    print(i)

# リストとif文の組み合わせ
scores = [85, 42, 90, 60, 73]

for score in scores:
    if score >= 70:
        print(f"{score}点：合格")
    else:
        print(f"{score}点：不合格")