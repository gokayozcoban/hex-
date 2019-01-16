

# hex()

# hexadecimal (16'lı) 
# BU FONKSİYON HERHANGİ BİR SAYININ 16 (ONALTI)'LI SİSTEMDEKİ KARŞILIĞINI
# STRİNG OLARAK VERİR.

# SORU: 10 SAYISININ HEXADECİMAL KARŞILIĞI NEDİR?

hexadecimal_değeri_nedir = 10
print(hex(hexadecimal_değeri_nedir))
print(hex(hexadecimal_değeri_nedir)[2:])
#'0xa'     DEĞERİN BAŞINDAKİ 0x İFADELERİ SONUCUN HEXADECİMAL SİSTEME AİT 
#'a'       OLDUĞUNU GÖSTERİR. TEK BAŞINA 10'UN KARŞILIĞI a'DIR.

# ÖRNEK PROGRAM:
# from integer to hexadecimal and from hexadecimal to integer
veri = int(input("Sayı girin: "))
if veri == veri:
    print(hex(veri)) # çıktıyı str olarak verir.
veri2 = input("Kodu girin: ")
if veri2 == veri2:
    print(int(veri2,16))# veri2 str'dir.hexadecimal sayı olduğu için 16 yazdım.
#Sayı girin: 1500250
#0x16e45a
#Kodu girin: 0x16e45a
#1500250

# BİÇİMLENDİRME YOLUYLA YAPACAK OLURSAM:
veri = 1980
print("{:x}".format(veri))
#7bc
# NE YAPTIM: "{:x}" İFADESİ hex() İLE AYNI İŞİ YAPAR.
