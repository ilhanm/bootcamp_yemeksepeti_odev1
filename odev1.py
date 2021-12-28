"""[soru1] Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu """

# metin="uzunluğu hesaplacak olan metin"
# print(len(metin))

"""[soru2]Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız."""

# val=input("metin giriniz: ")
# print(f"İlk İki Harfi: {val[:2]} , Son İki Harfi: {val[-2:]}",sep=" | ")

"""[soru3]Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız."""

# degisecekMetin=input("değiştirilecek metin: ")
# eskiharf=input("eski harf: ")
# yeniharf=input("yerine konulacak yeni harf: ")
# degisecekMetin=degisecekMetin.replace(eskiharf,yeniharf)
# print(degisecekMetin)

"""[soru4]Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """

# inputMetin=input("Palindrom kontrolü için metin giriniz: ")
# if(inputMetin.replace(" ","")==inputMetin[::-1].replace(" ","")):
#     print("palindromdur")
# else:
#     print("palindrom değildir.")

#######################################################################################################################
#######################################################################################################################

"""[soru5]Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz. """

# metin=input("Metin giriniz: ")
# print(metin+metin[-2:]*4)

"""[soru6]5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız. """

# mylist=[1,2,3,4,5]
# mylist[1]=100
# print(mylist)

"""[soru7]İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """

# birinciList=[1,2,3,4,5]
# ikinciList=[6,7,8,9,10]
# birinciList.append(ikinciList)
# print(birinciList)
# birinciList=[1,2,3,4,5]
# birinciList.extend(ikinciList)
# print(birinciList)
# birinciList=[1,2,3,4,5]
# birinciList+=ikinciList
# print(birinciList)

"""[soru8]Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """

# mylist=["Armut","Portakal","Ayva"]
# mylist.insert(0,"Elma")
# print(mylist)

"""[soru9]liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. """

# liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
# liste.remove(3)
# print(liste)

"""[soru10] liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,
her iki listeyi ekrana yazdırınız. Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 Çıktısı """
# liste1 = ["1",1,2,"3"]
# liste2=liste1.copy()
# liste2.append(250)
# print(liste1)
# print(liste2)


"""[soru11]
Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız
 dict1={1:10, 2:20} dict2={3:30, 4:40} dict3={5:50,6:60} Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """
# dict1,dict2,dict3={1:10, 2:20} ,{3:30, 4:40}, {5:50,6:60}

# dict1=dict1 | dict2 | dict3 #python 3.9 dict merge operator
# print(dict1)


"""[soru12]sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız Beklenen Çıktı :(6,60) """

# sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print(sozluk.popitem())


"""[soru13]dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30} """

# dict1={1:10, 2:20}
# dict1.update({3:30}) 
# print(dict1)

"""[soru14]liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun b.sözlüğün her alamanının karşılığına değer olarak
 anahtarda bulunan sayısal değerin 10 katını eşitleyin. Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,5:0} b. {1:10,2:20,3:30,4:40,5:50} """

# liste=[1,2,3,4,5]
# a=dict.fromkeys(liste,0)
# mappedlist=list(map(lambda i:i*10,liste))
# b=dict(zip(liste,mappedlist))
# print(a)
# print(b)

"""[soru15]sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz

"""

# sozluk={1:10,2:20,3:30,4:40,5:50}
# sozluk.setdefault(6,60)
# print(sozluk)

"""[soru16]Seven Segment Display https://en.wikipedia.org/wiki/Seven-segment_display

* * * * *
*       *
*       *
* * * * *
*       *
*       *
* * * * *

8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım
## hex,bin,zfill, tek satırda if
"""
# 
#bu kodu sevensegment.py dosyası içine ayrı olarak yazdım..
#

"""[soru17] Bir listeyi bir sözlükte sıralamak için bir Python programı yazın
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """

# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for mykey in num.keys():
#     num[mykey].sort()
# print(num)    

"""[soru18] sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. """
# #https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
# sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
# sozluk2=sozluk.copy()
# for mykey in sozluk2.keys():
    
#     mynewkey=mykey.replace(" ","")    
#     sozluk[mynewkey]=sozluk[mykey]
#     del sozluk[mykey]
    
# print(sozluk)

"""[soru19]
liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz? """

# liste1=[1,2,3]
# liste2=[4,5,6,7,8]
# liste3=liste1+liste2

# print(liste3)

"""[soru20]
liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?
"""

# liste=[1,2,3,4,5,6]
# del liste[0]
# print(liste)


"""[soru21] liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz? """

# liste=["elma" , "armut", "çilek"]
# liste.append(3)
# print(liste)

"""[soru22] Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""
# myarr=[]
# for i in range(10):
#     myarr.append(int(input(f"{i+1}. sayıyı girin: ")))
# myarr.sort()
# print(myarr[-3:])

"""[soru23] Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

# metin="DeNeMestRinG"
# buyukler=[]
# kucukler=[]
# for i in metin:
#     if(i.isupper()):
#         buyukler.append(i)
#     if(i.islower()):
#         kucukler.append(i)
# print(f"buyuk harf listesi: {buyukler} \nkucuk harf listesi{kucukler}")

"""[soru24] kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """  

# sayilar=[]
# cift,tek=0,0
# for i in range(10):
#     sayilar.append(int(input("sayiyi giriniz: ")))
# for sayi in sayilar:
#     if sayi%2==0:
#         cift=cift+1
#     else:
#         tek=tek+1
# print(f"toplam {cift} çift sayı ve {tek} tek sayı girilmiştir.")
    