sifreli_metin=''
def getMessage():
    return input()

def sifrele(karakter):
    if karakter.isalpha():
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
        print('KARAKTER HATASI')

def dosya_yaz(sifreli_karakter):
    with open("sifreli_dosya.txt","a") as f:
        f.writelines(sifreli_karakter)
       
try:
    while True:
        print('Lufen bir anahtar girin(1-26):')
        anahtar=int(getMessage())
        if(anahtar>0 and anahtar<=26):
            with open("sifrele.txt","r+") as dosya:
                tut=dosya.readlines()
                for symbol in tut:
                    for i in range(0,len(symbol)):
                        sifrele(symbol[i])       
            break
        else:
            print('LUTFEN 1-29 ARASINDA BIR SAYI GIRIN')
except ValueError:
    print("Lutfen sayı giriniz")

