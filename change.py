def change():
    # Pedir valores al usuario
    gasto = float(input("Ingresar gasto: "))
    dinero_recibido = float(input("Ingresar dinero recibido: "))

    # Cálculo del vuelto
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)  
    centavos = int(round((vuelto - pesos) * 100))  

    # Imprimir resultados
    print("\nVuelto")
    print(" ")
    print(f"Pesos: {pesos}")
    print(f"Centavos: {centavos}")

# Llamar a la función
change()
