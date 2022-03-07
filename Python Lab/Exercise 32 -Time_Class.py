from datetime import *

class Time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__min = m
        self.__sec = s

    def __add__(self, other):
        return timedelta(hours=self.__hour, minutes=self.__min, seconds=self.__sec) + timedelta(hours=other.__hour, minutes=other.__min, seconds=other.__sec)


t1 = Time(2, 5, 45)
t2 = Time(0, 5, 20)


print(t1 + t2)
