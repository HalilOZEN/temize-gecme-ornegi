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
