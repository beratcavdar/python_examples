website = "https://www.Beratcavdar.com"
course = "Baştan sona kendime öğretir gibi 40 saat python dersi!.."
# 'course' karakter dizisi içerisinde kaç tane karakter bulunur?

print(len(course))

# 'website' içinden www karakterini alın

www = website[8:11]
print(www)

# 'website' içerisinden com karakterini alın
length=len(website)
com = website[length-3:length]
print(com)
# course içinden ilk ve son 15 haneyi alın
lenght=len(course)
print(course[0:15]+" "+course[lenght-15:lenght])
# course ifadesini tersten yazdırmak
print(course[::-1])

name, surname, age, job ="Remzi", "Çavdar", 42, "Düşünmek"
# Benim adım Remzi Çavdar, 42 yaşındayım ve mesleğim Düşünmek   ifadesini yazdırın

print(f"Benim adım {name} {surname}, {age} yaşındayım ve mesleğim {job}.")
print("Benim adım {} {}, {} yaşındayım ve mesleğim {}.".format(name, surname, age, job))
print("Benim adım "+name+" "+surname+","+" "+str(age)+" yaşındayım ve mesleğim "+job+".")

# Hello world ifadesindeki w yerine W ifadesini getirin

s="Hello world"
s= s[:6]+"W"+s[7:]
print(s)
#abc ifadesini üç defa yazdıralım
a="abc " * 3
print(a)
