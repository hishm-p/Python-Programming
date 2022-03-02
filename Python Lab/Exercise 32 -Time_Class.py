from datetime import *
from time import time


class Time:
    def __init__(self, h, m, s):
        self._hour = h
        self._min = m
        self._sec = s

    def __add__(self, other):
        return timedelta(
            hours=self._hour, minutes=self._min, seconds=self._sec
        ) + timedelta(hours=other._hour, minutes=other._min, seconds=other._sec)


t1 = Time(2, 5, 45)
t2 = Time(0, 5, 20)


print(t1 + t2)