class Hesap:
    def topla(self,*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def ortalama(self,*args):
        toplam = 0
        for i in args:
            toplam +=i
        ortalama = toplam/len(args)
        return ortalama