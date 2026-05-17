# 関数：処理をまとめて名前をつけたもの
def greet(name):
    print(f"こんにちは、{name}さん！")

greet("iviv")
greet("田中")

# 戻り値のある関数
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# 複数の処理をまとめた関数
def check_score(score):
    if score >= 70:
        return "合格"
    else:
        return "不合格"

print(check_score(85))
print(check_score(50))