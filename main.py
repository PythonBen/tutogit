""" testing git and pycharm"""
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    def __repr__(self):
        return f'Person({self.name},{self.age})'


if __name__ == '__main__':
    print('hello version control')
    p = Person('bob', 20)
    print(p)
