proc=input("""
What do you need?
1) mass/volume
2) moles/volume
""")
if proc=="1":
  mass=float(input("What is the mass in kg? "))
  volume=float(input("What is the volume in meters cubed? "))
  print(f"Concentration is {mass/volume}kg/meters cubed.")
elif proc=="2":
  moles=float(input("What is the number of moles? "))
  volume=float(input("What is the number of dm³? "))
  print(moles/volume)
  