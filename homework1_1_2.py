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
            level="A" if(score>=90) else "B" if(score>=80) else "C" if(score>=70) else "D" if(score>=60) else "E"
            print(f'{score}：{level}級')
        
        else:
            if score==-1:
                continue
            print("請輸入 0-100 的數字！")
    except: 
        print("您輸入了非數字！")