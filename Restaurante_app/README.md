# Sistema de Gestión de Restaurante — POO en Python

**Nombre:** Isabel Katherine Montaño Montaño  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 4  

---

## Descripción del sistema

Sistema básico de gestión para un restaurante desarrollado en Python
aplicando Programación Orientada a Objetos. Permite registrar productos
del menú, gestionar clientes y consultar información general del negocio
desde la consola.

---

## Estructura del proyecto
restaurante_app/

├── modelos/

│   ├── producto.py     # Clase Producto

│   └── cliente.py      # Clase Cliente

├── servicios/

│   └── restaurante.py  # Clase Restaurante

└── main.py             # Punto de entrada

README.md

---

## Explicación de cada archivo

- **modelos/producto.py:** contiene la clase `Producto` con atributos
  como nombre, categoría, precio y disponibilidad. Incluye métodos para
  aplicar descuentos y cambiar disponibilidad.

- **modelos/cliente.py:** contiene la clase `Cliente` con atributos como
  cédula, nombre, email y teléfono. Gestiona el historial de pedidos y
  calcula el total gastado.

- **servicios/restaurante.py:** contiene la clase `Restaurante` que
  importa los modelos y administra las listas de productos y clientes.

- **main.py:** punto de arranque del programa. Crea los objetos y
  ejecuta los métodos para demostrar el funcionamiento del sistema.

---

## Cómo ejecutar

```bash
cd restaurante_app
python main.py
```

---

## Reflexión

Estructurar el código en módulos independientes con tareas específicas es esencial en la creación de software. Al asignar una única función a cada archivo, realizar cambios en una sección del sistema no impacta otras partes. La clase `Producto` puede ser modificada sin alterar `Cliente`, y el servicio `Restaurante` puede expandirse sin dañar los modelos. Esta distribución también potencia la colaboración en grupo, optimiza la claridad del código y facilita la ampliación del proyecto. Implementar POO con una correcta organización desde el principio representa una inversión en la calidad y el cuidado del software a largo plazo.