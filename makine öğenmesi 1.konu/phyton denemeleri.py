
# # import datetime
# # tarih = input('araciniz kac gundur trafikte:   ')
# # tarih = tarih.split('/')
# # trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# # simdi = datetime.datetime.now()
# # fark =  simdi - trafigeCikis
# # days = fark.days

# # if days >=0 and days < 365:
# #     print('1.servis araligi')

# # elif days >=365 and days <= 365*2:
# #     print('2.servis araligi')

# # elif days >=365*2 and days <= 365*3:
# #     print('3.servis araligi')
# # else:
# #     print('hatali tarih')

# # names = 'Sadik turan'

# # for n in names:
# #     print(n)

 
# sayilar= [1,3,5,7,9,12,19,21]

# # 3 ün katı olanları bulma
# # for n in sayilar:
# #     if n % 3 == 0:
# #         print(n)    

# #sayilar listesindeki sayiların toplamı kaçtır

# # toplam = 0
# # for n in sayilar:
# #     toplam = n + toplam
# # print(toplam)

# #sayilar listesindeki tek sayıların karsini alma 

# for n in sayilar:
#     if n % 2 == 1:
#         t=n
#         n = n*n

#         print(t,n)

# sehirler=["samsun","izmir","ankara","istanbul","urfa"]
# #sehirlerden hangileri en az 5 harflidir.
# for sehir in sehirler:
#     if len(sehir)<=5:
#         print(sehir)

urunler =[
    {"name":"iphone 15pro max", "price":"90000"},
    {"name":"iphone 15pro ", "price":"80000"},
    {"name":"iphone 15", "price":"70000"},
    {"name":"iphone se2024", "price":"65000"},
    {"name":"iphone 14", "price":"50000"},
]
#ürünlerin fiyarları toplamı nedir

# toplam = 0
# for urun in urunler:
    
#     fiyat = int(urun['price'])
#     toplam = toplam + fiyat 

# print(toplam)    

#ürünlerden fiyatı en fazla 71000 olan ürünleri gösteriniz.

# for urun  in urunler:
#     fiyat = int(urun['price'])
#     if fiyat >= 70000:
#         print(urun)

#for item in range(50,100,10):
#    print(item)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("linear.csv")  # Verimizi okuyalım

print(data) # Veriyi inceleyelim.

x = data["metrekare"] # Metrekareleri bir axis' e çekelim, panda nın özelliği.
y = data["fiyat"] # Üstteki ile aynı.
x = pd.DataFrame.as_matrix(x) # NumPy matrisine dönüştürelim.
y = pd.DataFrame.as_matrix(y) # NumPy matrisine dönüştürelim.

print(x)
print(y) # Ne oluşturduğumuza bakmak önemli.

plt.scatter(x,y) # Ne oluşturduğumuza 2 boyutlu grafikte bakalım.

#Doğrumuzun denklemi y = m*a+b , Biz ise en uygun m ve b yi arıyoruz. m Eğim, b kesim noktası


m,b = np.polyfit(x,y,1)# NumPy bizim için grafiğe oturtuyor çizgimizi. Bunu matematiksel
# İşlemlerle uzun uzun da yapabilirdik. Fakat NumPy halihazırda sahip. Çok kafa karıştırmamak 
# Adına böylesi daha iyi.
# np.polyfit(x ekseni, y ekseni, kaçıncı dereceden polinom denklemi) ki biz birinci dereceden kullanacağız.


a = np.arange(150) # Denklemimiz hazır. a nın aralığını ayarlayalım.

plt.scatter(x,y) # Scatter ile nokta çizdirimi yapıyoruz.
plt.plot(m*a+b) # 


z = int(input("Kaç metrekare?"))
tahmin = m*z+b
print(tahmin)

plt.scatter(z,tahmin,c="red",marker=">")

plt.show()
print("y=",m,"x+",b)
