# shapes.py

class Shape:
    def draw(self):
        print("도형을 그립니다.")

class Circle(Shape):
    def draw(self):
        print("원을 그립니다.")

class Rectangle(Shape):
    def draw(self):
        print("사각형을 그립니다.")
        
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹~")
