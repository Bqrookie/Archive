# coding=utf-8
from collections import Iterable


class Person(object):

    def __init__(self):
        self.count = 0
        self.names = list()

    def add_per(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.names):
            result = self.names[self.count]
            self.count += 1
            return result
        else:
            raise StopIteration

if __name__ == '__main__':

    per = Person()
    per.add_per('老A')
    per.add_per('老B')
    per.add_per('老C')

    for item in per:
        print(item)

    # print('是否可迭代对象：', isinstance(per, Iterable))
    # perper = iter(per)
    # print('是否迭代器：', isinstance(perper, Iterable))