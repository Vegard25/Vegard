# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:30:54 2022

@author: Vegard Sinaga
"""

class mhs:
    def __init__(self, nama='none', nilai='none'):
        self.nama = nama
        self.nilai= nilai  
    def Displaymhs(self):
        print('the name is',self.nama)
        print('the grade is',self.nilai)
    @property
    def fname(self):
        print('Getting name')
        return self.nama
        return self.nilai        
    @fname.setter
    def cnama(self, value):
        print('data changed to ' + value)
        self.nama = value 
