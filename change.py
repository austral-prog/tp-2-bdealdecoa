def change():
    # Pedir valores al usuario
    # gasto = float(input("Ingresar gasto: "))
    gasto = 23.75
    print(f"Ingresar gasto:\n{gasto}")
    # dinero_recibido = float(input("Ingresar dinero recibido "))
    dinero_recibido = 100
    print(f"Dinero recibido\n{dinero_recibido}")

    # Cálculo del vuelto
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)  
    centavos = int(round((vuelto - pesos) * 100))  

    # Imprimir resultados
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")


