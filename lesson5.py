# クラス：データと関数をまとめた設計図
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"こんにちは、{self.name}です。{self.age}歳です。")

    def is_adult(self):
        if self.age >= 18:
            return "成人です"
        else:
            return "未成年です"

# クラスからインスタンスを作成
person1 = Person("iviv", 20)
person2 = Person("田中", 15)

person1.greet()
person2.greet()

print(person1.is_adult())
print(person2.is_adult())