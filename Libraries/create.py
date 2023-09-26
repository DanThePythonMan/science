import os
for a in range(118):
  os.system(f"echo 'def el{a+1}():' >> test1.py")
  os.system("echo '  return ' >> test1.py")