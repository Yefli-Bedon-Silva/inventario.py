# inventario.py
import time  # Defecto 1: Importación no utilizada
import math  # Defecto 2: Importación no utilizada

def agregarRepuesto(nombre, precio, lista=[]): # Defecto 3: Uso de camelCase en lugar de snake_case y argumento por defecto mutable (lista=[])
    nuevo_item = {"nombre": nombre, "precio": precio}
    lista.append(nuevo_item)
    
    variable_temporal = 100 # Defecto 4: Variable declarada pero nunca usada
    
    return lista

def CalcularTotal(inventario): # Defecto 5: Función empieza con mayúscula
    Total = 0 # Defecto 6: Variable empieza con mayúscula
    
    # Defecto 7: Forma no "pythonica" de iterar, Codacy sugerirá usar "for item in inventario:"
    for i in range(len(inventario)):
        Total = Total + inventario[i]["precio"]
        
    return Total

def main():
    print("Iniciando sistema de inventario...")
    
    mi_inventario = []
    mi_inventario = agregarRepuesto("Compresor VRF", 1250.50, mi_inventario)
    mi_inventario = agregarRepuesto("Filtro de aire", 45.00, mi_inventario)
    mi_inventario = agregarRepuesto("Válvula", 85.20, mi_inventario)
    
    resultadoFinal = CalcularTotal(mi_inventario)
    
    print("El valor total del inventario es: " + str(resultadoFinal))

if __name__ == "__main__":
    main()
