# parola= input("Lütfen parolanozı girin:")
# print("Teşekkürler!")
# print("Girdiğiniz parola %s" %(parola))
# print("Girdiğiniz parola, %s ne yazık ki doğru değil." %(parola))

# a= int(input())
# print(a*a)

# a= input("Bir sayı girin:")
# print(int(a))

# #-*- coding: utf-8 -*- 



# for i in range(0,10):
#     print("a")

# print(i)



# sayi= int(input("Katını alabilmemiz için bir sayı giriniz: "))
# kat= int(input("%s sayısının almamızı istediğiniz katını yazınız: " %(sayi)))
# sonuc= ("%s sayısının %s\"inci katı %s\"dir. " %(sayi, kat, sayi**kat))
# print(sonuc)




# name= input("İsminizi Giriniz: ")
# surname= input("Soy isminizi Giriniz: ")
# a= "*"
# a=a.center(50,"*")

# print(a)
# kullaniciadi= input("Adınızı giriniz: ")
# kullanicisoyadi= input("Soy adınızı Giriniz: ")

# if name==kullaniciadi:

#     if surname==kullanicisoyadi:
#         print("Programa Hoşgeldiniz!")
#     else: print("Lütfen bilgileri Kontrol Ediniz")
# else: print("Lütfen bilgilerinizi kontrol ediniz.")


# secenek1= "(1) Toplama işlemi"
# secenek2= "(2) Çarpma İşlemi"
# secenek3= "(3) Çıkarma İşlemi"
# secenek4= "(4) Bölme İşlemi"

# print(secenek1)
# print(secenek2)
# print(secenek3)
# print(secenek4)

# islem= int(input("Başlamak İçin Bir İşlem Seçiniz: "))

# a="*"
# a=a.center(50,"*")
# print(a)

# ilksayi= int(input("İlk Sayınızı Seçiniz: "))
# print(a)
# ikincisayi= int(input("İkinci Sayınızı Seçiniz: "))

# print(ilksayi, " ", ikincisayi)
# print(a)

# if islem==1:
#     print(ilksayi+ikincisayi)

# elif islem==2:
#     print(ilksayi*ikincisayi)

# elif islem==3:
#     print(abs(ilksayi-ikincisayi))

# elif islem==4:
#     print(ilksayi/ikincisayi)
# BASİT HESAP MAKİNESİ

# WHILE IF AYIRDI İÇİN BU ÖRNEK ÖNEMLİ 
# soru= input("Python mı Ruby mi?")

# while soru !="Python":
#     print("Yanıtınız Yanlış!")

# ## WHILE ÖĞRENMEMİŞSİN ABİ

# a= 0
# while a<100:
#     a=a+1
#     print(a)

## RANGE()
# x= range(100, 200, 2)
# for n in x:
#     print(n)
    
# for sarki in range(1,15):
#     print (sarki, "mumdur")

# while True:
#     a= input("Lütfen bir parola belirleyin: ")
#     if len(a)<=8:
#         print("Parolanız etkinleştirilmiştir.")
#         break
    
#     else:
#         print("Lütfen yeni bir parola belirleyiniz.")


# soru= input("Python mı Ruby mi?")

# if soru !="Python":
#     print("Yanlış Cevap!")


# FOR İÇİN ÖRNEKLER 
# for sarki in range(1,15):
#     print(sarki ,"mumdur")

# for kelimeler in "linux":
#     print(kelimeler)

# !! len()
# answr= input("Lütfen Parolanızı Giriniz: ")
# if len(answr) >= 8:
#     print("Lütfen en fazla 8 karakterli bir şifre giriniz.")

# else:
#     print("Parolanız Aktive edilmiştir.")


# !! break 

# kullanici_adi= "Berat"
# sifre= "kktc"

# while True:
#     askname=input("Kullanıcı Adı: ")
#     askpswrd=input("Şifre: ")
#     if askname==kullanici_adi and askpswrd==sifre:
#         print("Sisteme Hoşgeldiniz!")
#         break
#     else:
#         print("Bilgilerinizden birisi veya her ikisi yanlış.")
#         print("Lütfen bilgileriniz gözden geçirin.") 



# !! continue

# while True:
#     question=input("What is the greatest food on the world? ")
    
#     if question=="İptal":
#         break
#     if question=="Kebap":
#         continue
#         print("Yanıtınız Yanlıştır!")


# #!! in 
# answr=input("Do you want to get off? ")

# if "Y" in answr or "y" in answr:
#     print("See you soon!")
# else:
#     print("You are in the system still. Thank you for this choose.")



# LİSTELELER!!

#  .append() listenin sonuna 'bir' öge eklememizi sağlar.   (append=eklemek, iliştirmek)

# liste= ["Berat", "Hüseyin", "Ömer"]

# liste.append("Muhammed")
# liste.append("Su")
# print(len(liste))

# .insert()  listenin belirtilen sırasına 'bir' öge eklememizi sağlar.    (insert= yerleştirmek, sokmak)

