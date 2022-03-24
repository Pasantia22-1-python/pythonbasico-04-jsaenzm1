

class Persona:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print('Hello, mi name es {} and I am {} years old'.format(self.name, self.age))

if __name__ == '__main__':
    persona1 = Persona('Rocio', 22)

    print('Age: {}'.format(persona1.age))
    persona1.say_hello()

    