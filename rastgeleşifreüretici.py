import string
import random

while True:
    sayı = input("Parolanın içerisinde sayı olsun mu? [E/H]: ")
    if(sayı != "E" and sayı != "H"):
        print("Hatalı tuşlama yaptınız.")
        continue
    elif(sayı == "H"):
        print("Ekleme yapılmadı.")
    harf = input("Parolanın içerisinde harf olsun mu? [E/H]: ")
    if (harf != "E" and harf != "H"):
        print("Hatalı tuşlama yaptınız.")
        continue
    elif (harf == "H"):
        print("Ekleme yapılmadı.")
    özel_karakter = input("Parolanın içerisinde özel karakter olsun mu? [E/H]: ")
    if (özel_karakter != "E" and özel_karakter != "H"):
        print("Hatalı tuşlama yaptınız.")
        continue
    elif (özel_karakter == "H"):
        print("Ekleme yapılmadı.")

    min = int(input("Parola minimum kaç karakter olsun?"))
    maks = int(input("Parola maksimum kaç karakter olsun?"))

    if (min >= maks):
        print("Hatalı giriş yaptınız, tekrar deneyiniz.")
    elif (min <= 0):
        print("Parola 0'dan küçük olamaz.")


    break

def üretici(stringLenght = min):
    if(sayı == "E"):
        rastgele = string.digits
    if (harf == "E"):
        rastgele = string.ascii_letters + string.digits
    if (özel_karakter == "E"):
        rastgele = string.punctuation + string.digits + string.ascii_letters

    return''.join(random.choice(rastgele) for i in range(stringLenght))
print("Şifreniz: ",üretici(min))