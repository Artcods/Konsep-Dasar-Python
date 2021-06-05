
print(10*"="+"Operasi Assignment"+10*"=") 
# Operasi Assignment adalah operasi yg dilakukan dengan penyingkatan 

a = 5 # Variabel

print("Nilai a =",a) # Ini adalah Assignment 


print("\n=====>Belum Disingkat<=====") 
 
a = a + 5 # Belum disingkat 

print("Nilai a =",a)   
 
  
---><---
 
  
print("\nDan Disingkat Menjadi :") 
# Disingkat

a += 1 # Disingkat penjumlahan 

print("Nilai a =",a)  


---><---

  
print("\nDan Disingkat Menjadi :") 
 
a -= 2 # Disingkat pengurangan 

print("Nilai a =",a) 


---><---


print("\nDan Disingkat Menjadi :")  

a *= 5 # Disingkat perkalian 

print("Nilai a =",a) 


---><---


print("\nDan Disingkat Menjadi :") 

a /= 2 # Disingkat perkalian 

print("Nilai a =",a) 




print("\n=====>Membuat contoh baru<=====") 
# Disingkat dengan Modulus, Floor Devision, Exponen 

b = 10 

print("\nNilai b =",b) # Belum Disingkat  


---><---


print("\nDan Disingkat Menjadi :") 
# Disingkat

b %= 3 # disingkat Modulus 

print("Nilai b =",b) # 10 % 3 = 1 


---><---
 

print("\nDan Disingkat Menjadi :") 

b //= 2 # disingkat Division 

print("Nilai b =",b) # 10 % 2 = 5 


---><---


print("\nDan Disingkat Menjadi :") 

b **= 3 # disingkat Eksponen 

print("Nilai b =",b) # 10 ** 3 = 1000 



 
print("\n=====>Disingkat dgn Operasi Bitwise<=====") 

 
print("===OR (|)===") 
# OR (|) 

print("\n1. OR (|)") 

c = True  

c |= False 

print("Nilai c or False =",c) # True | False = True 
 
  
---><---  


print("\n2. OR") 

c = False  

c |= False 

print("Nilai c or False =",c) # False | False = False 


---><---


print("\n===AND (&)===")  
# AND (&) 


print("1. AND") 

c = True  

c &= False 

print("Nilai c & False =",c) # True & False = False 


---><---
 
  
print("\n2. AND") 

c = True  

c &= True 

print("Nilai c & False =",c) # True & True = True 

 

print("=====>Contoh dari biner<=====")
# ini contoh dari Shifting Right and Shifting Left 

d = 0b0100 

print("Nilai d =", format(d,'04b'))  


---><--- 


print("\nShifting Right") 

d >>= 2 

print("Nilai c >>= 2 =", format(d,'04b')) # 0100 >> 2 = 0001 


---><---


print("\nShifting Left") 

d <<= 1 

print("Nilai c <<= 1 =", format(d,'04b')) # 0100 << 1 = 0010 




