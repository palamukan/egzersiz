print(""""
İŞLEMLER;
********************************************
1-) TOPLAMA
2-) ÇIKARMA
3-) ÇARPMA
4-) BÖLME
********************************************
""")


x = int(input("İlk sayıyı giriniz: "))
y = int(input("İkinci sayıyı giriniz: "))

yapılacak_işlem = input("Yapılacak işlem nedir ? ")

def toplama():
    print("{} ile {}'nin toplamı {}'dir.".format(x,y,x+y))
def çıkarma():
    print("{} ile {}'nin farkı {}'dir.".format(x,y,x-y))
def çarpma():
    print("{} ile {}'nin çarpımı {}'dir.".format(x,y,x*y))
def bölme():
    print("{}'in {}'e bölümü {}'dir.".format(x,y,x/y))



if (yapılacak_işlem == "1"):
    toplama()
elif (yapılacak_işlem == "2"):
    çıkarma()
elif (yapılacak_işlem == "3"):
    çarpma()
elif (yapılacak_işlem == "4"):
    bölme()







