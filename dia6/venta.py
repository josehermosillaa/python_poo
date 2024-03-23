class DetalleVentaItem():
    def __init__(self, producto:str, cantidad:int):
        self.__producto = producto
        self.__cantidad = cantidad

    @property ## getter obtener un atributo
    def producto(self):
        return self.__producto
    
    @property
    def cantidad(self):
        return self.__cantidad


class DetalleVenta():
    def __init__(self):
        self.__items = []

    def agregar_item(self,item:DetalleVentaItem):
        self.__items.append(item)
    
    def __str__(self):
        retorno = (f""":::::::::::: DETALLE DE ESTA VENTA :::::::::::::::::
        PRODUCTO        CANTIDAD
        """)

        items = [f"{i.producto}     {i.cantidad}\n" for i in self.__items]

        return f"{retorno}{''.join(items)}"


class Venta():
    def __init__(self):
        self.__detalle = DetalleVenta()

    def modificar_detalle(self, producto:str, cantidad:int):
        detalle_venta_item = DetalleVentaItem(producto, cantidad)
        self.__detalle.agregar_item(detalle_venta_item)

    @property
    def detalle(self):
        return self.__detalle


# paracetamol = DetalleVentaItem('paracetamol', 100)
# venta1 = DetalleVenta()
# venta1.agregar_item(paracetamol)

# print(venta1)