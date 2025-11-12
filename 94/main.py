lista_numeros = [1, 2, 3] 

try:
    resultado = 9 / 1
    print(lista_numeros[3])

except ZeroDivisionError as e:
    print("Error Zero:", e)

except Exception as e:
    print("Error Except:", e)

finally:
    print("Finally")