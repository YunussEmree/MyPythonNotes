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

#del df3["Şehir"] #Şehir sütununu sildik
#df3.pop("Şehir") #üsttekine alternatif

print("df3  =\n" + str(df3))

print("**************")

print("df3.loc[1]  =\n" + str(df3.loc[1])) #indexi 1 olan kişinin bilgilerini yazdırdık
print("df3.iloc[0]  =\n" + str(df3.iloc[0])) #sırası 1 olan kişinin bilgilerini yazdırdık, indexten farklı olarak veri sırasına bakıyor

df4 = pd.concat([df2,df3])
print("df4  =\n" + str(df4)) #append metotu kaldırılmış. #DataFrame birleştirme methodu
print("**************")
print("df4.head(1)  =\n" + str(df4.head(1))) #en öndeki veriyi çağırma. Ne kadar belirtirsen o kadar veri çağırır.
print("df4.tail(1)  =\n" + str(df4.tail(1))) #en arkadaki veriyi çağırma. Ne kadar belirtirsen o kadar veri çağırır.



notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar)
print(notlar.loc[:5,"Test1":"Test4"]) #ilk 6 kişinin test notlarını getirme
print(notlar.loc[:5,["İsim","Final"]]) #ilk 6 kişinin isim ve finallerini getirme
print(notlar.loc[:5,:"Test2"]) #ilk 6 kişinin Test2 ye kadar olan tüm verileri getirme



films = pd.read_csv("imdb-1000.csv")
print(films.columns)
print(films[["title","star_rating"]].head())
print(films[films["star_rating"] > 8.5][["title","star_rating"]]) #imdb si 8.5 tan yüksek olan filmlerin isim ve imdb lerini getirme
print(films[(films["star_rating"] > 8.5) & (films["star_rating"] < 9.0)][["title","star_rating"]]) #imdb si 8.5 ile 9.0 arasında olan filmlerin isim ve imdb lerini getirme



















