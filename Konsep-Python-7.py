print("Operator Bitwise/Binery") 
# Operator bitwise, Disebut juga operasi biner (BINERY) 




print("\n=====>Operator Bitwise<=====") 


a = 9 

b = 5 


print('nilai :',a,'binery : ', format(a,'08b')) 

print('nilai :',b,'binery : ', format(b,'08b')) 
# Mengoperator bitwise atau binery memakai keyword (format) 



  
print("\n=====>Bitwise OR<=====") 
# Bitwise OR (|) 


print('nilai :',a,'binery : ', format(a,'08b')) 

print('nilai :',b,'binery : ', format(b,'08b')) 

print("-------------------------------------(|)") 

 
c = a | b 

print('nilai :',c,'binery :', format(c,'08b')) 

 
  

print("\n=====>Bitwise AND<=====")  
# Bitwise AND (&) 


print('nilai :',a,'binery : ', format(a,'08b')) 

print('nilai :',b,'binery : ', format(b,'08b')) 

print("-------------------------------------(&)") 
 

c = a & b 

print('nilai : ',c,'binery :', format(c,'08b')) 


 
  
print("\n=====>Bitwise XOR<=====") 
# Bitwise XOR (^) 


print('nilai :',a,'binery : ', format(a,'08b')) 

print('nilai :',b,'binery : ', format(b,'08b')) 

print("-------------------------------------(^)") 

 
c = a ^ b 

print('nilai :',c,'binery :', format(c,'08b')) 




print("\n=====>Bitwise NOT (~a)<=====")  
# Bitwise NOT (~a) 
 

print('nilai :',a,'binery : ', format(a,'08b')) 

print("-------------------------------------(~)") 
 

c = ~a 

print('nilai:',c,'binery :', format(c,'08b')) 




print("\n=====>Bitwise NOT (~b)<=====") 
# Bitwise NOT (~b) 

 
print('nilai :',b,'binery : ', format(b,'08b')) 

print("-------------------------------------(~)") 

 

c = ~b 

print('nilai:',c,'binery : ', format(c,'08b')) 

  

print("=====>Flip NOT<=====") 


d = 0b0000001001 

e = 0b1111111111 
 

print('nilai :',e^d,'binery : ', format(e^d,'08b')) 


 
print("\n=====>Shifting Right (>>)<=====")  
# Shifting right (>>) 
 

print('nilai :',b,'binery : ', format(b,'08b')) 

c = a >> 2 

print("-------------------------------------(>>)") # Ini bakal geser ke kanan 
 

print('nilai :',c,'binery : ', format(c,'08b')) 
 
  

  
print("\n=====>Shifting Right (<<)<=====") 
# Shifting Left (<<) 
 

print('nilai :',b,'binery : ', format(b,'08b')) 

c = a << 2 

print("-------------------------------------(<<)") # Ini bakal geser ke kiri 
 

print('nilai :',c,'binery :', format(c,'08b')) 

 
