#変数と型
name = "iviv" #str
age = 20 #int
height = 1.75 #float
is_student = True #bool

print(name)
print(age)
print(height)
print(is_student)


# 型を確認する
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# 計算
print(age + 5)        # 足し算
print(height * 2)     # 掛け算
print(age / 3)        # 割り算
print(age % 3)        # 余り


# 文字列の操作
greeting = "Hello"
print(greeting + " " + name)   # 文字列の結合
print(len(name))                # 文字数を数える
print(name.upper())             # 大文字に変換
print(f"私の名前は{name}、年齢は{age}歳です")  # f文字列


# リスト：順番のあるデータの集まり
fruits = ["apple", "banana", "cherry"]

print(fruits)           # リスト全体
print(fruits[0])        # 最初の要素（0番目）
print(fruits[2])        # 3番目の要素
print(len(fruits))      # 要素数


# リストの操作
fruits.append("grape")  # 末尾に追加
print(fruits)

fruits.remove("banana") # 削除
print(fruits)