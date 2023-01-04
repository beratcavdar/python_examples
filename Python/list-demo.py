from unittest import result


names=["Hüseyin","Berat","Ömer","Ertuğrul"]
years=[2002,2004,2004,2004]

names.append("Birol")
names.insert(0,"Ayşegül")
del names[4]
names.count("Berat")
names.reverse()
names.sort()
years.sort()
str="Chavrolet,Dacia"
result=min(years)

result=years.count(2004)

result=years.clear()


markalar=[]
marka= input("İstediğiniz araba markasını giriniz. ")
markalar.append(marka)

marka=input("İstediğiniz araba markasını giriniz. ")
markalar.append(marka)

marka=input("İstediğiniz araba markasını giriniz. ")
markalar.append(marka)

print(markalar)