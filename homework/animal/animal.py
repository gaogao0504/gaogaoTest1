"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】 111111
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】111
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2、使用yaml 来管理猫猫，狗狗的属性
"""

# 创建一个动物类
import yaml


class Animal:
    # 属性名称
    name = "tom"
    color = "pink"
    age = 1
    sex = "female"

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 类方法
    def shout(self):
        print("我会叫")

    def run(self):
        print("running")


"""
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】 111111
"""


# 创建子类
class Cat(Animal):
    # 定义新的属性
    fur = "short"

    # 复用父类方法
    def __init__(self, name, color, age, sex, fur):
        self.fur = fur
        super().__init__(name, color, age, sex)

    def shout(self):
        print(f"{self.name}会喵喵叫")

    def catch(self):
        print(f"{self.name}会捉老鼠")


"""
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】 1111
"""


class Dog(Animal):
    fur = "long"

    def __init__(self, name, color, age, sex, fur):
        self.fur = fur
        super().__init__(name, color, age, sex)

    def shout(self):
        print(f"{self.name}会汪汪叫")

    def watch_home(self):
        print(f"{self.name}会看家")


"""
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2 使用yaml 来管理猫猫，狗狗的属性
"""
if __name__ == '__main__':
    with open("animal.yaml") as f:
        # yaml.safe_load() 是将yaml格式转换为python对象
        animals = yaml.safe_load(f)
        cat = animals["default"]
        dog = animals["default1"]
    # cat = Cat(animals["cats"][0]["name"], animals["cats"][0]["color"], animals["cats"][0]["age"], animals["cats"][0]["sex"] , animals["cats"][0]["fur"])
    cat = Cat(cat["name"], cat['color'], cat['age'], cat['sex'], cat['fur'])
    print(f"猫猫的名字是：{cat.name} \n猫猫的颜色是：{cat.color}\n猫猫的年龄为：{str(cat.age)} 岁\n猫猫的性别为:{cat.sex} \n猫猫的毛发为：{cat.fur}")
    cat.catch()
    dog = Dog(dog["name"], dog['color'], dog['age'], dog['sex'], dog['fur'])
    print(f"狗狗的名字是：{dog.name} \n狗狗的颜色是：{dog.color}\n狗狗的年龄为：{str(dog.age)} 岁\n狗狗的性别为:{dog.sex} \n狗狗的毛发为：{dog.fur}")
    dog.watch_home()
