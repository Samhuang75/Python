# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def X():
    str1=""
    for i in range(1,10):
        for j in range(1,10):
            str1+="{}*{}={:2d}".format(i, j, i*j)+"   "
        str1+= '\n'
    return str1
result=X()
print(result)

