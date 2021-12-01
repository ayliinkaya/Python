class Araba():
    def __init__(self,model,renk):
        self.model = model
        self.renk = renk

benimArabam1 = Araba("Anadol","Beyaz")
benimArabam2 = Araba("Murat","Mavi")

print(type(benimArabam1),type(benimArabam2))
print(benimArabam1.model,benimArabam1.renk)
print(benimArabam2.model,benimArabam2.renk)