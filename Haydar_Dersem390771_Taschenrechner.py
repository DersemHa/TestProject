
import math

while True:
 x = int(input("Addieren(1), Subtrahieren(2), Multiplizieren(3), Dividieren(4), Pythagoras(570), weitere Funktionen(0)"))
 if (x == 0):
     y = int(input("Summe(5), Maximum(6), Minimum(7), Mittelwert(8), Umfang(9)"))
     if(9>y>=5):
         Liste = []
         n = int(input("Geben Sie die Anzahl an Zahlen ein!: "))
         for i in range(0, n):
             ele = int(input())

             Liste.append(ele)
             if (y == 5):
                 if (len(Liste) == n):
                  print(sum(Liste))

             if(y==6)    :
                 if (len(Liste) == n):
                  print(max(Liste))
             if(y==7):
                 if (len(Liste) == n):
                  print(min(Liste))
             if(y==8):
                 if (len(Liste) == n):
                     def mean(mw):
                         return sum(mw) / len(mw)

                     print(mean(Liste))
                     break
     if(y==9):
        r = int(input("Geben Sie den Radius ein! r="))
        print(2*math.pi*r)
     break
 if(x<5 or x>9):
  a = int(input("1.Zahl="))
  b = int(input("2.Zahl="))
  if (x==1):
    print(a + b)
  if(x==2):
    print(a - b)
  if(x==3):
    print(a * b)
  if(x==4):
    print(a / b)
  if(x==570):
    print(math.sqrt(a**2+b**2))




