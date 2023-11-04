# -*- coding: utf-8 -*-
import numpy as np


liste = [1,3,5,7,8,11,12,18]

#15 e kadar olan sayıların listesini oluşturma
a = np.arange(15)
print("a  =" + str(a))
print("a type  =" + str(type(a))) #numpy.ndarray
print("a reshape 3,5  =" + str(a.reshape(3,5))) #a listesini 3 satır 5 sütun şeklinde düzenleyip yazdırdık
print("a dimension count  =" + str(a.reshape(3,5).ndim)) #a reshape in boyut sayısını alma : 2

b = np.arange(10)
print("b shape  =" + str(b.shape)) 
print("b dimension count  =" + str(b.ndim)) #b nin boyutunu alma : 1