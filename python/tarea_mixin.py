import marketplace

# Crear un producto con descuento
televisor = marketplace.ProductoConDescuento("Televisor", 1000,10)
print(televisor)  # Televisor - Precio: $1000.00

# Aplicar un descuento
televisor.aplicar_descuento(10)  # Se aplicó un descuento del 10%. Nuevo precio: $900.00
print(televisor)  # Televisor - Precio: $900.00


# Crear un producto completo
laptop = marketplace.ProductoCompleto("Laptop", 1500, 10)

# Mostrar información inicial
print(laptop)  # Laptop - Precio: $1500.00

# Aplicar descuento
laptop.aplicar_descuento(15)  # Se aplicó un descuento del 15%. Nuevo precio: $1275.00
print(laptop)  # Laptop - Precio: $1275.00

# Aumentar inventario
laptop.aumentar_inventario(5)  # Inventario aumentado en 5. Nuevo inventario: 15

# Disminuir inventario
laptop.disminuir_inventario(3)  # Inventario disminuido en 3. Nuevo inventario: 12

# Intentar disminuir más inventario del disponible
try:
    laptop.disminuir_inventario(20)
except ValueError as e:
    print(e)  # No se puede disminuir más inventario del disponible.


# Crear un producto completo
laptop = marketplace.ProductoCompleto("Laptop", 1500, 10)

# Mostrar información inicial
print(laptop)  # Laptop - Precio: $1500.00

# Registrar una venta
laptop.registrar_venta(2)  # Venta registrada: 2 unidades vendidas por $3000.00

# Verificar ingresos totales
print(f"Ingresos totales: ${laptop.ingresos_totales:.2f}")  # Ingresos totales: $3000.00

# Verificar ventas registradas
print("Historial de ventas:", laptop.ventas)  # [{"cantidad": 2, "ingreso": 3000.0}]

# Intentar vender más del inventario disponible
try:
    laptop.registrar_venta(8)
except ValueError as e:
    print(e)  # No hay suficiente inventario para realizar la venta.
