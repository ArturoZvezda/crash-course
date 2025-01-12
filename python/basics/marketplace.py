class Producto:
    def __init__(self,nombre,precio,inventario):
        self.__nombre = nombre
        self.__precio = precio
        self.__inventario = inventario
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value
 
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = value

    @property
    def inventario(self):
        return self.__inventario

    @inventario.setter
    def inventario(self, value):
        if value < 0:
            raise ValueError("El inventario no puede ser negativo.")
        self.__inventario = value


    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f}"

class DescuentoMixin:
    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Se aplicó un descuento del {porcentaje}%. Nuevo precio: ${self.precio:.2f}")

class InventarioMixin:
    def aumentar_inventario(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a aumentar debe ser mayor que cero.")
        self.inventario += cantidad
        print(f"Inventario aumentado en {cantidad}. Nuevo inventario: {self.inventario}")

    def disminuir_inventario(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a disminuir debe ser mayor que cero.")
        if cantidad > self.inventario:
            raise ValueError("No se puede disminuir más inventario del disponible.")
        self.inventario -= cantidad
        print(f"Inventario disminuido en {cantidad}. Nuevo inventario: {self.inventario}")

class RegistroVentasMixin:
    def __init__(self):
        self._ventas = []  # Lista para registrar las ventas
        self._ingresos_totales = 0  # Acumula ingresos generados

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")
        if cantidad > self.inventario:
            raise ValueError("No hay suficiente inventario para realizar la venta.")
        
        # Disminuir inventario
        self.inventario -= cantidad
        
        # Calcular el ingreso
        ingreso = cantidad * self.precio
        self._ingresos_totales += ingreso
        
        # Registrar la venta
        self._ventas.append({"cantidad": cantidad, "ingreso": ingreso})
        print(f"Venta registrada: {cantidad} unidades vendidas por ${ingreso:.2f}")
    
    @property
    def ventas(self):
        return self._ventas

    @property
    def ingresos_totales(self):
        return self._ingresos_totales


class ProductoConDescuento(Producto, DescuentoMixin):
    pass

class ProductoCompleto(Producto, DescuentoMixin, InventarioMixin, RegistroVentasMixin):
    def __init__(self, nombre, precio, inventario):
        Producto.__init__(self, nombre, precio, inventario)
        RegistroVentasMixin.__init__(self)  # Inicializamos el mixin de ventas
