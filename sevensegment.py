import math

sutun=5 #    
satir=7 #
sevensegment=[] #2d liste sayının gösterimi için
oneline = [" "]*sutun #bir satir

#2d boş liste oluşturrma
for i in range(satir):
    sevensegment.append(oneline.copy())

def printsevensegment(): #seçim sonrası kullanılacak print fonksiyonu
    for i in range(satir):
        for j in range(sutun):
            print(sevensegment[i][j],end=" ")
            if(j==sutun-1):
                print("\n")

def fillA():
    for i in range(satir):
        for j in range(sutun):
            sevensegment[i][j]="*"
        break

def fillB():
    for i in range(math.ceil(satir/2)):
        for j in range(sutun):
            if j==sutun-1:
                sevensegment[i][j]="*"

def fillC():
    for i in range(math.floor(satir/2),satir):
        for j in range(sutun):
            if j==sutun-1:
                sevensegment[i][j]="*"

def fillD():
    for i in range(satir-1,satir):
        for j in range(sutun):
            sevensegment[i][j]="*"
        
def fillE():
    for i in range(math.floor(satir/2),satir):
        for j in range(sutun):
            if j==0:
                sevensegment[i][j]="*"
    
def fillF():
    for i in range(math.ceil(satir/2)):
        for j in range(sutun):
            if j==0:
                sevensegment[i][j]="*"

def fillG():
    for i in range(math.floor(satir/2),math.floor(satir/2)+1):
        for j in range(sutun):
            sevensegment[i][j]="*"

digitMap = {0: "11111100",1: "01100000",2: "11011010",3: "11110010",4: "01100110",5: "10110110",
        6: "10111110",7: "11100000",8: "11111110",9: "11110110"}

funcList = [fillA, fillB, fillC, fillD, fillE, fillF, fillG] #thanks to baran =)

inputvalue=int(input("0-9 arası sayı giriniz: "))

if(0<=inputvalue<=9):
    for index,value in enumerate(digitMap[inputvalue]):
        if int(value)==1: funcList[index]()
    printsevensegment()
else:
    print("input 0-9 araliginda degil")    


