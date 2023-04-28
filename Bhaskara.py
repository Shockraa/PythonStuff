print("Descobrir o Delta e X1 e X2")
a = float(input("Insira o valor do A: "))
b = float(input("Insira o valor do B: "))
c = float(input("Insira o valor do C: "))
Delta = float(b**2-4*a*c)

if a == 0:
    print("Não pode ser zero")
  
elif Delta < 0:
    print("Não tem raízes reais")
  
else:
    x1 = (-b + Delta ** (1 / 2)) / (2 * a)
    x2 = (-b - Delta ** (1 / 2)) / (2 * a)
    print(f"O valor do Delta = {Delta}")
    print(f"O valor do x1 = {x1}")
    print(f"O valor do x2 = {x2}")
  input()
