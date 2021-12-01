import matplotlib.pyplot as plt 

plt.figure("Harcamalar")
harcamalar = ('Ticari','Kamu','Yüksek Öğretim')
miktarlar = [50, 39.7, 10.3]
renkler = ('yellow','lightblue','green')
plt.pie(miktarlar,labels=harcamalar,colors=renkler,autopct='%.1f') #autopct kaç tane ondalık değer gösterileceği
plt.title('Sektörlere Göre Ar-Ge Harcamaları')
plt.show()