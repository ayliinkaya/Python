import yfinance as yf #pandas dataframe içinde mevcuttur

bist = yf.Ticker("XU100.IS")
aselsan = yf.Ticker("ASELS.IS")

histBIST = bist.history(period="30d")
histAselsan = aselsan.history(period="30d")

fiyatBist = histBIST["Close"]
fiyatAselsan = histAselsan["Close"]

pearsonKorelasyon = fiyatBist.corr(fiyatAselsan, method="pearson")
spearmanKorelasyon = fiyatBist.corr(fiyatAselsan, method="spearman")
kendallKorelasyon = fiyatBist.corr(fiyatAselsan, method="kendall")

print("Pearson : ", round(pearsonKorelasyon,2))
print("Spearman : ", round(spearmanKorelasyon,2))
print("Kendall : ", round(kendallKorelasyon,2))