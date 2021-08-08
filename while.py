# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 17:19:31 2021

@author: Prince
"""

dostlar = {}
ishora = True

while ishora :
    ism = input("DO'stingizni ismini kiriting :")
    yosh = input("Do'stingizni yoshini kiriting :")
    dostlar[ism] = int(yosh)
    
    javob = input("Yana do'stingizni qoshasizmi (HA/YOQ)")
    
    if javob == "YOQ" :
        ishora = False

for ism , yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

