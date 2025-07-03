#!/usr/bin/env python3


# Python'da sys.argv ve len() fonksiyonu genellikle komut satırından veri alma ve veri sayısını ölçme gibi işlemlerde kullanılır. 
# len() veri sayisini olcer lenghte gibi.
# sys.argv "argument vector" ise komut satirindan veri alir.Bu özellik sys modülü içinde bulunur, önce içe aktarılmalıdır:Yani argv=argument vector demektir.Sys ise bir modüldür ve bu modülün içinde argv bulunur.


import sys
param_count = len(sys.argv) - 1  # Komut satırından gelen argüman sayısını alır, -1 çünkü ilk argüman betiğin kendisidir.

print(f"Number of parameters: {param_count}.")  # Komut satırından gelen argüman sayısını yazdırır.")