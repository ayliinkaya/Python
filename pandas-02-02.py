# -*- coding: utf-8 -*-
#pandas modülü yükleniyor ve pd ismi veriliyor.
#pd modulü artık bir nesne gibi davranır.
import pandas as pd
#matplotlib modülü yükleniyor ve plt ismi veriliyor.
#plt modulü artık bir nesne gibi davranır.
import matplotlib.pyplot as plt

#pd modülünün CSV dosyasını okumasını sağlayabiliriz. 'read_csv' metodunu kullanırız.
#'read_csv' metodu CSV dosyasını okur ve bir DataFrame e dönüştürür.
#aşağıdaki kod satırında 'df' ismini vererek, dataframe RAM de kaydediliyor.
#df diye kullanabileceğimiz bir DataFrame nesnemiz var.
df = pd.read_csv(r'BTC-USD.csv')
df2 = pd.read_csv(r'fear-greed.csv')

#'df' ismindeki DataFrame'in 'Date' isimli sütunundaki verileri yazdırıyoruz.
sonVerininIndeksi = len(df)-1

gunSayisi = list(range(1,31))

fiyat = list(df["Close"][sonVerininIndeksi-30:sonVerininIndeksi])
sentiment = list(df2["Value"])

sentiment.reverse()

plt.subplot(2,1,1)
plt.plot(gunSayisi,fiyat)
plt.xticks(gunSayisi)

plt.xlabel("Gün")
plt.ylabel("BTC/USD")

plt.subplot(2,1,2)
plt.plot(gunSayisi,sentiment)
plt.xticks(gunSayisi)

plt.xlabel("Gün")
plt.ylabel("Sentiment")

plt.show()

#plt.xlim(1)