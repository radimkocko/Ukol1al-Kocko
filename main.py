import random

array = [1 , 5, 7, 12, 24, 37, 49, 80, 100] #Pole s cisly od 1-100
prvni = min(array) #vypise prvni hodnotu pole
prostredni =  max(array) / 2
posledni = max(array) #Vypise posledni hodnotu pole
print(prvni)
print(prostredni)
print(posledni)
array[5] = 34 #zameni 5. indexovou hodnotu za cislo 34.
print(array)
print(array[7])
print(len(array)) #Vypise delku pole
print(min(array))
print(max(array))
arrayb = [2, 4, 6, 8, 10, 12] #Druhe pole
vypocet_poli = sum(array) + sum(arrayb) #Secte hodnoty obou poli.
print(vypocet_poli)
vypocet = arrayb[1] + arrayb[5] #Secte pouze 2 vybrané hodnoty z pole
print(vypocet)
random.shuffle(arrayb) #Random zamicha druhe pole
print(arrayb)