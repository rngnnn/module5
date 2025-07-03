

num=[2,8,9,48,8,22,-12,2] 

#array [] bu oluyor bazi urunleri yani genel olarak urunleri listelemek icin kullanilir.# array [] this happens to list some products.

print(num) 
# bu sekilde arrayi iki katina cikartmis oluyoruz.# array [] this happens to list some products, i.e. general

doubled_set=set()    
  
for i in range(len(num)):
     doubled_set.add(num[i] * 2)

print(doubled_set) 

# num = [...] → liste tanımı

    #Python’da veri gruplarını saklamak için kullanılır.

    #Köşeli parantez ([]) ile tanımlanır.

    #İçinde tekrar eden değerler olabilir: örnek olarak 2 ve 8 bu listede iki kez geçiyor.
    #    Python’da set, tekrar eden değerleri otomatik olarak siler.

    #set içinde elemanlar benzersizdir.

    #Sıralama garanti edilmez (yani her çalıştırmada sırası farklı olabilir).

