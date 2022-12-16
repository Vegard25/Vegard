# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:20:29 2022

@author: Vegard Sinaga
"""

import pandas as p

data = p.read_csv("Negara.csv")

df=p.DataFrame(data)
m= df.groupby(["Benua"]).mean()
s=df.groupby(["Benua"]).std()

m.to_csv('NegaraMean.csv')
s.to_csv("NegaraStandarDeviasi.csv")

print(df)
print(m)
print(s)
