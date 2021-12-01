# -*- coding: utf-8 -*-
#pandas modülü yükleniyor ve pd ismi veriliyor.
#pd modulü artık bir nesne gibi davranır.
import pandas as pd

#pd modülünün CSV dosyasını okumasını sağlayabiliriz. 'read_csv' metodunu kullanırız.
#'read_csv' metodu CSV dosyasını okur ve bir DataFrame e dönüştürür.
#aşağıdaki kod satırında 'df' ismini vererek, dataframe RAM de kaydediliyor.
#df diye kullanabileceğimiz bir DataFrame nesnemiz var.
df = pd.read_csv(r'BTC-USD.csv')

#Pandas DataFrame nesnesinde bulunan tablo veriyi eğer 'command prompt' diğer adıyla 'console' uyumlu yazdırmak istersek 'to_string' metodunu kullanırız.
metin = df.to_string()

print(metin)
"""----------------------------------------------------"""
#print(type(df))
#print(type(metin))