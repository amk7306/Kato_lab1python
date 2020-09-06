# Author: Abbey Kato amk7306@psu.edu
#Collaborator: Jack Trueax jrt5617@psu.edu
#Collaborator: Jiahui Lan jzl6335@psu.edu

temp = input("Enter temperature: ")
symbol = input("Enter unit in F/f or C/c:")
celcius = float(temp)
fahrenheit = float(temp)
if  symbol == "F" or symbol == "f":
  print(f" {celcius}° in Fahrenheit is equivalent to {(celcius-32)*5/9}° Celsius.")
elif symbol == "C" or symbol == "c":
  print(f" {fahrenheit}° in Celsius is equivalent to {fahrenheit*9/5+32}° Fahrenheit.")
else:
 print(f" Invalid unit({symbol}).")
