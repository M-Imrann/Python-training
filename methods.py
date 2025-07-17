from datetime import date


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def BirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    @staticmethod
    def Adult(age):
        return age >= 18

    @property
    def Calculate_BirthYear(self):
        return (date.today().year - self.age)


person = Parent('Ali', 24)

person1 = Parent.BirthYear('Imran', 1996)

print(f"Person1 Age: {person.age}")
print(f"Person2 Age: {person1.age}")
print(f"Person 1 Birth year is : {person.Calculate_BirthYear}")
print(f"Person 2 Birth year is : {person1.Calculate_BirthYear}")

print(f"Is Person1 an adult? {'Yes' if Parent.Adult(person.age) else 'No'}")
print(f"Is Person2 an adult? {'Yes' if Parent.Adult(person1.age) else 'No'}")
