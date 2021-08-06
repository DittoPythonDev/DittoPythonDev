# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 13:52:18 2021

@author: Prince
"""

#Nesting2

davlatlar = {
    
    "Ispaniya" : {
                    "poytaxt" : "Madrid" ,
                    "hududi" : "329750 km.kv" , 
                    "aholisi" : "15456781 mln "
                    } ,
    
    "Uzbekistan" : {"poytaxti" : "Tashkent" ,
                    "hududi" : "329302 kv.km",
                    "aholisi" : "33000000 mln "        
                    } ,
    
    "Rossiya" : {"poytaxti" : "Moskow" ,
                 "hududi" : "315465124 kv.km" ,
                 "aholisi" : "214578156 mln"
                }        
    }

# print(davlatlar)

davlat = input("Davlat nomini kiriting ")
if davlat in davlatlar:
    print(davlatlar[davlat])
else:
    print("Bunday davlat mavjud emas")
    

