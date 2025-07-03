

num=[2,8,9,48,8,22,-12,2] 

#array [] bu oluyor bazi urunleri yani genel olarak urunleri listelemek icin kullanilir.# array [] this happens to list some products.

print(num) 
# bu sekilde arrayi iki katina cikartmis oluyoruz.# array [] this happens to list some products, i.e. general

doubled_set=set()    
  
for i in range(len(num)):
     doubled_set.add(num[i] * 2)

print(doubled_set) 

