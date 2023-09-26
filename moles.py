import sys
from Libraries import isupper
from Libraries import dict
def moles():
  def chemmass(chemical):
    currentchem=""
    array = []
    for i in range(0,len(chemical)):
      try: nexti = chemical[i+1]
      except: nexti=""
      else:
        nexti = chemical[i+1]
      if isupper.check_upper(chemical[i]) == True:
        if isupper.check_lower(nexti) == True:
          array.append(chemical[i]+nexti)
        else:
          array.append(chemical[i])
    #print(array)
    def chemicalMass(array):
      totalMass=0
      for i in range(0,len(array)):
        totalMass+=dict.eturn(array[i])
        if dict.eturn(array[i]) == -1:
          totalMass = "Yes."
          break
      try:
        int(totalMass)
        return totalMass
      except:
        return totalMass
  
    return chemicalMass(array)
  proc2=input("""What do you need?
  1) Mass 
  2) Number of Moles
  3) Relative Formula Mass
  """)
  if proc2=="1":
    moles=float(input("What is the number of moles? "))
    loop=True
    while loop == True:
      yorno=input("""
    Do you know the relative formula mass or the chemical equasion?
    1) RFM
    2) Chemical Equasion
    """)
      if yorno=="1":
        loop=False
        rfm=float(input("What is the Relative formula mass? "))
      elif yorno =="2":
        loop=False
        chemical=input("What is the chemical equation?(For each element that is repeated, put it in that many times. Thanks!) ")
        rfm=float(chemmass(chemical))
      else:
        print("You were not understood, try again")
    #print(rfm)
    
    mass=float(moles*rfm)
    try:
      mass=int(mass)
      #print(mass)
    finally:
      mass=str(mass)
      #print(f"mass is {mass}")
      mass=mass+"g"
      print(f"Mass is {mass}.")
  elif proc2 =="2":
    mass=float(input("What is the mass in grammes? "))
    loop=True
    while loop == True:
      
      yorno=input("""
    Do you know the relative formula mass or the chemical equasion?
    1) RFM
    2) Chemical Equasion
    """)
      if yorno=="1":
        loop=False
        rfm=float(input("What is the Relative formula mass? "))
      elif yorno =="2":
        loop=False
        chemical=input("What is the chemical equation?(For each element that is repeated, put it in that many times. Thanks!) ")
      else:
        print("You were not understood, try again")
    rfm=float(chemmass(chemical))
    print(rfm)
    moles=float(mass/rfm)
    print(str(moles)+" mol")
  elif proc2=="3":
    mass=input("What is the mass in grammes? ")
    moles=input("What is the number of moles? ")
    try:
      mass=float(mass)
      moles=float(moles)
    finally:
      a=mass/moles
      print(f"Relative formula mass is {a}")
  else:
    print("Something was wrong, please try again.")
moles()
