class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")


class Circle():
    pi=3.14
    def __init__(self, radius):
        self.radius = radius
    
    def get_circumference(self):
        return 2 * Circle.pi * self.radius
    
mycircle = Circle(5)
print("The circumference of the circle is " + str(mycircle.get_circumference()) + ".")