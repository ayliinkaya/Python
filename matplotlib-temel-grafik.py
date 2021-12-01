import matplotlib.pyplot as plt 

sehirler = ('İstanbul','Ankara','İzmir','Balıkesir','Antalya','Trabzon') #bilgiler değişmeyeceği için Tuple (demet)
gelirler = [3500,4500,2700,2200,3000,2250] #bilgiler değişebileceği için List (liste)

plt.figure("İller ve Gelir")
plt.bar(sehirler,gelirler,align='center',alpha=0.5)
plt.xticks(sehirler)
plt.ylabel('Gelir')
plt.xlabel('İller')
plt.title('İllere Göre Gelir Ortalaması')
plt.show()