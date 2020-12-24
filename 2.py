def leapyear(year):
  if 0 == year % 4 and 0 != year % 100 or 0 == year % 400:
    print(year,"-> true")
  else:
    print(year,"-> false")
leapyear(1600)
leapyear(2000)
leapyear(1500)
leapyear(2004)
leapyear(2008)
leapyear(2010)