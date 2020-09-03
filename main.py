#Kyle Chen kvc5823@psu.edu  
#Mitchell Feyl mmf5871@psu.edu
#Michael Lavallee mal6423@psu.edu
temperature = float(input ("Enter temperature in celsius: "))
unit = input("Enter unit in F/f or C/c: ")

if unit == "F" or unit == "f":
  NewTempinC = (((temperature - 32) * 5)/9)
  print(f"{temperature}° in Fahrenheit is equivalent to {NewTempinC}° Celsius.")
elif unit == "C" or unit == "c":
  NewTempinF = ((temperature * (9/5))+32)
  print(f"{temperature}° in Celsius is equivalent to {NewTempinF}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")

