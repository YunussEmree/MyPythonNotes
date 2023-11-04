# -*- coding: utf-8 -*-
import numpy as np


liste = [1,3,5,7,8,11,12,18]

#15 e kadar olan sayıların listesini oluşturma
a = np.arange(15)
print("a  =" + str(a))
print("a type  =" + str(type(a))) #numpy.ndarray
print("a reshape 3,5  =" + str(a.reshape(3,5))) #a listesini 3 satır 5 sütun şeklinde düzenleyip yazdırdık
print("a dimension count  =" + str(a.reshape(3,5).ndim)) #a reshape in boyut sayısını alma : 2

b = np.arange(1,10) #1 den 10 a kadar olan tam sayılarla liste oluşturma, 1 dahil 10 dahil değil
print("b shape  =" + str(b.shape)) 
print("b dimension count  =" + str(b.ndim)) #b nin boyutunu alma : 1


c = np.array([1,3,6,8,9]) #kendi np arrayimizi oluşturduk [] koyma sebebimiz bu methodun tek parametre istemesi eğer koymazsak çok parametre olarak algılıyor.