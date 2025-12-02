"""
Modulo de Modelos - Producto
Define las entidades principales del sistema, adaptadas para una Botica.
"""
from datetime import datetime
from enum import Enum

class Categoria(Enum):
    """Enumeracion de categorias de productos en una Botica (Farmacia)."""
    MEDICAMENTOS_CON_RECETA = "Medicamentos con Receta"
    MEDICAMENTOS_LIBRE_VENTA = "Medicamentos de Venta Libre"
    CUIDADO_PERSONAL = "Cuidado Personal"
    SUPLEMENTOS = "Vitaminas y Suplementos"
    MATERIAL_CURACION = "Material de Curacion"
    BEBES_Y_NINOS = "Bebés y Niños"
    OTROS = "Otros Productos de Botica"

class Producto:
    """
    Representa un producto en el inventario de la botica.

    Attributes:
        id_producto (int): Identificador unico
        nombre (str): Nombre del producto (ej: Paracetamol, Pañales)
        descripcion (str): Descripcion del producto
        precio (float): Precio unitario
        cantidad (int): Cantidad en stock
        categoria (Categoria): Categoria del producto
        fecha_creacion (str): Fecha de creacion
    """
    
    _contador = 1000
    
    def __init__(self, nombre: str, descripcion: str, precio: float,
                 cantidad: int, categoria: Categoria):
        """
        Inicializa un producto.
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede ser vacio")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo") 
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        Producto._contador += 1
        self.id_producto = Producto._contador
        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")