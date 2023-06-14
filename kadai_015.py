class Human:
    #コンストラクタを定義する
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #メソッドを定義する
    def show_info(self):
        print(self.name,self.age)

#インスタンス化する
human = Human("花子", 25)

#メソッドにアクセスして実行する
human.show_info()




