from flask import Flask, render_template, request
import requests
import json

def sifreleulan(karakter,anahtar):
    if karakter.isalpha() or karakter.isspace():
        message=''
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
        message+=chr(sayi)
    else:
        pass
    return message

def cozlan(karakter,anahtar):
    message=''
    if karakter.isalpha() or karakter.isspace():
        sayi = ord(karakter)
        sayi -= anahtar
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
        message+=chr(sayi)
    else:
        pass
    return message

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/sifrele/", methods=['GET', 'POST'])
def sifrele():
        sifreli_metin=''
        if request.method == 'POST':
            message = request.form['message']
            anahtar = request.form['anahtar']
            sifreli_metin=''
            for i in message:
                    sifreli_metin += sifreleulan(i,int(anahtar))
        return render_template('sifrele.html',  sifreli_metin=sifreli_metin)

@app.route("/desifrele", methods=['GET', 'POST'])
def desifrele():
        cozulmus_metin=''
        if request.method == 'POST':
            sifreli_metin = request.form['message']
            anahtar = request.form['anahtar']
            for i in sifreli_metin:
                    cozulmus_metin += cozlan(i,int(anahtar))
        return render_template('desifre.html',  cozulmus_metin=cozulmus_metin)

if __name__ == "__main__":
    app.run()

"""
ENSAR KARABUDAK - github.com/ensarkarabudak   

"""