from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


restaurante = Restaurante("La Sason Deliciosa")


p1 = Producto("P001", "Papas fritas", 5.50)
p2 = Producto("P002", "Batido de fresa", 3.99)
p3 = Producto("P003", "Café americano", 1.75)

c1 = Cliente("1234567890", "Leonardo Pérez", "Leonardo@example.com", "0987654321")
c2 = Cliente("0987654321", "Viviana Gómez", "Viviana@example.com", "1234567890")

restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)
restaurante.agregar_producto(p3)


restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)

print(restaurante)
restaurante.mostrar_resumen()


print("\n---Productos registrados---")
for producto in restaurante.productos:
    print(producto)

print("\n---Clientes registrados---")
for cliente in restaurante.clientes:
    print(cliente)