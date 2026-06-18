class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_resumen(self):
        print(f"Restaurante: {self.nombre}")
        print(f"Productos registrados: {len(self.productos)}")
        print(f"Clientes registrados: {len(self.clientes)}")
        
    
    def __str__(self):
        return (
            f"Restaurante: {self.nombre}, "
            f"Productos: {len(self.productos)}, "
            f"Clientes: {len(self.clientes)}"
        )
