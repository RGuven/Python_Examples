#Bubble sort algorithm bir sıralama algoritmasıdır.

def sırala(deger):
    while True:
        dogruluk=False
        for i in range(0,len(deger)-1):
            if deger[i]>deger[i+1]:
                deger[i],deger[i+1]=deger[i+1],deger[i]
                dogruluk=True
        if not dogruluk:
            return print(deger)


sırala([1,5,3,9,45,22,1])
sırala([-1,2,3,5,566,-96])
