# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 17:32:31 2021

@author: Prince
"""
# Buyurtma qabul qilish

buyurtmalar = []

ishora = True

print ("Buyurtma berishni to'xtatish uchun 'Stop' sozini kiriting ")
while ishora :
    
    name = input("Buyurtma nomini kiriting : ")
    
    if name.lower() == "stop" :
        ishora = False 
    else: 
        buyurtmalar.append(name)

print (f"Siz bergan buyurtmalar {buyurtmalar}")

    
    

