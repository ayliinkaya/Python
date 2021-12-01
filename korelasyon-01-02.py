import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sporverisi.csv')
#DataFrame içerisindeki her sütundaki verilerin birbiriyle korelasyon değerleri hesaplanıyor.
korelasyon = df.corr()

#3 tip korelasyon hesaplama metodu popülerdir.
# Pearson, Spearman, Kendall Tau - Varsayılan ayar Pearsondır

# 1.00000 mükemmel korelasyon
# 0.6 dan düşük değer kötü korelasyon
# 0.6 - 1 arası değer iyi korelasyon
# - değerler ise zıt korelasyondur.

#Korelasyon matriksi ısıl haritası olarak yazdırılıyor.
# annot = True ile kutucukların içerisinde korelasyon derecesi de yazdırılıyor.
sns.heatmap(korelasyon, annot = True)

#Matplotlib Plotly ile grafik ekrana getiriliyor.
plt.show()