#クラスについて勉強する
class Student:
    def __init__(self, name, age):  #selfはインスタンス自身を指す
        #nameとage　→　メンバ変数(属性)
        self.name = name    #メンバ関数(メソッド)
        self.age = age
    
    def profile(self):
        print(f"私の名前は{self.name}です")
    
    def get_age(self):
        return self.age
    
student1 = Student("永所康太朗", 20)    #studentクラスを持つ新しいインスタンスを作成
print(student1.name)    #student1のname属性を取得
student1.profile()
print(student1.get_age())