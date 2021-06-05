# Konsep Python -4 



print("=====>Konversi Satuan Temperature<=====") 
# Program Konversi Celsius ke Satuan yg lain 



print("\n===PROGRAM KONVERSI TEMPERATURE===\n") 


celcius = float(input("Masukkan suhu : ")) 

print("Suhu Celsius adalah", celcius, "Celcius") 


print("--->Reamur") 


reamur = (4/5) * celcius 
print("Suhu Reamur adalah", reamur, "Reamur") 


print("--->Fahrenheit")


fahrenheit = ((9/5) * celcius) + 32 
print("Suhu Fahrenheit adalah",fahrenheit, "fahrenheit") 


print("--->kelvin") 


kelvin = celcius + 273 
print("Suhu Kelvin", kelvin, "Kelvin") 



print("========================================================================")



# mencari suhu fahrenheit ke kelvin dan, kelvin ke fahrenheit
print("=====>Fahrenhait Ke Kelvin<=====") 

 

fahrenheit = float(input("Masukkan Suhu : ")) 

print("Suhu Fahrenheit adalah", fahrenheit,("Fahrenheit")) 


celcius = fahrenheit - 32 # rumus
kelvin = ((5/9) * celcius) + 273 # rumus


print("Hasil Suhu Kelvin ",kelvin, "Kelvin") 

 

print("=====>Kelvin Ke Fahrenheit<=====") 

 

kelvin = float(input("Masukkan suhu : ")) 

print("Suhu Kelvin : ", kelvin, ("Kelvin")) 


celcius = kelvin - 273 # rumus
fahrenheit = ((9/5) * celcius) + 32 # rumus

 
print("Hasil Suhu Kelvin ke Fahrenheit adalah ",fahrenheit, "Fahrenheit")
