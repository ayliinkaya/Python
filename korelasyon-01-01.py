import pandas as pd

df = pd.read_csv('sporverisi.csv')
korelasyon = df.corr()

print(korelasyon)

print(type(korelasyon))

print(korelasyon['Sure']['Nabiz'])

# 1.00000 mükemmel korelasyon
# 0.6 dan düşük değer kötü korelasyon
# 0.6 - 1 arası değer iyi korelasyon
# - değerler ise zıt korelasyondur.