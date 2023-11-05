# -*- coding: utf-8 -*-
import numpy as np
#numpy docs: https://numpy.org/doc/stable/user/quickstart.html


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
print("c  =" + str(c))
print("c.dtype  =" + str(c.dtype))

c = np.array([1.2,3,6,8,9])
print("c  =" + str(c)) #tek bir değer float olursa tüm intleri floata çeviriyor
print("c.dtype  =" + str(c.dtype))

c = np.array([1.2,"3",6,8,9])
print("c  =" + str(c)) #tek bir değer string olursa tüm değerleri stringe çeviriyor
print("c.dtype  =" + str(c.dtype))
#yani tüm data türlerini aynı yapmaya çalışıyor


d = np.array([[2,3],[5,1],[4,1]])
print("d  =" + str(d))
print("d ndim  =" + str(d.ndim))


e = np.linspace(1,10) #1 ile 10 dahil olmak üzere 50 tane eşit aralıklı sayı oluşturup listeliyor
print("e  =" + str(e))

e = np.linspace(1,10,10) #1 ile 10 dahil olmak üzere 10 tane eşit aralıklı sayı oluşturup listeliyor
print("e  =" + str(e))

e = np.linspace(1,10,5) #1 ile 10 dahil olmak üzere 5 tane eşit aralıklı sayı oluşturup listeliyor
print("e  =" + str(e))


f = np.array([20,30,40,50])
g = np.arange(4)

print("f-g  =" + str(f-g)) #f elemanlarından g elemanlarının çıkarılma sonucu
print("g**2  =" + str(g**2)) #g nin elemanlarının karesi işlemi
print("10*np.sin(a)  =" + str(10*np.sin(g)))
print("f@g  =" + str(f@g)) #f ile g nin matris çarpımı
print("f.dot(g)  =" +  str(f.dot(g))) #f ile g nin matris çarpımına alternatif metot

print("np.ones((2,5))  =" + str(np.ones((2,5)))) #2 satır 5 sütunluk 1 lerden oluşan bir matris yazdırdık
print("np.zeros((2,5))  =" + str(np.zeros((2,5)))) #2 satır 5 sütunluk 0 lerden oluşan bir matris yazdırdık
print("np.random.random(2,5)  =" + str(np.random.random((2,5)))) #0 ile 1 arasında rastgele sayılarla 2 satır 5 sütunluk bir matris yazdırdık
print("np.sum(g)  =" + str(np.sum(g))) #tüm g elemanlarını toplama
print("g.sum()  =" + str(g.sum())) #üsttekine alternatif
print("np.min(g)  =" + str(np.min(g))) #g nin minimum değerini döndürür
print("np.max(g)  =" + str(np.max(g))) #g nin maksimum değerini döndürür
print("np.sqrt(g)  =" + str(np.sqrt(g))) #g değerlerinin kareköklerini alma


sayilar = np.array([2,4,6,8,10,12,14])
print("sayilar[0]  =" + str(sayilar[0])) #1. elemanı alma
print("sayilar[0:3]  =" + str(sayilar[0:3])) #1. elemandan 4. elemana kadar olan sayıları alma. 4. eleman dahil değil.
print("sayilar[]::-1]  =" + str(sayilar[::-1])) #sayilar listesini tersten sırala

sayilar2 = np.array([[2,4,6],[8,10,12]])
print("sayilar2[0]  =" + str(sayilar2[0])) #1. elemanı alma
print("sayilar2[0,2]  =" + str(sayilar2[0,2])) #1. elemanın 3. elemanını alma
print("sayilar2[:,2]  =" + str(sayilar2[:,2])) #tüm elemanların 3. elemanını alma
print("sayilar2[:,0:2]  =" + str(sayilar2[:,0:2])) #tüm elemanların 1. elemanından 3. elemanına kadar olan sayıları alma
print("sayilar2[::-1,::-1]  =" + str(sayilar2[::-1,::-1])) #elemanları ve elemanların elemanlarını tersten sırala
print("sayilar2[:,::-1]  =" + str(sayilar2[:,::-1])) #sadece elemanların elemanlarını tersten sırala
print("sayilar2[-1,:]  =" + str(sayilar2[-1,:])) #son elemana ulaşma
print("sayilar2[-1,-1]  =" + str(sayilar2[-1,-1])) #son elemanın son elemanına ulaşma
print("sayilar2[-1,0]  =" + str(sayilar2[-1,0])) #son elemanın ilk elemanına ulaşma


h = np.floor(10*np.random.random((3,4))) #0 dan 10 a kadar olan rastgele sayıların tam değeriyle oluşturulup 3 satır 4 sütunluk bir matris yazdırma
print("h  =" + str(h))
print("h.shape  =" + str(h.shape)) # (3,4)
print("h.ravel()  =" + str(h.ravel())) #boyutunu 1 e indirerek değerleri yazma
h = h.ravel()
print("h.reshape(2,6)  =" + str(h.reshape(2,6)))
h = h.reshape(2,6)
print("h.T  =" + str(h.T)) #transpose alma -> 2 satır 6 sütunluk matrixi 6 satır 2 sütun halina getirme
print("h.reshape(2,-1)  =" + str(h.reshape(2,-1))) #sütun sayısı 2 olsun satır sayısını da ona göre ayarla demek


i1 = np.floor(10*np.random.random((2,3)))
i2 = np.floor(10*np.random.random((2,3)))
print("i1  =" + str(i1))
print("i2  =" + str(i2)) 

i3 = np.vstack((i1,i2)) #vertical stack -> dikey biçimde verileri ekleme işlemi
print("i3  =" + str(i3))
i4 = np.hstack((i1,i2)) #horizontal stack -> yatay biçimde verileri ekleme işlemi
print("i4  =" + str(i4))



k = np.arange(10)
print("k  =" + str(k))

l = k

print("l  =" + str(l))

l[0] = 100
print("k  =" + str(k))
print("l  =" + str(l))
#k yı değiştirmememize rağmen bu nasıl oldu?: aslında k nın değeri bellekte bir yer ve sen l yi k ya eşitlersen ikisini de aynı bellek kısmına atamış oluyorsun. Bu yüzden bir değerden değişince diğerinden de değişmiş oluyor.
#olayın adı: referans ataması
#bunun olmasını istemiyorsak:
    
    
k = l.copy() #k artık l nin kopyası ve birinden değer değişince diğerini etkilemeyecek
print("k  =" + str(k))
k[0] = 1000
print("k  =" + str(k))
print("l  =" + str(l))
    
    
    
m = k.view() #m k nın görünüşüne sahip fakat birinde boyut değiştirirsek diğerinde değişmiyor.
print("m  =" + str(m))
print("k  =" + str(k))
m[0] = 250
print("m  =" + str(m))
print("k  =" + str(k))
m.shape = 2,5
print("m  =" + str(m))
print("k  =" + str(k))
    
    
    
    
    
    
    
    
 






















