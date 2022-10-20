# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:54:38 2022

@author: Vegard Sinaga
"""
umur="0"
total=0
while (umur!=""):
    umur= int(input("masukan umur: "))
    if umur!='':
        umurangka= int(umur)
        if umurangka<= 2:
            print("gratis")
            harga=0
        elif umurangka>= 3 and umurangka<= 12:
            print("harga= 14 dollar")
            harga= 14 
        elif umurangka>= 65:
            print("harga= 18 dollar")
            harga= 18
        else:
            print("harga= 23 dollar")
            harga= 23
        total= total+harga
        print("total %0.3f"%total)
    jumlah= int(input("masukan jumlah uang:"))
    hasil= jumlah-total
    print("kembalian %0.3f"%hasil)
    
        
        