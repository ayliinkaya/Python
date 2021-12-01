import numpy as np
import pandas as pd
df = pd.DataFrame({'isim':['Ahmet','Filiz','Ayşe','Mine','Emine','Can','Canan'],
'kategori':['A','A','C','B','B','C','B'],
'deger':np.random.random(7).round(2),
'deger2':np.random.randint(1,10, size=7)
})

print(df)