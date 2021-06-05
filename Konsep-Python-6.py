# Konsep Python -6

 

print("\nOperasi Logika dan Boolean") 
# not, or, and, xor 



print("\n========NOT========") 


a = True 

c = not a 


print('data a = ',a) 

print("---------->NOT") 

print('data c = ',c) 
 
 

print("\n========OR========") 
# OR (Jika 2 buah False yg dimasukan akan menjadi false) 
 

# OR False and False 
a = False 

b = False 

c = a or b 

print(a,'OR',b,'=',c) 


# OR False and True 
a = False 

b = True 

c = a or b 

print(a,'OR',b,' =',c) 
 

# OR True and False 
a = True 

b = False 

c = a or b 

print(a,' OR',b,'=',c) 
 

# OR True and True 
a = True 

b = True 

c = a or b 

print(a,' OR',b,' =',c) 
# ket : JIKA ADA SALAH SATU YG TRUE, MAKA HASILNYA AKAN TRUE (or) 

 

print("\n========AND========") 
# AND (Jika 2 buat true yg dimasukan akan menjadi true) 


# AND False and False 

a = False 

b = False 

c = a and b 

print(a,'AND',b,'=',c) 

 
# AND False and True 
a = False 

b = True 

c = a and b 

print(a,' AND',b,'=',c) 
 

# AND True and False 
a = True 

b = False 

c = a and b 

print(a,'AND',b,'=',c) 

 
# AND True and True 
a = True  

b = True 

c = a and b 

print(a,' AND',b,'=',c) 
# ket : JIKA ADA SALAH SATU YG FALSE, MAKA HASILNYA AKAN FALSE (and) 

 
  
print("\n========XOR========") 
# XOR (Akan True Jika Salah Satu yg Ditulis True, Sisanya akan False) 

 
# XOR False and False 
a = False 

b = False 

c = a ^ b 

print(a,'XOR',b,'=',c) 

 
# XOR False and True 
a = False 

b = True 

c = a ^ b 

print(a,' XOR',b,'=',c) 
 

# XOR True and False 
a = True 

b = False 

c = a ^ b 

print(a,' XOR',b,'=',c) 


# XOR True and True 
a = True  

b = True 

c = a ^ b 

print(a,' XOR',b,'=',c) 

 
  
print("==========================================================================") 
 

  
print("\n=====>Gabungan Area Rentang dari Angka") 
# Logika dan Komparasi 
# Membuat gabungan area rentang dari angka 


print("\n+++++++++3--------------10+++++++++") 


inputUser = float(input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih dari 10\n: ")) 

 
# +++++3--------------- 
 

isKurangDari = (inputUser < 3) 

print("kurang dari 3 :1",isKurangDari) 


# -------------10+++++++ 
 

isLebihDari = (inputUser > 10) 

print("Lebih Dari 10 :",isLebihDari) 


# +++++++++3------OR------10+++++++++ 

 
isCorrect = isKurangDari or isLebihDari 

print("\nHasil dari OR",'=',isCorrect) 

 

print("\n-----------3+++++++++10-------------") 
# Kasus Irisan 
 

inputUser = float(input("Masukkan angka yang bernilai \nkurang dari 3 \ndan \nlebih dari 10\n: ")) 


# -------------3++++++++ 

 
isLebihDari = (inputUser > 3) 

print("lebih Dari 3 :",isLebihDari) 
 

# ++++++++++++10------- 

isKurangDari = (inputUser < 10) 

print("Kurang Dari 10 :",isKurangDari) 
 

# -----------3+++AND+++10------------- 
 

isCorrect = isLebihDari and isKurangDari 

print("\nHasil Dari AND :", isCorrect) 



print("\n",10*'=' + 'Latihan' + 10*'=') 
# Latihan  


print("\n-------0+++++++5-------8+++++++11-------") 
 

x = float(input("Masukkan angka :")) 
 

# ------------0+++++++ 
 

isLebihDari = (x > 0) 

print("\nKurang Dari 0 :",isLebihDari) 
 

# ++++++++++++5------- 


isKurangDari = (x < 5) 

print("Lebih Dari 5 :",isKurangDari) 
 

# ------------8+++++++ 


isLebihDari = (x > 8) 

print("Lebih Dari 8 :",isLebihDari) 


# +++++++++++11------- 


isKurangDari = (x < 11) 

print("Kurang Dari 11 :",isKurangDari) 

 
# -------0+++++++5--OR--8+++++++11------- 
 

isCorrect = isLebihDari or isKurangDari or isLebihDari or isKurangDari 

print("\nHasil Dari OR :", isCorrect) 

 

print("\n+++++++0-------5+++++++8--------11++++++") 

 
y = float(input("Masukkan Angka :")) 

 
# ++++++++++++0------- 


isKurangDari = (y < 0) 

print("\nKurang Dari 0 :",isKurangDari) 


# -----------5++++++++ 
 

isLebihDari : (y > 5) 

print("Lebih Dari 5 :",isLebihDari) 
 

# +++++++++++8-------- 
 

isKurangDari = (y < 8) 

print("Kurang Dari 8 :",isKurangDari) 
 

# ----------11++++++++ 


isLebihDari = (y > 11) 

print("Lebih Dari 11 :",isLebihDari) 
 

# +++++++0-------5++AND++8--------11++++++ 


isCorrect = isKurangDari and isLebihDari and isKurangDari and isLebihDari 

print("\nHasil Dari AND :",isCorrect) 



print("\n=====>cara if dan else<=====") # Cara ini akan Lebih mudah  
 

# OR 
x = float(input("masukkan angka : ")) 

if (x>0 and x<5) or (x>8 and x<11) : 
    print(True) 
else : 
    print(False) 


# AND 
x = float(input("masukkan angka : ")) 

if (x<0 and x>5) or (x<8 and x>11) : 
         print(True) 
else : 
         print(False) 
