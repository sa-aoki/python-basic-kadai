class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self, name, age):
        self.name = name
        self.age = age
        if self.age >= 20:
            print(f"{self.name}、 あなたは{self.age}才なので大人です。")
        else:
            print(f"{self.name}、 あなたは{self.age}才なので大人ではありません。")

# インスタンス化する
taro = Human("太郎", 25)
goro = Human("五郎",13)
hana = Human("はな", 55)
sakura = Human("さくら", 7)

taro.check_adult("太郎", 25)
goro.check_adult("五郎",13)
hana.check_adult("はな", 55)
sakura.check_adult("さくら", 7)