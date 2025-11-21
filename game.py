def main():
  profit = 0
  tool = "teeth"
  earning_power = 1

  print("""
  
    Opportunity awaits! 
    
    Make money TODAY... cutting grass. 

    No drug test or proof of citizenship required.
    No tools or experience needed. 

  """)

  running = True
  while running:

    print("""
    
      Cut some grass, make some money... whaddya say?
      
        1. Whateva, sure... I'll cuts some damn grass!
        2. I wanna buy a tool.
        3. Nah, I'll take some free government handouts.

    """)

    option = input("Whaddya wanna do: ").strip()

    if option == "1":
      profit += earning_power
    elif option == "2":
      if profit >= 5 and tool == "teeth":
        print("""
        
          Available Tools:

            1. Rusty old scissors
            2. Nevamind
            
        """)

        choice = input().strip("Well, what's it gonna be?")

        if choice == "1":
          profit -= 5
          tool = "rusty old scissors"
          earning_power = 5
        elif choice == "2":
          pass
        else:
          print("You can't do that!")
      else:
        print("You don't have enough to buy a tool you fool!")
    elif option == "3":
      running = False
    else:
      print("What the hell you tryin to do...?")

    print("You only have "+ str(profit) +" dollars." )

if __name__ == "__main__":
  main()