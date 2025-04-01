temp_fah = float(input("Ingresa la tempertura en F: "))

temp_cel = ((temp_fah - 32)* 5) / 9

temp_kel = temp_cel + 273.15
print("Grados Celcius", temp_cel)
print ("Grados Kelvin", temp_kel)