num = int(input("Enter Number : "))
star = int(num/2)
temp = 0 if num % 2 == 0 else 1
space = 0
space_in = num - 2
for row in range(star):
  txt = ""
  print((" " * space) + "*" + (" " * space_in) + "*" if num > 1 else "")

  space += 1
  space_in -= 2

txt = (" " * star) + "*" if temp == 1 else ""
if txt:
  print(txt)

space = star - 1
space_in = 0 if num % 2 == 0 else 1
for row in range(star):
  txt = ""
  print((" " * space) + "*" + (" " * space_in) + "*" if num > 1 else "")

  space -= 1
  space_in += 2