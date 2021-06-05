print("Membuat Macam String")


data = "ini adalah String" 

print(data) 

print(type(data)) 


 ---><---

  
# 1. cara membuat string 
 

''' 

   1, dengan menggunakan single qoute '...'

   2, dengan menggunakan double qoute "..." 

''' 
 

data = 'menggunakan single qoute' # Single Qoute ('')

print(data) 



data = "menggunakan double qoute" # Single Qoute ("")

print(data) 

 
  
# dan bisa juga disatukan kedua duanya 
# contoh  


data = ('"Hello World"') # dan juga bisa kebalikannya   

print(data) 


---><---


# 2, menggunakan tanda (\) 
# contoh 


data = ('mari kita sholat jum\'at berjama\'ah') # kita harus menggunakan tanda (\) supaya terbaca 

print(data) 

data = ('i don\'t care') # kalau males pake kutip 2  

print(data) 


# Backlash 

print('C:\\User\\Abdul Hamid') # Dijadikan Double Backlash 


#Tab 

print('New\tOld') # Ini untuk menjauhi jarak kata (Tab) 


# backSpace 

print("New \bOld") # Ini tidak ada spasi, jadi kata "NewOld" 
 

# Newline 

print("Baris Pertama.\nBaris Kedua.") # Ini akan Membuat baris baru (LF -> Line Feed) --> INi Dipake untuk Unix, macOS, Linux 

print("Baris Pertama.\rBaris Kedua.") # CR -> Carriage return Line Feed --> Ini dipake untuk Commodore, Acorn, dan Lips 

print("Baris Pertama.\r\nBaris Kedua.") # CRLF -> Carriage return --> Dipake untuk Windows 

 
---><---
 

# 3. String Literal atau Raw 


# HATI - HATI JANGAN BIKIN KAYAK GINI : 
print('C:\new Folder') # INI AKAN SALAH PATH NYA 



# Tips kalau ada banyak backlash (biar gk salah path nya) 
# Yaitu Menggunakan Raw String 
 
print(r'C:\new Folder') # Ini Baru Yang Bener, Gak ada masalah 

 

# Muliline LIteral String 

print(""" 

Nama : Abdul Hamid 

Kelas : X MIPA 1 

""") # Ini yg ditampilkan akan sama yg kita ketik, baik enternya, dan juga newline. 

 

# Multiline String and Raw 

print(r""" 

Nama : \Abdul\ Hamid 

Kelas : X\n MIPA \t1 

""") # Ini Akan Menampilkan Tanda Backlash, Newline, Tab 
# Ini Biasa digunakan untuk menulis panjang 



