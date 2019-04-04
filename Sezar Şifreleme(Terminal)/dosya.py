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
        print(chr(sayi))
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
    with open("sifreli_dosya.txt","a+") as f:
        f.writelines(sifreli_karakter)
try:
    while True:
        print('Lufen bir anahtar girin(1-26):')
        anahtar=int(input())
        if(anahtar>0 and anahtar<=26):
            with open("sifrele.txt","r+") as dosya:
                tut=dosya.readlines()
                for symbol in tut:
                    for i in symbol:
                        sifrele(i) 
            break
     
        else:
            print('LUTFEN 1-29 ARASINDA BIR SAYI GIRIN')

    while True:
        print('Anahtar Gir:')
        coz=int(input())
        with open("sifreli_dosya.txt","r+") as dosya:
            tut=dosya.readlines()
            for symbol in tut:
                for i in symbol:
                    desifrele(i)
        break
except ValueError:
    print("Lutfen sayı giriniz")
