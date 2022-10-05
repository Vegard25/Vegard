# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:12:53 2022

@author: Vegard Sinaga
"""

import math
print("\nPROGRAM INI AKAN MENGHITUNG PERSAMAAN KUADRAT")
print("=============================================")
print("!!!PETUNJUK!!!")
print("ax^2+bx+c = 0")
a = int(input("\nMasukkan koefisien a: "))
b = int(input("Masukkan koefisien b: "))
c = int(input("Masukkan koefisien c: "))
determinan = b**2 - 4*a*c
if a == 0: 
    print("ini bukan persamaan kuadrat")
elif determinan == 0:
    print("Determinannya adalah: ",determinan)
    print("\nTermasuk jenis akar-akar kembar dan real")
    print("-----------------------------------")
    x1 = -b/2*a
    x2 = -b/2*a
    print("Akar-akarnya adalah x1 : ",x1,"dan x2 : ",x2)
elif determinan > 0:
    print("Determinannya adalah: ",determinan)
    print("\nTermasuk jenis akar-akar berbeda dan real")
    print("-----------------------------------")
    x1 = (-b + math.sqrt(determinan))/2*a
    x2 = (-b - math.sqrt(determinan))/2*a
    print("Akar-akarnya adalah x1 : ",x1," dan x2 : ",x2)
else:
    print("\nTermasuk jenis akar-akar tidak real atau imajiner.")
    print("-----------------------------------")
    print("Akar x1 = -",b,"+ Akar ",determinan,"/2 *",a)
    print("Akar x2 = -",b,"- Akar ",determinan,"/2 *",a)