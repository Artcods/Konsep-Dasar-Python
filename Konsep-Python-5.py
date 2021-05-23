# Konsep Python -5 

 

print("Operasi Komparasi") 
# Setiap hasil dari operasi komperasi (membandingankan suatu variabel) adalah boolean 
# Contoh : 
# >,<,>=,<=,==,!=,is,is not 

 
a = 4 # a --> variabel

b = 2 # b --> variabel

 

print("\n=====>Lebih Besar<=====") 
# Lebih Besar dari > 
 

hasil = a > 3 

print(a,'>',3,'=',hasil) # hasilnya bener karna 4 lebih dari 3 (True) 

 

hasil = b > 3 

print(b,'>',3,'=',hasil) # hasilnya salah karna 2 kurang dari 3 (False) 

 

hasil = b > 2 

print(b,'>',2,'=',hasil) # karna kalau lebih besar, harus lebih besar dari nilainya 

 

print("\n=====>Kurang dari<=====") 
# Kurang dari < 
 

hasil = a < 5 

print(a,'<',5,'=',hasil) # Hasilnya bener karna 4 kurang dari 5 (True) 


hasil = b < 1 

print(b,'<',1,'=',hasil) # Hasilnya salah karna 2 lebih dari 1 (False) 


hasil = b < 2 

print(b,'<',2,'=',hasil) # karna kalau kurang dari, harus kurang dari nilainya 

 

print("\n=====>Lebih Besar darisama dengan<=====") 
# Lebih Besar darisama dengan (>=) 

 
hasil = a > 3 

print(a,'>=',3,'=',hasil) # Hasilnya Benar karna 4 Lebih besar dari samadengan 3 
 

hasil = b >= 3 

print(b,'>=',3,hasil) # Hasilnya salah karna 2 kurang dari samadengan 3 


hasil = b >= 2 

print(b,'=',2,hasil) # karna 2 sama dengan 2, itu lebih besar untuk samadengan 
 
  

print("\n=====>Kurang darisama dengan<=====") 
# Kurang dari samadengan (<=) 
 

hasil = a <= 5 

print(a,'<',5,hasil) # hasilnya benar karna 4 kurang dari samadengan 5 


hasil = b <= 1 

print(b,'<=',1,hasil) # hasilnya salah karna 2 kurang dari samadengan 1 


hasil = b <= 2 

print(b,'=',1,hasil) # karna 2 sama dengan 2, itu nilainya jadi True untuk lebih dari samadengan 

 

print("\n=====>Samadengan dari<=====") 
# Samadengan dari (==) 
 

hasil = a == 4 

print(a,'==',4,hasil) # hasilnya benar karna sama-sama 4 


hasil = b == 3 

print(b,'==',3,hasil) # hasilnya salah karna tidak sama-sama 2 

 

print("\n=====>Tidak Samadengan dari<=====") 
# Tidak samadengan dari (!=) 


hasil = a != 3 

print(a,'!=',3,hasil) # hasilnya benar karna 4 tidak samadengan 3 
 

hasil = b != 2 

print(b,'!=',2,hasil) # hasilnya salah karna sama-sama 2 
 
 

print("\n========Object Identity (is)========") 
# 'is' Sebagai Komparasi Object Identity (is) 
# ini adalah assignment 
 

x = 5 

y = 5 
 

print("nilai x = ",x,',id = ',hex(id(x))) 

print("nilai y = ",y,',id = ',hex(id(y))) 
# Tipe data yang sama akan di masukan ke memori yg sama, jadinya lebih efisien 

 
hasil = x is y 

print('x is y',hasil) # dan hasilnya akan true 
# Kalau diganti dengan literal/angka akan menjadi syntaxwarning 



x = 5 

y = 6 

print("\n") # Jarak

print("nilai x = ",x,',id = ',hex(id(x))) 

print("nilai y = ",y,',id = ',hex(id(y))) 

 
hasil = x is y 

print('x is y',hasil) # dan hasilnya akan false 

 

print("\n========Object Identity (is not)========") 
# 'is not' Sebagai Komparasi Object Identity (is not) 
# ini adalah assignment 


x = 5 

y = 5 


print("nilai x = ",x,',id = ',hex(id(x))) 

print("nilai y = ",y,',id = ',hex(id(y))) 
# Tipe data yang sama akan di masukan ke memori yg sama, jadinya lebih efisien 


hasil = x is not y # is not

print('x is not y',hasil) # dan hasilnya akan false 
# Kalau diganti dengan literal/angka akan menjadi syntaxwarning  
  
  

x = 5 

y = 6 

print("\n") # jarak

print("nilai x = ",x,',id = ',hex(id(x))) 

print("nilai y = ",y,',id = ',hex(id(y))) 


hasil = x is not y 

print('x is not y', hasil) # dan hasilnya akan true 
