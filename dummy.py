'''import pandas as pd

df = pd.DataFrame({'isim':["Ali","Ayşe","Ahmet","Berk","Cem","İdil","Elif"], 'yaş':[17,35,23,15,17,32,18]})

df.index = ['1.kişi','2.kişi','3.kişi','4.kişi','5.kişi','6.kişi','7.kişi']

print(df)'''

import numpy as np
import pandas as pd
df = pd.DataFrame({'isim':['Ahmet','Filiz','Ayşe','Mine','Emine','Can','Canan'],
'kategori':['A','A','C','B','B','C','B'],
'deger':np.random.random(7).round(2),
'deger2':np.random.randint(1,10, size=7)
})
print(df)

# metod 1 matematiksel operatörler ile
# yeniDF = df[(df.deger > 0.5)]
# print(yeniDF)

# yeniDF = df[(df.isim > 'Filiz')]
# print(yeniDF)

# metod 2 & ve - | veya
yeniDF = df[(df.deger < 0.5) | (df.deger2 > 7)]
print(yeniDF)