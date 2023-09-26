from Libraries import isupper
from Libraries import dict
def returnall():
  currentchem=""
  array = []
  print("For each element that is repeated, put it in that many times. Thanks!")
  chemical=input("Chemical? ")
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
        totalMass = "Hehe funny number"
        break
    try:
      int(totalMass)
      return totalMass
    except:
      return totalMass
  print(f"Relative Formula Mass is: {chemicalMass(array)}")
