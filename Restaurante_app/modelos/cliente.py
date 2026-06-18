class Cliente:
    
    def __init__(self,cedula_cliente, nombre, email, telefono):
        self.cedula_cliente = cedula_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return (
            f"Cédula: {self.cedula_cliente} | "
            f"Nombre: {self.nombre} | "
            f"Email: {self.email} | "
            f"Teléfono: {self.telefono}"
        )