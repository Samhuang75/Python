# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
score = 0

while score != -1:
    
    try:
        score=float(input("請輸成績<結束-1>"))
        
        if(score<=100 and score>=0):
            compare=score//10
            match compare:
                case 10 | 9:level="A"
                #case 9:level="A"
                case 8:level="B"
                case 7:level="C"
                case 6:level="D"
                case _:level="E"
            
            print(f'{score}：{level}級')
        
        else:
            if score==-1:
                continue
            print("請輸入 0-100 的數字！")
    except: 
        print("您輸入了非數字！")