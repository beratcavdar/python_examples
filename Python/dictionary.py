# isim soyisim yaş öğrenci no telefon no 

ogrenciler={}
number= input("Öğrenci Numarası: ")
name= input("İsim Soy İsim: ")
age= input("Yaşınız: ")
phone= input("Telefon No: ")
# ogrenciler[number]= {
#     "İsim: ":name,
#     "Yaş: ":age,
#     "Telefon Numarası:":phone
# }
# print(ogrenciler)

ogrenciler.update({
    number:{
        "ad": name,
        "yaş": age,
        "telefon no":phone
    }
})
print(ogrenciler)