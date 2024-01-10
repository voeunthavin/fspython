# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)

print(miles.description())
print(miles.speak("Woof Woof"))
print(miles.speak('Bow Bow'))
print(miles.speak())
print(miles)

