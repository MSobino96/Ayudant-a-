#[]
#{}
#() tuplas 

productos = {
    "notebooks": 100000,
    "monitores": 30000
}

def calcular_valores():
    total_pedido = 0

    #Solicitar cantidad por cada producto y calcular el subtotal
    for producto, precio in productos.items():
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        valorneto = cantidad * precio
        total_pedido + valorneto

        

#TODO calculos (suma neto, suma iva, total)
    #iva al 19%
    iva = total_pedido * 0.19

    total_final = total_pedido + iva

    print(f"Total neto del pedido: ${total_pedido}")
    print(f"Total iva del pedido: ${iva}")
    print(f"Total del pedido: ${total_final}")

        

calcular_valores()
