# Author: Abbey Kato amk7306@psu.edu
#Collaborator: Jack Trueax jrt5617@psu.edu
#Collaborator: Jiahui Lan jzl6335@psu.edu

temp = input("Enter temperature: ")#the temperature equals the code inputer will put in
symbol = input("Enter unit in F/f or C/c:")#the symbol(C or F) depends on what they put in
celcius = float(temp)#celcius is a float of the input temp
fahrenheit = float(temp)#fahrenheit is a float of the input temp
if  symbol == "F" or symbol == "f":#if the symbol is equal to fahrenheit...
  print(f" {celcius}° in Fahrenheit is equivalent to {(celcius-32)*5/9}° Celsius.")#you subtract 32 and then multiply 5 and divide by 9
elif symbol == "C" or symbol == "c":#else if, its celcius they want to conver to...
  print(f" {fahrenheit}° in Celsius is equivalent to {fahrenheit*9/5+32}° Fahrenheit.")#print out the fahrenheit which is multiply 9 and divide by 5 and add 32
else:
 print(f" Invalid unit({symbol}).")#this is if they input something either than C/c or F/f
