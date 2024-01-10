# inheritance.py

class Parent:
    hair_color = "brown"
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")