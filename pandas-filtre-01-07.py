import numpy as np
import pandas as pd
df = pd.DataFrame({'isim':['Ahmet','Filiz','Ayşe','Mine','Emine','Can','Canan'],
'kategori':['A','A','C','B','B','C','B'],
'deger':np.random.random(7).round(2),
'deger2':np.random.randint(1,10, size=7)
})
print(df)
# metod 1 matematiksel operatörler ile
#yeniDF = df[(df.deger > 0.5)]
#print(yeniDF)

#yeniDF = df[(df.isim > 'C')] #isim sütunundaki isimlerin baş harfi C den büyük olan isimleri getirir. (C harfiyle başlayanlar da dahil edilir) 
#print(yeniDF)

# metod 2 & ve - | veya
#yeniDF = df[(df.deger > 0.5) & (df.deger2 >=3)]
#print(yeniDF)

#yeniDF = df[(df.deger < 0.5) | (df.deger2 > 7)]
#print(yeniDF)

# metod 3 belirli isimlere göre getir. ISIN metoduyle ...
#isimler = ['Ayşe','Ahmet','Can']
#yeniDF = df[(df.isim.isin(isimler))]
#print(yeniDF)

# metod 4 startswith veya contains metodları
#yeniDF = df[(df.isim.str.startswith('A'))]
#print(yeniDF)

#yeniDF = df[(df.isim.str.contains('i'))]
#print(yeniDF)

#metod 5 ~ NOT 
#yeniDF = df[(~df.isim.str.startswith('A'))]
#print(yeniDF)

#yeniDF = df[(~df.isim.str.contains('i'))]
#print(yeniDF)

#metod 6 nlargest nsmallest
#yeniDF = df.nlargest(3,'deger') # en büyük değere sahip ilk 3 tanesi
#print(yeniDF)

#yeniDF = df.nlargest(len(df)-1,'deger') # en büyük değere sahip tüm diziyi getirir
#print(yeniDF)

#yeniDF = df.nsmallest(3,'deger') # en küçük değere sahip ilk 3 tanesi
#print(yeniDF)

#metod 7 loc iloc
#iloc ise satır indekslerine göre
#loc sütün başlıklarına göre
#df.index = ['a','b','c','d','e','f','g']
#yenidDF = df.iloc[3:5, :]
#print(df)

#yenidDF = df.loc['b':'d', :]
#print(yenidDF)

#metod 8 query için ayrı bir örnek mevcuttur Bkz. pandas-query.py