# 1
name = "iviv"
age = 26
height = 1.72

print(f"name: {type(name)}")
print(f"age: {type(age)}")
print(f"height: {type(height)}")
print(f"私は{name}です。{age}歳、身長{height}cmです。")

# 2
foods = ["hamburger", "ramen", "sushi", "pizza", "curry"]
for favorite in foods:
    print(f"{favorite}が好きです。")

# 3
score = 60
if score >= 90:
    print("S")
elif score >=70:
    print("A")
elif score >= 50:
    print("B")
else:
    print("C")

# 4
a = 10
b = 30

def analyze(a, b):
    print(f"合計：{a + b}")
    print(f"平均：{(a + b) / 2}")
    print(f"最大値：{max(a, b)}")

analyze(a, b)

# 5
class Car:
    def __init__(self, maker, speed):
        self.maker = maker
        self.speed = speed

    def drive(self):
        print(f"{self.maker}が時速{self.speed}kmで走っています。")

car1 = Car("トヨタ", 120)
car2 = Car("ホンダ", 150)

car1.drive()
car2.drive()