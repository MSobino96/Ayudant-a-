#Definimos el stock del producto
stock_producto = 50 #Este valor puede ser modificado a gusto pero no ser menos a 20

# funcion realizar compra

def realizar_compra(stock_producto):
    unidades_solicitadas = int(input("\n Ingrese la cantidad de uunidades a solicitar: "))


    if unidades_solicitadas > 20:
        print("\n No es posible solicitar más de 20 artartículos")

    elif unidades_solicitadas > stock_producto:
        print("No es posible realizar esta compra ya que no hay stock suficiente")

    else:
        #si compra m[as de 12 articulos se agrega 1
        if unidades_solicitadas > 12 and stock_producto - unidades_solicitadas >=1:
            unidades_solicitadas += 1
            print("Se he añadido una unidad extra por que compré más de 12 unidades")

        stock_producto -= unidades_solicitadas
        print(f"Pedido se realiz[o con exito. Unidades solicitadas: {unidades_solicitadas}, Stock Actual: {stock_producto}.")
    
    return stock_producto

while stock_producto > 0:
    print(f"Stock inicial del producto: {stock_producto}")
    stock_producto = realizar_compra(stock_producto)

    continuar = input("Desea realizar otra compra? (si o no):")

    if continuar != "si":
        print("gracias por tu compra. Hasta la proxima!")
        break 

if stock_producto <= 0:
    print("El stock se ha agotado")





   
