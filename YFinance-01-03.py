import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bist = yf.Ticker("XU100.IS")
aselsan = yf.Ticker("ASELS.IS")
thy = yf.Ticker("THYAO.IS")
isbank = yf.Ticker("ISCTR.IS")

histBIST = bist.history(period="30d")
histAselsan = aselsan.history(period="30d")
histTHY = thy.history(period="30d")
histIsbank = isbank.history(period="30d")

fiyatlar = pd.DataFrame({'BIST' : histBIST["Close"], 'Aselsan' : histAselsan["Close"], 'THY' : histTHY["Close"], 'IsBankasi' : histIsbank["Close"]})
#print (fiyatlar)

korelasyon = fiyatlar.corr()

#print(korelasyon)
sns.heatmap(korelasyon, annot = True)

plt.show()