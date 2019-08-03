import random

bs=random.randint(1,99)
tahmin=-1
s=0
print(bs)
while (tahmin != bs):
    tahmin=int(input("Sayı Giriniz: "))
    s=s+1
    
    if (tahmin > bs):
        print("Daha Küçük Sayı Giriniz.")
        
    if (tahmin < bs):
        print("Daha Büyük Sayı Giriniz.")
        
print("Doğru Bildiniz Tahmininiz:",tahmin)
