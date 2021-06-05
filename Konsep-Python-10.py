print("\n====>If Else (if statement)<====") 
# Menentukan Hasil Boolean True atau False 


print("Contoh Pertama") 

x = 10 
 
y = 5 
 

if x > y : # Harus Memakai Titik 2 

    print("Betul") 

else: 

    print("Salah") 

    
---><--- 


print("Contoh Kedua") 

x = 10 

y = 5 
 

if y < x: # Harus Memakai Titik 2 

    print("Betul") 

else: 

    print("Salah") 

    
---><--- 


print("\n-------3++++6----AND---7++++2-------") 


x = float(input("Masukkan angka = ")) 
 

if (x>3 and x<6) or (x>7 and x<2 ) : 

    print("Betul") 

else: 

    print("Salah") 

    
---><---  


print("\n--------3++++6----OR---7++++2-------") 

 
x = float(input("Masukkan angka = ")) 


if (x<3 or x>6) and (x<7 or x>2 ) : 

    print("Betul") 
else: 
    print("Salah") 

 
---><---  


print("\n====>If Else dan Elif<====") 
# Elif adalah Menentukan Syarat yg belum terpenuh  


print("Contoh Pertama") 
 
  
hutang = input("Masukkan Uang anda =") 

Uang = 20000 
 

if int(hutang) > Uang : 
    print("Kelebihan") 
    
elif int(hutang) == Uang : 
  
    print("Cukup") 
else : 
    print("Tidak Cukup") 

    
---><--- 


print("\n====>If Else dan Elif<====") 
# Elif adalah Menentukan Syarat yg belum terpenuh  
 

  
print("\nContoh Pertama") 


hutang = input("Masukkan Uang anda =")  

Uang = 20000 


if int(hutang) < Uang : 
    print("Tidak Cukup")  

     
elif int(hutang) == Uang : 
  
    print("Cukup") 
else : 
    print("Kelebihan") 



print("\nContoh Kedua") 


''' 

    Seseorang sedang mencari teman 

    yang baik dan rajin 

''' 
 

si = "Orang Baik" 

baik = True 

rajin = True 
 

if baik & rajin & (si == "Orang Jahat"): 
    print("Gak Teman") 
 

elif baik & rajin & (si == "Orang Baik"): 

    print("Temenan") 
else: 
    print("Gak Sopan") 
    
   
    
---><---    


    
si = "Orang Jahat"

baik = True

rajin = True
 
if baik & rajin & (si == "Orang Jahat") :
    print("Gak Teman")
 
elif baik & rajin & (si == "Orang Baik") :

    print("Temanan")
else:
    print("Gak Sopan")
    
    
    
    
