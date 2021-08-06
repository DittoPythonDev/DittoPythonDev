# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 8:25:05 2021

@author: Prince
"""

# cars = {
#         "BMW" : "blue" , "audi" : "black" ,
#         "mercedes" : "red" , "porche" : "orange" , 
#         "chevrolet" : "white" , "ferrari" : "red",
#         "lamborgini" : "yellow"   
#         }

# for car in sorted(cars.keys()):
#     print(car.title())
    
countries  = {"Uzbekistan" : "Tashkent" , 
              "AQSH" : "New York" , 
              "Russia" : "Moscow" ,
              "Canada" : "Ottawa" ,
              "Germany" : "Berlin" ,
              "Brazil" : "Brasilia" ,
              "Turkey" : "Istanbul" ,
              "India" : "New Delhi" ,
              "Poland" : "Warsaw" ,
              "Spain" : "Madrid" ,
              }

country = input("Davlat nomini kiriting ")

for name in countries:
    if name.upper() == country.upper():
        capital = countries[name]
        print(f"Siz kiritgan davlatning poytaxti {capital}")
        break
    else:
        print("Kechirasiz unday davlat ro'yhatimizda mavjud emas")
        break
                

    
    



      
