'''
Returneaza 1 daca n este prim si 0 daca nu.
'''
def is_prime(n):
  if n > 1:
      for i in range(2, int(n / 2) + 1):
          if (n % i) == 0:
              return 0
  else:
    return 1
  return 0

  
'''
Returneaza produsul numerelor din lista list.
'''
def get_product(list):
  ans = 1
  for i in list:
      ans *= i
  return ans
  
  
'''
Returneaza CMMDC a doua numere x si y folosind algoritmul lui Euclid.
'''
def get_cmmdc_v1(x, y):
  while x!=y :
    if x>y  :
      x=x-y
    else:
      if x<y:
        y=y-x
  return x      


    

  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y): 
  r = x%y
  while r!=0:
    x=y
    y=r
    r=x%y
  return y


    



def main():
  # interfata de tip consola aici
  print("""
Meniu:
1. Verificati daca un numar este prim
2. Produsul numerelor dintr-o lista
3. CMMDC Euclid 
4. CMMDC impartiri repetate
  """)
  option = int(input("Selectati o optiune: "))

  if option == 1:
      num = int(input("Introduceti un numar: "))
      if is_prime(num):
          print("Prim")
      else:
          print("Neprim")

  elif option == 2:
      str_list = input("Introduceti pe rand numere separate prin cate un spatiu: ")
      map_obj = map(int, str_list.split())
      lst = list(map_obj)
      print(get_product(lst))

  elif option == 3 or option == 4:
      x = int(input("Introduceti primul numar: "))
      y = int(input("Introduceti cel de-al doilea numar: "))
      if option == 3:
          print(get_cmmdc_v1(x, y))
      else:
          print(get_cmmdc_v2(x, y))
  else:
      print("Nu ati selectat o optiune valida!")



if __name__ == '__main__':
  main()