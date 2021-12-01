class Araba():
    def __init__(self,model,renk): #özellikler burada tanımlanır
        self.model = model
        self.renk = renk
        
    def calis(self): #metod diğer bakış açısıyla fonksiyon tanımı
        print("Vınnnn vınnnn!")
    def gazla(self):
        print("Vuhuuuuuuuuu!")
    def dur(self):
        print("Durdu!")

benimArabam = Araba("Murat124","Beyaz")

print(type(benimArabam))
print(benimArabam)
print(benimArabam.model,benimArabam.renk)

benimArabam.calis()
benimArabam.gazla()
benimArabam.dur()

"""
Self parametresi, sınıfın mevcut örneğine bir referanstır ve sınıfa ait değişkenlere erişmek için kullanılır.
Self olarak adlandırılması gerekmez, istediğiniz gibi adlandırabilirsiniz, ancak sınıftaki herhangi bir işlevin ilk parametresi olmalıdır
"""