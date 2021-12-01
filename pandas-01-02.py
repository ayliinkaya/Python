# -*- coding: utf-8 -*-
#pandas modülü yükleniyor ve pd ismi veriliyor.
#pd modulü artık bir nesne gibi davranır.
import pandas as pd

#pd modülünün CSV dosyasını okumasını sağlayabiliriz. 'read_csv' metodunu kullanırız.
#'read_csv' metodu CSV dosyasını okur ve bir DataFrame e dönüştürür.
#aşağıdaki kod satırında 'df' ismini vererek, dataframe RAM de kaydediliyor.
#df diye kullanabileceğimiz bir DataFrame nesnemiz var.
df = pd.read_csv(r'BTC-USD.csv')

#'df' ismindeki DataFrame'in 'Date' isimli sütunundaki verileri yazdırıyoruz.
print(df["Date"])

#'df' ismindeki DataFrame'in 'Date' isimli sütunundaki ilk satırdaki veriyi yazdırıyoruz.
print(df["Date"][0])

#'df' ismindeki DataFrame'in 'Date' isimli sütunundaki en son veriyi yazdırıyoruz.
print(df["Date"][len(df)-1])