# Pythonda matematiksel semboller Toplama(+), Çıkarma(-), Çarpma(*), Bölme(/) şeklinedir.
# Öncelikle biz iki farklı değişken atayıp bu değişkenlere dışarıdan değer atamak için "input" komutunu kullanıyoruz.
# Bundan sonra bu atadığımız iki değişkeni içinde tutup aralarında işlem yapması için bir tane "sonuc" isimli bir değişken oluşturuyoruz.
# Son olarak da print komutu ile sonuc değişkenini mesaj olarak veriyoruz.F5 tuşu ile kodu çalıştırabilirsiniz. 


#Toplama İşlemi.
top1 = int(input("1.sayıyı giriniz :")) # Birinci sayıyı kullanıcıdan input komutu ile alıyoruz.
top2 = int(input("2.sayıyı giriniz :")) # İkinci sayıyı kullanıcıdan input komutu ile alıyoruz.
topSonuc = top1 + top2 # "topSonuc" diye ayrı bir değişken atıp birinci ve ikinci sayıyı toplatıyoruz. 
print(topSonuc) # En Sonda print komutu ile topSonuc değişkenini mesaj verdiriyoruz.

#Ekran çıktısı
# 1.sayıyı giriniz : 5
# 2.sayıyı giriniz : 8
# 13

#Çıkarma İşlemi.
cık1 = int(input("1.sayıyı giriniz :"))
cık2 = int(input("2.sayıyı giriniz :"))
cıkSonuc = cık1 - cık2 
print(cıkSonuc)


#Çarpma İşlemi.
sayi1=int(input("sayı giriniz:"))
sayi2=int(input("bir sayı daha giriniz:"))
sonuc=sayi1*sayi2
print(sonuc)


#Bölme İşlemi.
bol1 = int(input("1.sayıyı giriniz :"))
bol2 = int(input("2.sayıyı giriniz :"))
bolSonuc = bol1 / bol2 
print(bolSonuc)