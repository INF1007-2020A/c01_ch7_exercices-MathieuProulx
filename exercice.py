#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import turtle
import ch6

def ellipsoide(a=1, b=1, c=1, v=1):
    volume =  (4/3) * a * b * c * math.pi
    masse = volume * v

    return volume, masse

def sort(sequence: str) -> tuple:
    return sorted(histogram(sequence).items(), key=lambda x: x[1])[-1]

if __name__ == '__main__':
    print(ellipsoide(4,5,1,0.75))
    pass
