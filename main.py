import os

def clearScreen():
   if os.name == 'nt':
      os.system('cls')

   else:
      os.system("clear")

# Rumus Konversi Celcius
def rumus_celcius(input_celcius):
   Celcius_Fahrenheit = (9/5 * input_celcius) + 32
   Celcius_Kelvin = input_celcius + 273.15
   Celcius_Reamur = 4/5 * input_celcius

   # Hasil konversi celcius
   print(f"{input_celcius}\u00B0C to {Celcius_Fahrenheit:.2f}\u00B0F")
   print(f"{input_celcius}\u00B0C to {Celcius_Kelvin:.2f}\u00B0K")
   print(f"{input_celcius}\u00B0C to {Celcius_Reamur:.2f}\u00B0R")

   return   

# Rumus Konversi Fahrenheit
def rumus_fahrenheit(input_fahrenheit):
   Fahrenheit_Celcius =  (5/9) * (input_fahrenheit - 32)
   Fahrenheit_Kelvin =  (5/9) * (input_fahrenheit - 32) + 273.15
   Fahrenheit_Reamur = (4/9) * (input_fahrenheit - 32)

   # Hasil konversi fahrenheit
   print(f"{input_fahrenheit}\u00B0F to {Fahrenheit_Celcius:.2f}\u00B0C")
   print(f"{input_fahrenheit}\u00B0F to {Fahrenheit_Kelvin:.2f}\u00B0K")
   print(f"{input_fahrenheit}\u00B0F to {Fahrenheit_Reamur:.2f}\u00B0R")

   return

# Rumus Konversi Kelvin
def rumus_kelvin(input_kelvin):
   Kelvin_Celcius = input_kelvin - 273.15
   Kelvin_Fahrenheit = (9/5) * (input_kelvin - 273.15) + 32
   Kelvin_Reamur = (4/5) * (input_kelvin - 273.15)

   # Hasil konversi kelvin
   print(f"{input_kelvin}\u00B0K to {Kelvin_Celcius:.2f}\u00B0C")
   print(f"{input_kelvin}\u00B0K to {Kelvin_Fahrenheit:.2f}\u00B0F")
   print(f"{input_kelvin}\u00B0K to {Kelvin_Reamur:.2f}\u00B0R")

   return
   
# Rumus Konversi Reamur
def rumus_reamur(input_reamur):
   Reamur_Celcius = (5/4) * input_reamur
   Reamur_Fahrenheit =  (9/4) * input_reamur + 32
   Reamur_Kelvin =  (5/4) * input_reamur + 273.15

   # Hail konversi Reamur
   print(f"{input_reamur}\u00B0R to {Reamur_Celcius:.2f}\u00B0C")
   print(f"{input_reamur}\u00B0R to {Reamur_Fahrenheit:.2f}\u00B0F")
   print(f"{input_reamur}\u00B0R to {Reamur_Kelvin:.2f}\u00B0K")

   return

sama_dengan = '='*10
while True:
   # Menu utama
   print(f"{sama_dengan} Menu Conversion {sama_dengan}")
   print("1. Celcius Conversion")
   print("2. Fahrenheit Conversion")
   print("3. Kelvin Conversion")
   print("4. Reamur Conversion")
   print("0. Exit")
   # user menentukan menu
   menu_utama = input("\n[+] Make a choice using number: ")
   clearScreen()
   
   if menu_utama == '1':
      input_celcius = float(input("[+] Enter value: "))
      clearScreen()
      rumus_celcius(input_celcius)

      # submenu
      print("\n9. Return to the main menu")
      print("0. Exit")
      submenu = input("\n[+] Make a choice: ")

      if submenu == '9':
         clearScreen()
         continue

      elif submenu == '0':
         print("Thanks for using this tools")
         break

      else:
         print("Invalid number")
         break

   elif menu_utama == '2':
      input_fahrenheit = float(input("[+] Enter value: "))
      clearScreen()
      rumus_fahrenheit(input_fahrenheit)

      # submenu
      print("\n9. Return to the main menu")
      print("0. Exit")
      submenu = input("\n[+] Make a choice: ")

      if submenu == '9':
         clearScreen()
         continue

      elif submenu == '0':
         print("Thanks for using this tools")
         break

      else:
         print("Invalid number")
         break
   
   elif menu_utama == '3':
      input_kelvin = float(input("[+] Enter value: "))
      clearScreen()
      rumus_kelvin(input_kelvin)

      # submenu
      print("\n9. Return to the main menu")
      print("0. Exit")
      submenu = input("\n[+] Make a choice: ")

      if submenu == '9':
         clearScreen()
         continue

      elif submenu == '0':
         print("Thanks for using this tools")
         break

      else:
         print("Invalid number")
         break

   elif menu_utama == '4':
      input_reamur = float(input("[+] Enter value: "))
      clearScreen()
      rumus_reamur(input_reamur)

      # submenu
      print("\n9. Return to the main menu")
      print("0. Exit")
      submenu = input("\n[+] Make a choice: ")

      if submenu == '9':
         clearScreen()
         continue

      elif submenu == '0':
         print("Thanks for using this tools")
         break

      else:
         print("Invalid number")
         break
   
   elif menu_utama == '0':
      print("Have a nice day")
      break

   else:
      print("Ivalid number")
      break