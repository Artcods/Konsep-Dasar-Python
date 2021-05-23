# Python 2
 

print("casting") 
# Casting itu adalah merubah dari satu tipe ke tipe lain 
# Data tipe = int, float, string, bool 
# int = Integer
# float = Float
# str = String
# bool = Boolean
 
  

print("=================Integer=================") 


data_int = 9 

print("data :", data_int, ",type =",type(data_int)) 

 

# mengubah data int ke data lainnya 

data_float = float(data_int) 
data_str   = str(data_int) 
data_bool  = bool(data_int) # akan false jika int = 0 

print("data :", data_float, ",type =",type(data_float)) 
print("data :", data_str, ",type =",type(data_str)) 
print("data :", data_bool, ",type =",type(data_bool)) 



print("=================float===================") 
 

data_float = 6.9 

print("data :", data_float, ",type =",type(data_float)) 

 

# mengubah data float ke data lainnya 

data_int   = int(data_float) # 9.9 akan dibulatkan ke bawah 
data_str   = str(data_float) 
data_bool  = bool(data_float) # akan false jika float = 0 

print("data :", data_int, ",type =",type(data_int)) 
print("data :", data_str, ",type =",type(data_str)) 
print("data :", data_bool, ",type =",type(data_bool)) 

 

print("=================String==================") 
 

data_str = "10" 

print("data :", data_str, ",type =",type(data_str)) 

 

# mengubah data str ke data lainnya 

data_int   = int(data_str) # 9.9 akan dibulatkan ke bawah 
data_float   = float(data_str) 
data_bool  = bool(data_str) # akan false jika float = 0 

print("data :", data_int, ",type =",type(data_int)) 
print("data :", data_float, ",type =",type(data_float)) 
print("data :", data_bool, ",type =",type(data_bool)) 

 
  
print("=================Boolean==================") 
 

data_bool = True # Bisa True atau False 

print("data :", data_bool, ",type =",type(data_bool)) 

 

# mengubah data bool ke data lainnya 

data_int   = int(data_bool) # 9.9 akan dibulatkan ke bawah 
data_float   = float(data_bool) 
data_str  = str(data_str) # akan false jika float = 0 

print("data :", data_int, ",type =",type(data_int)) 
print("data :", data_float, ",type =",type(data_float)) 
print("data :", data_str, ",type =",type(data_str)) 


  

print("<===Contoh Lain===>") 

# Ini adalah contoh lain dari tipe data string 

 

print("===string===") 

 

data_str = "halo" # tidak di isi angka maka data lain akan error  

print("data :", (data_str), ",type =", type(data_str)) 

 

data_int   = int(data_str) # Data str ke int akan error 
data_float   = float(data_str) # Data str ke float akan error 
data_bool  = bool(data_str) # Data str ke bool akan error atau hasilnya false 

print("data :", data_int, ",type =",type(data_int)) 
print("data :", data_float, ",type =",type(data_float)) 
print("data :", data_bool, ",type =",type(data_bool)) 

 

print("===>Kesimpulannya<===") 

  
# data_int : di integer string harus angka 

# data_float : di float string harus angka 

# data_bool : di bool jika string tidak di isi maka false 
