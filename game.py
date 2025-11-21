
profit = 0

running = True
while running:

  print("""
  
  Yo, want some money? Cut some grass and I'll give you dollar.
  
    1. Whateva, sure... I'll cuts some damn grass!
    2. Nah, I'll take some free government handouts.

  """)

  option = input("Whaddya wanna do: ").strip()

  if option == "1":
    profit += 1
  elif option == "2":
    running = False
  else:
    print("You can only choose #1 or 2.")

  print("You made "+ str(profit) +" dollars." )