# liste= ["Berat", "Hüseyin", "Ömer"]
# liste.insert(1, "Yıldız")
# liste.append("Neşeli")

# print(liste)


#extend()  mesela a ve be listelerimiz var. Bu iki listeyi tek çatı altında toplamak istiyorsam: a.extend(b) demeliyim.

# a=["Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]

# b=["Kalem", "Silgi", "Cetvel", "Raptiye"]

# a.extend(b)

# print(a)

# remove()   Listede silmek istediğimde mesela a.remove(b) karşılaştığı ilk b ögesini silecektir.

# a=["Otobüs", "Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]

# a.remove("Otobüs")
# print(a)

# pop()   remove ile aynı işlevli ekstra olarak sildiği ögeyi ekrana yazdırır.

# a=["Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]

# print(a.pop())
## print(a.remove())   bu şekilde yapamayız. Hata verir.

#  insert()  liste elemanlarının kaçıncı sırada bulunduklarını görmek için kullanırız.

# a=["Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]

# print(a.index("Kamyon"))

# .sort()   listeyi alfabetik veya küçükten büyüğe sıralar.

# a=["Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]

# # a= a.sort()     HÜSEYİN ABİYE SOR
# a.sort()
# print(a)

# .reverse() listeyi tersten yazdırır.

# a=["Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]
# a.reverse()
# print(a)

# .count()  bir ögenin liste içinde kaç defa geçtiğini gösterir.

# a=["Otobüs","Otobüs", "Kamyon", "Jet", "Jip", "Bibip"]

# print(a.count("Otobüs"))



# #LİSTE ÖZET
#   NASIL LİSTE OLUŞTURULACAĞI: liste=[]
#   BU LİSTEYE NASIL ÖGE EKLEYECEĞİMİZİ: liste.append(), liste.insert()
#   LİSTEMİZİ NASIL GENİŞLETECEĞİMİZİ: liste.extend
#   EKLEDİĞİMİZ ÖGELERİ NASIL ÇIKARACAĞIMIZI: liste.remove(), liste.pop()
#   LİSTE İÇİNDEKİ ÖGELERİN SIRASINI BULMAYI: liste.index()
#   ÖGELERİ ABC SIRASINA GÖRE YAZMAYI: liste.sort()
#   ÖGELERİN SIRASINI TERSE ÇEVİRMEYİ: liste.reverse()
#   LİSTENİN İÇERİSİNDE BİR ÖGENİN KAÇ DEFA GEÇTİĞİNİ BULMAYI: lise.count()     öğrendik!!!



#   Simples!!
# liste= ["elma", "armut", "şeftali"]

# liste[3:3] = ["domates", "salata"]
# print(liste)

# print(liste[2:])

# liste[3:3]= ["Havuç", "Biber"]
# print(liste)
 
# liste[2:3]= ["nane", "limon"]
# print(liste)
# liste[2]= "kabak", "lahana"
# print(liste)


## BUNU TAMAMLA HOCAM
# while True:
    
#     print("Welcome Buddy. How can I help you? \n (1) Toplama Çıkarma İşlemi\n (2) Çarpma bölme işlemi\n (3) Meyve Sebze Siparişi\n (4) Araba model bilgiledirmesi")

#     answer= input("İşlem türünü seçiniz(numara): ")

#     print(answer, "nolu işlemi seçtiniz")

#     if answer=="1":
#         answer1= input("Toplama işlemi mi Çıkarma İşlemi mi Yapacaksınız(Toplama/Çıkarma)? ")
#         if answer1=="Toplama":
#             number1=  int(input("İlk değeri giriniz: "))
#             number2= int(input("ikinci değeri giriniz: "))
#             print(number1+number2)
#         else:
            
#             number1=  int(input("İlk değeri giriniz: "))
#             number2= int(input("ikinci değeri giriniz: "))
#             print("Cevap: ", number1-number2)


# SIMPLE1    [BONUS TIMEE]
# serviceyear=int(input("How long did you work with us? " ))
# salary= int(input("How much do you get salary? " ))
# if serviceyear>=5:
#     print("Congurulations we have a good new for you.\n We wanted to reward you with %5 bonus. Your bonus money is {} dollar.".format((salary*5/100)))

# # for i in range(4):
# side1=  int(input("You have a rectangle. I want to you tell me what it's lenght and breadth values? \n 1- "))
# side2=  int(input(" 2- "))
# side3=  int(input(" 3- "))
# side4=  int(input(" 4- "))

# if side1==side2 and side2==side3 and side3==side4:
#     print("You have a square!")
# else:
#     print("Your rectangle isn't a square!")

# SIMPLE2    [BÜYÜK OLAN HAYATTA KALIR]
# while True:
#     print("Hello dude. I want to give me 2 number from you can you give me 2 number please?")
#     frstnmbr=input("First number: ")
#     if frstnmbr=="End" or frstnmbr=="end":    
        
