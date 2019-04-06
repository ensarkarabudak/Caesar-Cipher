sifreli_metin=''
def desifrele(karakter):
    if karakter.isalpha() or karakter.isspace():
        sayi = ord(karakter)
        sayi -= coz
        if karakter.isupper():
            if sayi > ord('Z'):      
                sayi -= 26
            elif sayi < ord('A'):
                sayi += 26
        elif karakter.islower():
            if sayi > ord('z'):      
                sayi -= 26
            elif sayi < ord('a'):    
                sayi += 26
        dosya_yaz(chr(sayi))
    else:
        pass

def sifrele(karakter):
    if karakter.isalpha() or karakter.isspace():
        sayi = ord(karakter)
        sayi += anahtar
        if karakter.isupper():
            if sayi > ord('Z'):      
                sayi -= 26
            elif sayi < ord('A'):
                sayi += 26
        elif karakter.islower():
            if sayi > ord('z'):      
                sayi -= 26
            elif sayi < ord('a'):    
                sayi += 26
        dosya_yaz(chr(sayi))
    else:
        pass

def dosya_yaz(sifreli_karakter):
    with open("sonuc.txt","a+") as f:
        f.writelines(sifreli_karakter)
try:
    print('Lutfen Seçim Yapınız:\n 1 - Şifrele \n 2 - Deşifrele')
    sec=int(input())
    if sec == 1:
        print('Lufen bir anahtar girin(1-26):')
        anahtar=int(input())
        if(anahtar>0 and anahtar<=26):
            with open("metin.txt","r+") as dosya:
                tut=dosya.readlines()
                for symbol in tut:
                    for i in symbol:
                        sifrele(i)
    elif sec == 2:
        print('Anahtar Gir:')
        coz=int(input())
        with open("metin.txt","r+") as dosya:
            tut=dosya.readlines()
            for symbol in tut:
                for i in symbol:
                    desifrele(i)
    else:
        print("Lutfen 1 veya 2 seçeneklerinden birini seçiniz!")
except ValueError:
    print("Lutfen sayı giriniz")
