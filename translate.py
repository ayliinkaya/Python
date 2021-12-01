from textblob import TextBlob

english = TextBlob("When we formulate a model, we need to be concerned with the units of the quantities involved.Units are also helpful when we estimate parameters from data.The units of both sides of the above equations must be the same.")

turkce = english.translate(to='tr')
print(turkce)

""" turkce = TextBlob("Python, üst düzey, genel amaçlı bir programlama dilidir.")
english = turkce.translate(to='en')
print(english) """