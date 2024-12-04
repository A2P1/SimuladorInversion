

def main():
    menu()

def menu():
    print("Bienvenido a la simulacion de inversion")
    monto = int(input("Primero ingrese el monto inicial para la inversión"))
    interes = float(input("A continuación, introduzca el porcentaje en decimal de la tasa de interés anual"))
    tiempo = int(input("Por último, ingrese el tiempo en años de la inversión"))

    CantidadFinal = inversion(monto, interes, tiempo)
    print("La Cantidad final es: ", CantidadFinal)
def inversion(monto, interes, tiempo):
    CantidadFinal = monto * (1 + interes) ** tiempo #Formula de la inversión
    return CantidadFinal

main()