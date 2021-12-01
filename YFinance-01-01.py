import yfinance as yf

aselsan = yf.Ticker("ASELS.IS")

hist = aselsan.history(period="30d") 
# get stock info
print(hist)
print(type(hist))
