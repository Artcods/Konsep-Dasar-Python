# Konsep Python -3


print("=====>Input data<=====") 
# Mengimput data 

 

data = input("masukan data: ") 
# text yang ditulis akan masuk ke data string 

print("data =", data, ",type =", type(data)) 

 

print("\n===input dengan data int===") 


data_int = int(input("masukan angka: ")) 

print("data =", data_int, ",type =", type(data_int)) 

 

print("\n===Input dengan data float===") 


data_float = float(input("masukan angka: ")) 

print("data =", data_float, ",type =", type(data_float)) 

 

print("\n===Input dengan bool===") 


data_bool = bool(input("masukan angka: ")) 

print("data =", data_bool, ",type =", type(data_bool)) 

 

print("\ncontoh dengan bool/biner") 


biner = bool(int(input("masukan nilai boolean: "))) 

# Ketika, 1 = true,  

# dan ketika 0 = false  

print("data =", biner, ",type =", type(biner)) 


 
print("==================================================================================")
 

  
print("=====>Operasi Aritmatika<=====")  

 
a = 10 

b = 5 

 
x = 9 

y = 2 

 

print("===Operasi Pertambahan===") 


hasil = a + b 

print(a,'+',b,'=',hasil) 


hasil = x + y 

print(x,'+',y,'=',hasil) 

 

print("===Operasi Pengurangan===") 
 

hasil = a - b 

print(a,'-',b,'=',hasil) 

 
hasil = x - y 

print(x,'-',y,'=',hasil) 

 

print("===Operasi Perkalian===") 
 

hasil = a * b 

print(a,'*',b,'=',hasil) 


hasil = x * y 

print(x,'*',y,'=',hasil) 

 

print("===Operasi Pembagian===") 


hasil = a / b 

print(a,'/',b,'=',hasil) 
 

hasil = x / y 

print(x,'/',y,'=',hasil) 
 

 
print("===Operasi Pangkat/Exponen===") 
 

hasil = a ** b 

print(a,'**',b,'=',hasil) # 10 di pangkatkan 3 (10*10*10) 

 
hasil = x ** y 

print(x,'**',y,'=',hasil) # 10 di pangkatkan 2 (10*10) 



print("===Modulus===") 
# Modulus adalah sisa dari pembagian  
 

hasil = a % b 

print(a,'%',b,'=',hasil) 


hasil = x % y 

print(x,'%',y,'=',hasil) 

 

print("===Floor Division===") 
# Membulatkan hasil dari pembagian 
 

hasil = a // b  

print(a,'//',b,'=',hasil) 
 

hasil = x // y 

print(x,'//',y,'=',hasil) 

 

print("===Operasi prioritas===") 
 

hasil = a + y - b * x / a ** y % b // x 

print(a,'+',y,'-',b,'*',x,'/',a,'**',y,'%',b,'//',x,'=',hasil) 

 
# Jika ada tanda kurung maka yg tanda kurung di prioritaskan 

 
hasil = a - y * (b + x) / a ** y % b // x 

print(a,'-',y,'*',b,'+',x,'/',a,'**',y,'%',b,'//',x,'=',hasil) 

# Hasilnya akan berbeda jika ada tanda kurung 
# Dikarnakan tanda yg dikurung akan mengambil langka pertama 

 

 

 

 

 

# jadi ini rumus operasi yg di proritasakan 

 

''' 

    1. Pertambahan (+)

    2. Pengurangan (-)

    3. Perkalian (*)

    4. Pembagian (/) 
    
    5. Pangkat/Exponen (**)
    
    6. Modulus (%)
    
    7. Floor Division

''' 
