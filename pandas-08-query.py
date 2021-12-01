#pandas modülü dahil edilir
import pandas as pd

#çevrimiçi bir kaynaktan CSV formatondaki bir veri çekilir ve data değişkeni içinde metin olarak saklanır
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv')

# aktarılan veri bu kod ile test edilebilir. print (pd.DataFrame.to_string(data))

#aktarılan metin Pandas DataFrame nesnesine dönüştürülüyor.
df = pd.DataFrame(data)

#query metodu ile sadece seçilen sütunlardan sadece belirtilen özelliklere sahip bilgilere ait satırlar çekilir ve sonuc değişkeninde yeni bir dataframe olarak saklanır
sonuc = df.query('color == "yellow" and payment == "cash" and pickup_borough == "Manhattan"')
#print(sonuc.to_string())

#bu kod ile sonuc nesnesinin türü öğrenilebilir. print(type(sonuc))

#filtrelenmiş sonuc adlı DataFrame içinde 'pickup'(yolcunun alındığı tarih), 'passengers' (yolcu sayısı), 'distance' (mesafe) bilgileri öğreniliyor.
#print(sonuc["pickup"],sonuc["passengers"],sonuc["distance"])

#alternatif yazdırma şekli
sayac = 0
while sayac<len(sonuc):
    print("Biniş Tarihi : "+ sonuc["pickup"].iloc[sayac]," | Yolcu Sayısı : "+ str(sonuc["passengers"].iloc[sayac])," | Mesafe km : "+ str(sonuc["distance"].iloc[sayac]))
    sayac +=1
