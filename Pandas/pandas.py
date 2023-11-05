# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


data = np.array(["Yunus", "Emre", "Senyigit"])
print("pd.Series(data)  =" + str(pd.Series(data)))
s = pd.Series(data, index=[1,2,3]) #indexleri 1 den başlayacak şekilde değiştirdik önceden 0 ile başlıyordu.
print("s  =" + str(s))

data2 = {"matematik":78,"fizik":62,"biyoloji":94}
s2= pd.Series(data2)
print("s2  =\n" + str(s2)) #index olarak matematik,fizik,biyoloji atadık.

s3= pd.Series(data2, index=["fizik","matematik","biyoloji"]) #datanın yerini değiştirdik.
print(s3)

s4= pd.Series(data2, index=["fiz","matematik","biyoloji"]) #index adı üsttekiyle farklı olursa değer döndüremeyecektir.
print(s4)


a = [10,20,30,40,50]
df = pd.DataFrame(a)
print("df  =" + str(df))

a2 = ["Yunus Emre",18,"Antalya"],["Bekir",16,"Konya"],["Mahmut",22,"Ankara"]
df2 = pd.DataFrame(a2, columns=["İsim","Yaş","Şehir"], index=[1,2,3])
print("df2  =\n" + str(df2))

a3 = {"İsim":["Yunus Emre","Bekir","Mahmut"],
      "Yaş":[18,16,22],
      "Şehir":["Antalya","Konya","Ankara"]}
df3 = pd.DataFrame(a3, columns=["İsim","Yaş","Şehir"], index=[1,2,3])
print("df3  =\n" + str(df3))
print("df3[İsim]  =\n" + str(df3["İsim"]))

del df3["Şehir"]

print("df3  =\n" + str(df3))
