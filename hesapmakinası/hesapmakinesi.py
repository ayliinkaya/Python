def topla(*args):
    #args burada bir liste olarak dahil edilecektir.
    toplam = 0
    for i in args:
        toplam += i
    return toplam

def cikar(*args):
    fark = 0
    for i in args:
        fark -= i
    return fark

def bolme(x,y):
    bolum = x/y
    return bolum

def carpma(*args):
    carpim = 1
    for i in args:
        carpim = carpim * i
    return carpim