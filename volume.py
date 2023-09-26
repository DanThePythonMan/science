
def cubevolume():
  a=input("What is the width in meters? ")
  b=input("What is the height in meters? ")
  c=input("What is the length in meters? ")
  try:
    a=float(a)
    b=float(b)
    c=float(c)
  except:
    print("You entered a wrong character. Please try again")
  finally:
    tot=a*b*c
    try:
      tot=int(tot)
    finally:
      print(f"Volume is {tot} meters cubed")
def spherevolume():
  import math as maths
  r=float(input("What is the radius in m? "))
  try:
    print(f"Area is {4/3*maths.pi*(int(r)**3)}meters cubed")
  except:
    print(f"Area is {4/3*maths.pi*r**3}meters cubed")
def conevolume():
  import math as maths
  r=float(input("What is the radius in m? "))
  h=float(input("What is the height in m? "))
  try:
    r=int(r)
    h=int(h)
  finally:
    print(f"Area is {maths.pi*(r**2)*(h/3)}meters cubed")
proc=input("""What do you want to do?
1) Volume of cube/rectangle
2) Volume of sphere
3) Volume of cone
""")
if proc == "1":
  cubevolume()
elif proc=="2":
  spherevolume()
elif proc=="3":
  conevolume()
else:
  import sys
  sys.exit("Something went wrong.")