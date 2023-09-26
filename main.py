def main():
    import os
    a=True
    try:
      while a == True:
        process=input("""What process do you want to use?
        1) Relative Formula Mass

        2) Mol triangle calculator

        3) Surface area to Volume ratio

        4) Volume calculator

        5) Concentration 

        6) % Yield

        7) Atom Economy

        """)
        if process=="1":
          a=False
          os.system("clear")
          import rfm
          while True:
            rfm.returnall()
        elif process=="2":
          a=False
          os.system("clear")
          import moles
          while True:
            moles.moles()
          
        elif process=="3":
          a=False
          os.system("clear")
          import savr
          while True:
            savr.savr()

        elif process=="4":
          a=False
          os.system("clear")
          import volume
          while True:
            volume.volume()
          
        elif process=="5":
          os.system("clear")
          while True:
            import conc
        elif process=="6":
          os.system("clear")
          import percentYield
          while True:
            percentYield.percentYield()
          
        elif process== "7":
          import atomEconomy
          os.system("clear")
          while True:
            
            atomEconomy.atomEconomy()
        else:
          print("You were not understood. Please try again \n")
    except:
      print("Something went wrong, please try again.")
if __name__ == "__main__":
  main()