





website = "https://www.Berahcavdar.com"
course = "Baştan sona kendime öğretir gibi 40 saat python dersi!.."

# 1- 'Hello World' karakter dizisinin baş ve sondaki boşluk karakterini silin.

result='       Hello World '.strip()
result='       Hello World'.rstrip()
result='       Hello World '.lstrip()
result= website.lstrip("htps:/")

# 2- 'www.Beratcavdar.com' içerisindeki Beratcavdar ifadesi haricindekileri silin.
result=website.strip("htps:/.comw")
# 3- 'course' içerisindeki tüm karakterleri küçük harf yapın.
result=course.title()

# 4-'website' içinde kaç tane a karakteri vardır?
result=website.count("a",0,20)
result=len(website)
result=website.count('B',0,20)
# 5-'website'www ile başlayıp com ile bitiyor mu?
result= website.startswith("www")
result=website.endswith(".com")
# 6-'website' içerisinde com ifadesi var mı ?
result=website.rfind("www")

# 7-'course' içindeki tüm karakterler alfabetik mi?
result="12346".isdigit()

# 8-'Contents' ifadesini 50 satıra yerleştirip sağ ve soluna * ekleyiniz.
result="contents".center(50,"*")
result="contents".rjust(50,"*")
result="contents".ljust(50,"*")

# 9-'course' ifadesindeki tüm ' ' ifadesini '-' ile değiştirin.

result=course.replace(" ","-")
# 10-'Hello World' ifadesindeki World yerine Dear koyun.

result="Hello World".replace("World","Dear")

# 11-'course' karakter dizisini boşluk karakterlerinden ayırın.

result=course.split()
result=result[2]

print(result)