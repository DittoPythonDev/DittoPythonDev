# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:14:14 2021

@author: Prince
"""
#Nesting

shaxslar = []

for n in range(4) :
    shaxs = {"ism-sharifi" : None ,
                "tug'ilgan joyi" : None , 
                "tugilgan yili" : None ,
                "umri" : None       
                }
    shaxslar.append(shaxs)

n=1
for shaxs in shaxslar:
    
    shaxs["ism-sharifi"] = input(str(n) + " - ismni kiriting ")
    shaxs["tugilgan yili"] = input("tugilgan yilini kiriting ")
    shaxs["tug'ilgan joyi"] = input("tugilgan joyini kiriting ")
    shaxs["umri"] = input("yashagan umrini kiriting ")
    n+=1
    
print(shaxslar)
        

    
