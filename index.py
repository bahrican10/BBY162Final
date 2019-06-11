fp = open('C:\Users\bahri\Desktop.txt') 
lines = fp.read().split("\n") 

print("Eger listeyi gormek istiyorsan 1'i, kitap eklemk istiyorsan 2'yi , kitabi isim ile armak istiyorsan 3'u sec,kitabi yazar ismi ile armak istiyorsan 4'u sec,kitabi basim tarihi ile armak istiyorsan 5'u sec ")
a=input("Enter a number")
print(a)
def KitapEkleme():
    kitapadi=input("Kitap Adi Giriniz")
    print(kitapadi)
    lines.append(kitapadi)
    print(lines)
    yazaradi=input("Yazar Adi Giriniz")
    lines.append(yazaradi)
    print(yazaradi)
    basimtarihi=input("Basim Tarihi Giriniz")
    lines.append(basimtarihi)

def isimarama():
    isim = input("Kitap ismini giriniz")
    for i in range(0,len(lines),3):

        if isim==lines[i]:
            print("Kitap Adi",lines[i])
            print("Yazar Adi",lines[i+1])
            print("Basim Yili", lines[i + 2])

def yazararama():
    for i in range(1,len(lines),3):
        isim=input("Yazar ismini giriniz")
        if isim==lines[i]:
            print("Kitap Adi",lines[i-1])
            print("Yazar Adi",lines[i])
            print("Basim Yili", lines[i+1])
def basintarihi():
    for i in range(2,len(lines),3):
        isim=input("Yazar ismini giriniz")
        if isim==lines[i]:
            print("Kitap Adi",lines[i-2])
            print("Yazar Adi",lines[i-1])
            print("Basim Yili", lines[i])
if a==1:
    for i in range (0,len(lines)):
         print(lines[i])
         i=+i

if a==2 :
    print (KitapEkleme())

if a==3 :
    print(isimarama())
if a==4:
    print (yazararama())
if a==5:
    print(basintarihi())







fp.close()