#         break
#     scndnmbr=input("Second number: ")
#     # if frstnmbr=="End" or "end" and scndnmbr=="End" or "end":
    
     
#     if int(frstnmbr)>=int(scndnmbr):
#         print(frstnmbr)
#     else:
#         print(scndnmbr)


## SIMPLE 3 WE HAVE TWO ALTERNATIVES  [İNDİRİM VAR GEL AĞABEY GEEL]

# quantity= input("How much quantity did you buy? ")
# cost= int(quantity)*100
# if int(cost)>=1000:
#     discount= int(cost)*9/10
#     print("You have quantity from us. Your  cost is {} dollar. Have a good day!".format(discount))
# else:
#     print("Your cost is {}".format(cost))

# quantity= input("quantity: ")
# if int(quantity)*100>=1000:
#     print(int(quantity)*90)
# else:
#     print(int(quantity)*100)

## SIMPLE 4  [SINAVDAN HANGİ DERECEYİ ALDIĞINI GÖSTERMECEE]
# print("Exams announced")
# grade=int(input ("What is your grade if you want to know that you should give me your mark. "))
# if grade<=25:
#     print("Your grade: F")
# elif grade>=25 and grade<=45:
#     print("Your grade: E")
# elif grade>=45 and grade<=60:
#     print("Your grade: D")
# elif grade>=60 and grade<=70:
#     print("Your grade: C")
# elif grade>=70 and grade<=80:
#     print("Your grade: B")
# else:
#     print("Your grade: A!! Congrulations")

# ## SIMPLE 5  [EN KÜÇÜK VE EN BÜYÜK YAŞI YAZDIRMACAAA]

# print("Yaşlarınızı teker teker giriniz:")
# firstperson=int(input("1- "))
# secondperson=int(input("2- "))
# thirdperson=int(input("3- "))

# if firstperson>secondperson and firstperson>thirdperson:
#     print(firstperson)
# elif secondperson>firstperson and secondperson>thirdperson:
#     print(secondperson)
# elif thirdperson>firstperson and thirdperson>secondperson:
#     print(thirdperson)
# if firstperson<secondperson and firstperson<thirdperson:
#     print(firstperson)
# elif secondperson<firstperson and secondperson<thirdperson:
#     print(secondperson)
# elif thirdperson<firstperson and thirdperson<secondperson:
#     print(thirdperson)
# else:
#     print("All are equal. Interestingg")


# # SIMPLE 6    [MUTLAK DEĞER YAPMACAA]
# number= int(input("Write a number: "))
# if number<0:
#     number= number*-1
#     print(number)
# else:
#     print(number)

# # SIMPLE 7 [GİRER Mİ GİRMEZ Mİ]

# print("We should know some informations about you for taking you to exam.")
# derssayisi= int(input("Number of classes held: "))
# katilim= int(input("Number of classes attended: "))
# print(derssayisi,"-", katilim)
# if katilim/derssayisi>=3/4:
#     print("You can go to the exam.")
# else:
#     print("We can't take you to this exam. sorry about that. muhahaha!")

## WHILE SIMLPES

## SIMPLE 1 (1'DEN 10'A)
# i=0
# while i<=10:
#     print(i)
#     i=i+1

# i=1
# while i<=4:
#     print("*"*i)
#     i=i+1

# # i=1
# # j=3
# # while i>=1:
# #     print(" "*j+"*"*i+" "*j)
# #     i=i+2
# #     j=j-1
# #     if i>5:
# #         break
# # i=3
# # j=2
# # while i>=1:
# #     print(" "*j+"*"*i+" "*j)
# #     i=i-2
# #     j=j+1
# #     if i<1:
# #         break

# # i=3
# # j=1

# # while i>=0:
# #     print(" "*j+"10"*i+"1"+" "*j)
# #     i=i-1
# #     j=j+1
# #     if i<0:
# #         break
# # i=1
# # while i<=10:
# #     print(24*i,"-", 50*i,"-", 29*i )
# #     i=i+1
# while True:
#     print("Allah")


# a=int(input("Number: "))
# i=1
# if a==0:
#     print(1)
# else:
#     while a>=1:
#         i=i*a
#         a=a-1
#     print(i)

# print("Write two numbers for GCD ")
# x=int(input("1. "))
# y=int(input("2. "))
# while y!=0:
#     x,y = y,x % y
#     print(x)

print("Can you write numbers? ")
toplam = 0
carpim = 1
girdiSayisi = 0

while True:
    a = input("-(enter q for quit)")
    if a == "q" :
        break
    else:
        a = int(a)
        toplam += a
        carpim *= a
        girdiSayisi = girdiSayisi + 1
if (girdiSayisi > 0):
    ortalama = toplam / girdiSayisi
    print("ortalama: ", ortalama)
    print("carpim: ", carpim)


# small = x 
# big = y
# if(small > big):
#     small = y
#     big = x


# i = small
# while i > 0:
#     if(small % i == 0 and big % i == 0):
#         print("GCD: ",i)
#         break
#     i = i-1