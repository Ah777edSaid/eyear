# my_script.py

class Greeter:
    def __init__(self, name):
        """المُنشئ (Constructor) لإعداد اسم الشخص"""
        self.name = name

    def greet(self):
        """وظيفة تطبع رسالة الترحيب"""
        print(f"Hello, {self.name}!")

if __name__ == "__main__":
    # إنشاء كائن (Object) من فئة Greeter
    greeter = Greeter("Ahmed")
    greeter.greet()  # سيطبع "Hello, Ahmed!"
