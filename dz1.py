def pal(slovo):
   a = slovo[::-1]
   return slovo == a
slovo = str(input())
print(pal(slovo))
